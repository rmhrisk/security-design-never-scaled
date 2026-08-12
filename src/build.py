#!/usr/bin/env python3
"""Assemble security-design-never-scaled-v3.md into a standalone HTML post."""
import re, markdown, html as htmllib
from figs import FIGA, FIGB, FIGC, FIGD, FIGE, FIGF, FIGG, FIGH, FIGI, FIGJ, FIGK

SRC = "essay.md"
OUT = "../index.html"

# ---------------------------------------------------------------- figures ---

HERO = '''
<figure class="hero-fig">
<svg viewBox="0 0 1060 400" role="img" aria-labelledby="h0t">
  <title id="h0t">A reachable path through a system graph, unchanged by a fully satisfied column of security artifacts</title>
  <text class="s-eyebrow accent" x="20" y="24">A PERFECTLY DOCUMENTED INSECURE SYSTEM</text>

  <text class="s-panelhead" x="20" y="62">THE SYSTEM</text>
  <text class="s-sub" x="20" y="80">authority, trust boundaries, dependencies, failure modes</text>

  <g class="h-graph">
    <path class="dim" d="M60 140 L150 112 M150 112 L240 132 M240 132 L232 200 M150 112 L232 200 M240 132 L318 108 M318 108 L318 232 M318 108 L392 160 M60 140 L232 200 M240 132 L318 232"/>
    <path class="live" d="M60 140 L138 186 L232 200 L318 232 L384 168"/>
    <path class="live-head" d="M392 160 L387.5 171.2 L380.7 164.2 Z"/>
    <circle class="dim" cx="150" cy="112" r="6"/><circle class="dim" cx="240" cy="132" r="6"/>
    <circle class="dim" cx="318" cy="108" r="6"/>
    <circle class="on" cx="60"  cy="140" r="7"/><circle class="on" cx="138" cy="186" r="7"/>
    <circle class="on" cx="232" cy="200" r="7"/><circle class="on" cx="318" cy="232" r="7"/>
    <circle class="end" cx="392" cy="160" r="9"/>
  </g>
  <text class="h-tag" x="60" y="122" text-anchor="middle">entry</text>
  <text class="h-tag" x="404" y="146">consequence</text>
  <text class="h-tag" x="150" y="262">four steps, every one sanctioned</text>

  <g class="h-arrow">
    <path d="M448 172 H598"/>
    <path class="h-fill" d="M604 172 l-10 -6 v12 z"/>
    <text x="523" y="158" text-anchor="middle">compression</text>
    <text x="523" y="196" text-anchor="middle" class="s-sub">the threat model falls out here</text>
  </g>

  <text class="s-panelhead" x="650" y="62">WHAT WE BUY INSTEAD</text>
  <text class="s-sub" x="650" y="80">legible, testable, budgeted, transactable</text>
  <g class="h-token">
    <rect x="650" y="98"  width="200" height="30" rx="3"/><text x="662" y="118">HSM</text><text x="836" y="118" text-anchor="end" class="tick">deployed</text>
    <rect x="650" y="136" width="200" height="30" rx="3"/><text x="662" y="156">SBOM</text><text x="836" y="156" text-anchor="end" class="tick">current</text>
    <rect x="650" y="174" width="200" height="30" rx="3"/><text x="662" y="194">MFA</text><text x="836" y="194" text-anchor="end" class="tick">98%</text>
    <rect x="650" y="212" width="200" height="30" rx="3"/><text x="662" y="232">Audit</text><text x="836" y="232" text-anchor="end" class="tick">unqualified</text>
    <rect x="650" y="250" width="200" height="30" rx="3"/><text x="662" y="270">Pentest</text><text x="836" y="270" text-anchor="end" class="tick">passed</text>
  </g>
  <text class="h-tag" x="870" y="186">the budget</text>
  <text class="h-tag" x="870" y="204">goes here</text>

  <path class="h-under" d="M20 318 H1040"/>
  <text class="h-verdict" x="530" y="348" text-anchor="middle">Every row on the right is green. The path on the left is unchanged.</text>
  <text class="s-sub" x="530" y="372" text-anchor="middle">Not one of those controls is wrong. None of them is the property anyone wanted.</text>
</svg>
<figcaption>The reductio, up front. You can satisfy every requirement in the right-hand column and still leave a four-step route from an internet-facing system to the authority that ends the company.</figcaption>
</figure>
'''
FIG1 = '''
<figure class="fig">
<svg viewBox="0 0 1060 400" role="img" aria-labelledby="f1t">
  <title id="f1t">A six-step attack path in which every edge is sanctioned and no team owns the path</title>
  <text class="s-eyebrow" x="20" y="26">EVERY EDGE HAS AN OWNER AND A REASON</text>

  <g class="s-owner">
    <text x="95"  y="60" text-anchor="middle">Platform</text>
    <text x="265" y="60" text-anchor="middle">Identity</text>
    <text x="435" y="60" text-anchor="middle">AppSec</text>
    <text x="605" y="60" text-anchor="middle">Cloud</text>
    <text x="775" y="60" text-anchor="middle">SRE</text>
    <text x="945" y="60" text-anchor="middle">PKI</text>
  </g>
  <g class="s-tick">
    <path d="M95 70 v14"/><path d="M265 70 v14"/><path d="M435 70 v14"/>
    <path d="M605 70 v14"/><path d="M775 70 v14"/><path d="M945 70 v14"/>
  </g>

  <g class="s-edgelabel">
    <text x="180" y="170" text-anchor="middle">is supposed</text><text x="180" y="184" text-anchor="middle">to have</text>
    <text x="350" y="170" text-anchor="middle">is supposed</text><text x="350" y="184" text-anchor="middle">to reach</text>
    <text x="520" y="170" text-anchor="middle">is supposed</text><text x="520" y="184" text-anchor="middle">to deploy</text>
    <text x="690" y="170" text-anchor="middle">needs authority</text><text x="690" y="184" text-anchor="middle">in</text>
    <text x="860" y="170" text-anchor="middle">is supposed</text><text x="860" y="184" text-anchor="middle">to invoke</text>
  </g>

  <g class="s-node">
    <rect x="20"  y="200" width="150" height="62" rx="4"/>
    <rect x="190" y="200" width="150" height="62" rx="4"/>
    <rect x="360" y="200" width="150" height="62" rx="4"/>
    <rect x="530" y="200" width="150" height="62" rx="4"/>
    <rect x="700" y="200" width="150" height="62" rx="4"/>
    <rect x="870" y="200" width="150" height="62" rx="4" class="s-node-end"/>
  </g>
  <g class="s-nodetext">
    <text x="95"  y="226" text-anchor="middle">Internet-facing</text><text x="95"  y="244" text-anchor="middle">service</text>
    <text x="265" y="226" text-anchor="middle">Application</text><text x="265" y="244" text-anchor="middle">identity</text>
    <text x="435" y="226" text-anchor="middle">CI</text><text x="435" y="244" text-anchor="middle">system</text>
    <text x="605" y="226" text-anchor="middle">Deployment</text><text x="605" y="244" text-anchor="middle">credential</text>
    <text x="775" y="226" text-anchor="middle">Production</text><text x="775" y="244" text-anchor="middle">administration</text>
    <text x="945" y="226" text-anchor="middle" class="s-end">Signing</text><text x="945" y="244" text-anchor="middle" class="s-end">service</text>
  </g>

  <g class="s-path">
    <path d="M170 231 H184"/><path d="M340 231 H354"/><path d="M510 231 H524"/>
    <path d="M680 231 H694"/><path d="M850 231 H864"/>
    <g class="s-head">
      <path d="M178 225 l8 6 -8 6z"/><path d="M348 225 l8 6 -8 6z"/><path d="M518 225 l8 6 -8 6z"/>
      <path d="M688 225 l8 6 -8 6z"/><path d="M858 225 l8 6 -8 6z"/>
    </g>
  </g>

  <path class="s-brace" d="M20 300 v12 H1020 v-12"/>
  <text class="s-caption" x="520" y="342" text-anchor="middle">The path has neither.</text>
  <text class="s-sub" x="520" y="368" text-anchor="middle">Six owners, five sanctioned edges, and no one accountable for what they compose into.</text>
</svg>
<figcaption>Figure 1 &middot; Every step is somebody’s intended behaviour. The composition is nobody’s.</figcaption>
</figure>
'''

