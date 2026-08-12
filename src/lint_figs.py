"""Flag text/path overlap, text/text overlap, and viewBox overflow in every figure."""
import re, math

CSS = open("style.css").read()

# class -> (font-size px, is_mono)
SIZE, MONO = {}, {}
for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", CSS):
    m = re.search(r"font-size:\s*([\d.]+)px", body)
    fam = "mono" in body
    for s in sel.split(","):
        s = s.strip()
        key = s.split()[-1].lstrip(".").split("{")[0]
        key = key.replace("text", "").strip(". ") or s.strip().lstrip(".")
        for c in re.findall(r"\.([a-zA-Z0-9_-]+)", s):
            if m: SIZE.setdefault(c, float(m.group(1)))
            if fam: MONO.setdefault(c, True)

def flatten(d):
    """Return sample points along a path's geometry."""
    pts, cur, start = [], (0.0, 0.0), (0.0, 0.0)
    toks = re.findall(r"([MmLlHhVvCcZz])([^MmLlHhVvCcZz]*)", d)
    for cmd, arg in toks:
        n = [float(x) for x in re.findall(r"-?\d+\.?\d*", arg)]
        rel = cmd.islower(); C = cmd.upper()
        if C == "M":
            for i in range(0, len(n) - 1, 2):
                p = (cur[0] + n[i], cur[1] + n[i+1]) if rel else (n[i], n[i+1])
                cur = p
                if i == 0: start = p
                pts.append(p)
        elif C == "L":
            for i in range(0, len(n) - 1, 2):
                p = (cur[0] + n[i], cur[1] + n[i+1]) if rel else (n[i], n[i+1])
                for t in range(1, 11):
                    pts.append((cur[0] + (p[0]-cur[0])*t/10, cur[1] + (p[1]-cur[1])*t/10))
                cur = p
        elif C == "H":
            for v in n:
                p = (cur[0] + v, cur[1]) if rel else (v, cur[1])
                for t in range(1, 21):
                    pts.append((cur[0] + (p[0]-cur[0])*t/20, cur[1]))
                cur = p
        elif C == "V":
            for v in n:
                p = (cur[0], cur[1] + v) if rel else (cur[0], v)
                for t in range(1, 11):
                    pts.append((cur[0], cur[1] + (p[1]-cur[1])*t/10))
                cur = p
        elif C == "C":
            for i in range(0, len(n) - 5, 6):
                c1 = (cur[0]+n[i], cur[1]+n[i+1]) if rel else (n[i], n[i+1])
                c2 = (cur[0]+n[i+2], cur[1]+n[i+3]) if rel else (n[i+2], n[i+3])
                p  = (cur[0]+n[i+4], cur[1]+n[i+5]) if rel else (n[i+4], n[i+5])
                for t in range(1, 25):
                    u = t/24; v = 1-u
                    pts.append((v**3*cur[0] + 3*v*v*u*c1[0] + 3*v*u*u*c2[0] + u**3*p[0],
                                v**3*cur[1] + 3*v*v*u*c1[1] + 3*v*u*u*c2[1] + u**3*p[1]))
                cur = p
        elif C == "Z":
            cur = start
    return pts

def text_boxes(svg):
    out = []
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", svg, re.S):
        attrs, body = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
        if "transform" in attrs: continue          # rotated axis labels
        xm = re.search(r'\bx="(-?[\d.]+)"', attrs); ym = re.search(r'\by="([\d.]+)"', attrs)
        if not (xm and ym): continue
        x, y = float(xm.group(1)), float(ym.group(1))
        classes = re.findall(r'class="([^"]*)"', attrs)
        cls = classes[0].split() if classes else []
        # inherit from nearest enclosing <g class=...>
        before = svg[:m.start()]
        gs = re.findall(r'<g class="([^"]*)"', before)
        cand = cls + (gs[-1].split() if gs else [])
        size = next((SIZE[c] for c in cand if c in SIZE), 13.0)
        mono = any(c in MONO for c in cand)
        body = re.sub(r"&[a-z#0-9]+;", "X", body).strip()
        w = len(body) * size * (0.62 if mono else 0.58)
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        a = anchor.group(1) if anchor else "start"
        x0 = x - w if a == "end" else (x - w/2 if a == "middle" else x)
        out.append((x0, y - size*0.78, x0 + w, y + size*0.24, body))
    return out

def check(svg, name):
    issues = []
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    W, H = (float(vb.group(1)), float(vb.group(2))) if vb else (1060, 400)
    boxes = text_boxes(svg)

    for x0, y0, x1, y1, body in boxes:
        if x1 > W + 1 or x0 < -1 or y1 > H + 1:
            issues.append("OVERFLOW  %-46s box=(%.0f,%.0f)-(%.0f,%.0f) vb=%gx%g" %
                          (body[:44], x0, y0, x1, y1, W, H))

    for d in re.findall(r'<path[^>]*\bd="([^"]+)"', svg):
        if len(d) < 4: continue
        pts = flatten(d)
        for x0, y0, x1, y1, body in boxes:
            hits = [p for p in pts if x0+2 < p[0] < x1-2 and y0+1 < p[1] < y1-1]
            if len(hits) >= 2:
                issues.append("LINE-THRU %-46s path crosses at ~(%.0f,%.0f)" %
                              (body[:44], hits[len(hits)//2][0], hits[len(hits)//2][1]))
                break

    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            a, b = boxes[i], boxes[j]
            ox = min(a[2], b[2]) - max(a[0], b[0]); oy = min(a[3], b[3]) - max(a[1], b[1])
            if ox > 6 and oy > 3:
                issues.append("TEXT-OVER %-46s and %s" % (a[4][:44], b[4][:34]))
    return issues

html = open("../index.html").read()
svgs = re.findall(r"<svg.*?</svg>", html, re.S)
total = 0
for i, s in enumerate(svgs, 1):
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    iss = check(s, i)
    total += len(iss)
    if iss:
        print("\nfig%02d  %s" % (i, (t.group(1)[:64] if t else "")))
        for x in dict.fromkeys(iss): print("   ", x)
print("\n%d issue(s) across %d figures" % (total, len(svgs)))
