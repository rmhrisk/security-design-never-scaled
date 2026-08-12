import re, cairosvg, os, sys
TOK={"--paper":"#f4f5f6","--panel":"#eaecee","--ink":"#12171d","--ink-soft":"#414c56",
     "--muted":"#78838d","--rule":"#d3d8dc","--accent":"#a3202a","--removed":"#a4adb5",
     "--affirm":"#17604f","--serif":"Georgia,serif","--sans":"Helvetica,sans-serif",
     "--mono":"monospace"}
h=open("../index.html").read()
css=re.search(r"<style>(.*?)</style>", h, re.S).group(1)
css=re.sub(r"@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", css, flags=re.S).replace("&","and")
for k,v in TOK.items(): css=css.replace("var(%s)"%k, v)
os.makedirs("render", exist_ok=True)
svgs=re.findall(r"<svg.*?</svg>", h, re.S)
for i,s in enumerate(svgs,1):
    for k,v in TOK.items(): s=s.replace("var(%s)"%k, v)
    doc = s if "xmlns" in s else s.replace("<svg",'<svg xmlns="http://www.w3.org/2000/svg"',1)
    doc = re.sub(r"(<svg[^>]*>)", r"\1<style><![CDATA[%s]]></style>"%css, doc, count=1)
    cairosvg.svg2png(bytestring=doc.encode(), write_to="render/fig%02d.png"%i,
                     output_width=1060, background_color="#f4f5f6")
print("rendered", len(svgs))