FIG2 = '''
<figure class="fig">
<svg viewBox="0 0 1060 470" role="img" aria-labelledby="f2t">
  <title id="f2t">Five candidate designs for one security property, compared by which attack paths each removes</title>
  <text class="s-eyebrow" x="20" y="26">DESIRED PROPERTY</text>
  <text class="s-prop" x="20" y="54">Compromise of the application must not disclose persistent signing authority.</text>

  <g class="s-colhead">
    <text x="470" y="104" text-anchor="middle">app compromise</text><text x="470" y="118" text-anchor="middle">discloses key</text>
    <text x="610" y="104" text-anchor="middle">host compromise</text><text x="610" y="118" text-anchor="middle">discloses key</text>
    <text x="750" y="104" text-anchor="middle">app compromise</text><text x="750" y="118" text-anchor="middle">signs arbitrarily</text>
    <text x="880" y="104" text-anchor="middle">long-lived key</text><text x="880" y="118" text-anchor="middle">exists at all</text>
    <text x="990" y="111" text-anchor="middle">cost</text>
  </g>
  <path class="s-rule" d="M20 132 H1040"/>

  <g class="s-rowlabel">
    <text x="20" y="171">Key in an environment variable</text>
    <text x="20" y="229">Separate signer process, same host</text>
    <text x="20" y="287">Separate signer host</text>
    <text x="20" y="345">Remote KMS or HSM</text>
    <text x="20" y="403">Protocol redesign, no long-lived key</text>
  </g>

  <g class="s-cell">
    <circle cx="470" cy="165" r="9" class="on"/>  <circle cx="610" cy="165" r="9" class="on"/>  <circle cx="750" cy="165" r="9" class="on"/>  <circle cx="880" cy="165" r="9" class="on"/>
    <circle cx="470" cy="223" r="9" class="off"/> <circle cx="610" cy="223" r="9" class="on"/>  <circle cx="750" cy="223" r="9" class="on"/>  <circle cx="880" cy="223" r="9" class="on"/>
    <circle cx="470" cy="281" r="9" class="off"/> <circle cx="610" cy="281" r="9" class="off"/> <circle cx="750" cy="281" r="9" class="on"/>  <circle cx="880" cy="281" r="9" class="on"/>
    <circle cx="470" cy="339" r="9" class="off"/> <circle cx="610" cy="339" r="9" class="off"/> <circle cx="750" cy="339" r="9" class="on"/>  <circle cx="880" cy="339" r="9" class="on"/>
    <circle cx="470" cy="397" r="9" class="off"/> <circle cx="610" cy="397" r="9" class="off"/> <circle cx="750" cy="397" r="9" class="off"/> <circle cx="880" cy="397" r="9" class="off"/>
  </g>

  <g class="s-cost">
    <rect x="950" y="160" width="14" height="10"/>
    <rect x="950" y="218" width="24" height="10"/>
    <rect x="950" y="276" width="46" height="10"/>
    <rect x="950" y="334" width="72" height="10"/>
    <rect x="950" y="392" width="90" height="10" class="s-cost-alt"/>
  </g>

  <path class="s-rule faint" d="M20 425 H1040"/>
  <g class="s-legend">
    <circle cx="28" cy="450" r="7" class="on"/><text x="44" y="455">path remains</text>
    <circle cx="164" cy="450" r="7" class="off"/><text x="180" y="455">path removed</text>
    <text x="1040" y="455" text-anchor="end" class="s-sub">The last row changes the problem rather than the storage.</text>
  </g>
</svg>
<figcaption>Figure 2 &middot; One property, five candidate architectures. Each removes some paths, leaves others, and costs differently. None of them is &ldquo;the secure option.&rdquo;</figcaption>
</figure>
'''

FIG3 = '''
<figure class="fig">
<svg viewBox="0 0 1060 480" role="img" aria-labelledby="f3t">
  <title id="f3t">A loop in which design asserts what must remain true and implementation evidence contradicts it</title>

  <text class="s-eyebrow" x="20" y="26">WHAT WE ASSERT MUST REMAIN TRUE</text>
  <text class="s-eyebrow accent" x="1040" y="412" text-anchor="end">WHAT THE SYSTEM ACTUALLY DOES</text>

  <g class="s-node">
    <rect x="30"  y="80"  width="180" height="60" rx="4"/>
    <rect x="290" y="80"  width="180" height="60" rx="4"/>
    <rect x="550" y="80"  width="180" height="60" rx="4"/>
    <rect x="820" y="200" width="200" height="60" rx="4"/>
    <rect x="550" y="330" width="180" height="60" rx="4"/>
    <rect x="250" y="330" width="200" height="60" rx="4" class="s-node-alert"/>
  </g>
  <g class="s-nodetext">
    <text x="120" y="107" text-anchor="middle">Desired security</text><text x="120" y="125" text-anchor="middle">property</text>
    <text x="380" y="116" text-anchor="middle">Threat model</text>
    <text x="640" y="116" text-anchor="middle">Design</text>
    <text x="920" y="236" text-anchor="middle">Implementation</text>
    <text x="640" y="366" text-anchor="middle">Observation</text>
    <text x="350" y="366" text-anchor="middle" class="s-alert">Contradiction</text>
  </g>

  <g class="s-flow">
    <path d="M210 110 H278"/><path d="M470 110 H538"/>
    <path d="M730 110 C 800 110 820 150 830 194"/>
    <g class="s-head">
      <path d="M272 104 l8 6 -8 6z"/><path d="M532 104 l8 6 -8 6z"/><path d="M824 188 l8 12 -13 2z"/>
    </g>
  </g>

  <g class="s-flow back">
    <path d="M880 260 C 860 316 800 360 738 360"/>
    <path d="M550 360 H462"/>
    <path d="M250 360 C 150 360 150 200 300 145"/>
    <g class="s-head">
      <path d="M744 354 l-10 6 10 6z"/><path d="M468 354 l-10 6 10 6z"/><path d="M296 152 l12 -8 2 13z"/>
    </g>
    <text class="s-flowlabel" x="600" y="410" text-anchor="middle">evidence argues back</text>
    <text class="s-flowlabel" x="150" y="250" text-anchor="middle">redesign</text>
  </g>

  <text class="s-sub" x="530" y="456" text-anchor="middle">The threat model stops being a launch document and becomes a hypothesis the system can falsify.</text>
</svg>
<figcaption>Figure 3 &middot; Design asserts what must remain true; implementation, observation, and contradiction get to disagree.</figcaption>
</figure>
'''

# --------------------------------------------------------------- assembly ---

md = open(SRC).read()

# Title + dek live outside the markdown body.
lines = md.split("\n")
title = lines[0].lstrip("# ").strip()
dek = ""
for ln in lines[1:]:
    if ln.startswith("### "):
        dek = ln[4:].strip()
        break
body_md = md.split(dek, 1)[1].lstrip("\n") if dek else "\n".join(lines[1:])

# Figure anchors.
anchors = [
    ("The threat model that justified the rule goes, and so does the reasoning that would tell you when the rule no longer applies.", "@@FIGH@@"),
    ("The governance that makes the path meaningful is another.", "@@FIGA@@"),
    ("It persists because nothing in the market currently makes the alternative visible.", "@@FIGI@@"),
    ("**Dogma replaces optimization with classification.**", "@@FIGB@@"),
    ("**Regressus ad infinitum.**", "@@FIGC@@"),
    ("survives so much spending.", "@@FIG1@@"),
    ("an interval measured in tens of minutes against a release measured in weeks is the thing defenders now have to reconsider.", "@@FIGD@@"),
    ("That is the reasoning the control cliff destroyed, made explicit enough to compare.", "@@FIG2@@"),
    ("**desired property \u2192 threat model \u2192 design \u2192 implementation \u2192 observation \u2192 contradiction \u2192 redesign**", "@@FIG3@@"),
    ("Only the last step changes what the machine is for.", "@@FIGF@@"),
]
for needle, token in anchors:
    if needle not in body_md:
        raise SystemExit("anchor not found: " + needle[:40])
    body_md = body_md.replace(needle, needle + "\n\n" + token, 1)

body_md = re.sub(
    r"::: aside\n(.*?)\n:::",
    lambda m: '<div class="aside" markdown="1">\n\n' + m.group(1) + "\n</div>",
    body_md, flags=re.S)

body_md = re.sub(
    r"::: lede\n(.*?)\n:::",
    lambda m: '<p class="lede" markdown="1">' + m.group(1) + "</p>",
    body_md, flags=re.S)

body_md = re.sub(
    r"::: keylesson\n(.*?)\n:::",
    lambda m: '<div class="keylesson" markdown="1"><span>Key lesson</span>\n\n' + m.group(1) + "\n</div>",
    body_md, flags=re.S)

body = markdown.markdown(
    body_md,
    extensions=["extra", "smarty"],
    extension_configs={"smarty": {"smart_dashes": False, "smart_ellipses": False}},
)

# Number the sections and drop in Part dividers.
PARTS = {
    1: ("I", "The Compression",
        "We compressed judgment because it was expensive."),
    8: ("II", "The Mismatch",
        "Attackers never accepted the compression, and cheap reasoning enlarges the asymmetry."),
    11: ("III", "The Representation",
        "The way out is not better controls. It is making the original reasoning cheap enough to run again."),
}
counter = {"n": 0}
toc = []

def h2(m):
    counter["n"] += 1
    n = counter["n"]
    text = m.group(1)
    sid = "s%d" % n
    if n in PARTS:
        toc.append(("part", "p" + PARTS[n][0], "Part %s \u00b7 %s" % PARTS[n][:2]))
    toc.append((n, sid, re.sub(r"<[^>]+>", "", text)))
    out = ""
    if n in PARTS:
        num, name, gist = PARTS[n]
        pid = "p" + num
        out += ('<div class="partbreak" id="%s"><span class="partnum">Part %s</span>'
                '<h2 class="partname">%s</h2><p class="partgist">%s</p></div>\n'
                ) % (pid, num, name, gist)
    out += '<h3 class="sec" id="%s"><span class="secnum">%d</span>%s</h3>' % (sid, n, text)
    return out

body = re.sub(r"<h2>(.*?)</h2>", h2, body, flags=re.S)
body = body.replace("<h3>Sources</h3>", '<h3 class="tail" id="sources">Sources</h3>')

for token, fig in (("@@FIGH@@", FIGH), ("@@FIGI@@", FIGI), ("@@FIGK@@", FIGK),
                   ("@@FIGA@@", FIGA), ("@@FIGB@@", FIGB), ("@@FIGC@@", FIGC),
                   ("@@FIG1@@", FIG1), ("@@FIGD@@", FIGD), ("@@FIGE@@", FIGE),
                   ("@@FIG2@@", FIG2), ("@@FIG3@@", FIG3),
                   ("@@FIGG@@", FIGG), ("@@FIGF@@", FIGF)):
    body = body.replace("<p>%s</p>" % token, fig).replace(token, fig)

def toc_row(n, sid, label):
    if n == "part":
        return '<li class="toc-part"><a href="#%s">%s</a></li>' % (sid, label)
    return '<li><a href="#%s"><span class="tocnum">%d</span>%s</a></li>' % (sid, n, label)
toc.append(("part", "sources", "Sources"))
toc_html = "\n".join(toc_row(*row) for row in toc)

# ---- citations: number in reading order, sort the source list to match ----
_body_part, _sep, _src_part = body.partition('<h3 class="tail" id="sources">')

order, seen = [], set()
for k in re.findall(r'class="ref" href="#r-([a-z0-9]+)"', _body_part):
    if k not in seen:
        seen.add(k); order.append(k)

entries = dict(re.findall(r'<li><span id="r-([a-z0-9]+)"></span>(.*?)</li>', _src_part, re.S))
missing = [k for k in order if k not in entries]
orphan = [k for k in entries if k not in seen]
if missing or orphan:
    raise SystemExit("citation mismatch. missing=%s orphan=%s" % (missing, orphan))

num = {k: i + 1 for i, k in enumerate(order)}
_body_part = re.sub(
    r'class="ref" href="#r-([a-z0-9]+)">\[[a-z0-9]+\]</a>',
    lambda m: 'class="ref" href="#r-%s">[%d]</a>' % (m.group(1), num[m.group(1)]),
    _body_part)

items = "\n".join('<li id="r-%s" value="%d">%s</li>' % (k, num[k], entries[k].strip())
                  for k in order)
_src_part = re.sub(r'<[ou]l>.*</[ou]l>', '<ol class="srclist">%s</ol>' % items, _src_part, flags=re.S)
body = _body_part + _sep + _src_part
print("citations numbered in reading order:", len(order))

_fig = {"n": 0}
def _renumber(m):
    _fig["n"] += 1
    return "<figcaption>Figure %d &middot;" % _fig["n"]
body = re.sub(r"<figcaption>Figure \d+ &middot;", _renumber, body)

CSS = open("style.css").read()

page = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DEK__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<style>
__CSS__
</style>
</head><body>
<header class="masthead">
  <a class="brand" href="#top">Unmitigated Risk</a>
  <span class="date">August 2026</span>
</header>

<main id="top">
  <div class="hero">
    <h1>__TITLE__</h1>
    <p class="dek">__DEK__</p>
  </div>

  __HERO__

  <nav class="toc" aria-label="Contents">
    <h2>Contents</h2>
    <ol>__TOC__</ol>
  </nav>

  <article class="prose">
__BODY__
  </article>
</main>

<footer class="foot">
  <p class="related">Companion piece, <a href="https://rmhrisk.github.io/continuous-assurance/">Why Continuous Assurance Did Not Happen Until Now</a>, on the same cost structure in assurance.</p>
  <p class="related">Related &middot; <a href="https://unmitigatedrisk.com/">Unmitigated Risk</a>, essays on PKI, privacy, and digital identity &middot; <a href="https://rmhrisk.github.io/classical-webpki/">A Deep Dive on the Classical WebPKI</a> &middot; <a href="https://rmhrisk.github.io/pq-webpki/">The Post-Quantum WebPKI</a> &middot; <a href="https://rmhrisk.github.io/containing-the-optimizer/">Containing the Optimizer</a> &middot; <a href="https://rmhrisk.github.io/assurance-model/">The Assurance Model Was Built for a World That No Longer Exists</a> &middot; <a href="https://rmhrisk.github.io/fips-140-3-corpus/">FIPS 140-3 Validation, in Practice</a></p>
</footer>
</body></html>
"""

page = (page.replace("__CSS__", CSS)
            .replace("__TITLE__", htmllib.escape(title))
            .replace("__DEK__", re.sub(r"<[^>]+>", "", markdown.markdown(dek)))
            .replace("__HERO__", HERO)
            .replace("__TOC__", toc_html)
            .replace("__BODY__", body))

open(OUT, "w").write(page)
print("wrote", OUT, len(page), "bytes;", counter["n"], "sections")
