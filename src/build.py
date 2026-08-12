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
<figcaption>The reductio. You can satisfy every requirement in the right-hand column and still leave a four-step route from an internet-facing system to the authority that ends the company.</figcaption>
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

# Title + description live in YAML front matter.
_fm = re.match(r"^---\n(.*?)\n---\n", md, re.S)
if not _fm:
    raise SystemExit("front matter not found")
_fmtext = _fm.group(1)
title = re.search(r"^title:\s*(.+)$", _fmtext, re.M).group(1).strip()
dek = re.search(r"^description:\s*(.+)$", _fmtext, re.M).group(1).strip()
body_md = md[_fm.end():].lstrip("\n")

# Figures are placed by explicit @@FIGnn@@ tokens in the markdown.

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
    1: ("I", "The cache", "Why we compressed design into controls, and the two things the compression drops."),
    3: ("II", "The regress", "How the missing model turns into ever more machinery instead of the judgment that joins it."),
    4: ("III", "The turn", "What cheap reasoning changes, and the representation it finally makes affordable."),
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
body = body.replace("<h3>What this post does not establish</h3>",
    '<h3 class="tail" id="limits">What this post does not establish</h3>')
body = body.replace("<h3>Sources</h3>", '<h3 class="tail" id="sources">Sources</h3>')

FIGSD = '''
<figure class="fig">
<svg viewBox="0 0 1060 400" role="img" aria-labelledby="fsdt">
  <title id="fsdt">Two problems side by side: searching a bounded defect space with an oracle, and drawing a boundary that bounds what a compromise reaches</title>

  <line x1="525" y1="40" x2="525" y2="362" stroke="var(--rule)" stroke-width="1.25"/>

  <text class="s-panelhead" x="20" y="26">WHERE A CRASH CAN SETTLE IT</text>
  <text class="s-eyebrow accent" x="20" y="44">SPACE EXHAUSTION</text>

  <rect x="48" y="82" width="150" height="118" fill="var(--accent)" opacity=".07"/>
  <g class="s-cell">
    <circle class="off" cx="70"  cy="100" r="5"/><circle class="off" cx="120" cy="100" r="5"/><circle class="off" cx="170" cy="100" r="5"/><circle class="off" cx="220" cy="100" r="5"/><circle class="off" cx="270" cy="100" r="5"/><circle class="off" cx="320" cy="100" r="5"/>
    <circle class="off" cx="70"  cy="140" r="5"/><circle class="off" cx="120" cy="140" r="5"/><circle class="on"  cx="170" cy="140" r="5"/><circle class="off" cx="220" cy="140" r="5"/><circle class="off" cx="270" cy="140" r="5"/><circle class="off" cx="320" cy="140" r="5"/>
    <circle class="off" cx="70"  cy="180" r="5"/><circle class="on"  cx="120" cy="180" r="5"/><circle class="off" cx="170" cy="180" r="5"/><circle class="off" cx="220" cy="180" r="5"/><circle class="off" cx="270" cy="180" r="5"/><circle class="off" cx="320" cy="180" r="5"/>
  </g>
  <g class="s-owner"><text x="123" y="216" text-anchor="middle">the defect space</text></g>

  <line x1="345" y1="140" x2="384" y2="140" stroke="var(--ink-soft)" stroke-width="1.5"/>
  <g class="s-node"><rect x="386" y="118" width="96" height="44" rx="4"/></g>
  <g class="s-nodetext"><text x="434" y="145" text-anchor="middle">ORACLE</text></g>
  <text class="s-sub" x="434" y="182" text-anchor="middle">a crash confirms a hit</text>

  <text class="s-sub" x="250" y="300" text-anchor="middle">A bounded space, a checkable oracle.</text>
  <g class="s-legend"><text x="20" y="352">fuzzers, XBOW, AIxCC</text></g>

  <text class="s-panelhead" x="560" y="26">WHERE ONLY INTENT CAN</text>
  <text class="s-eyebrow accent" x="560" y="44">JUDGMENT ABOUT SHAPE</text>

  <rect x="586" y="98" width="150" height="104" rx="6" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text class="s-sub" x="661" y="88" text-anchor="middle" style="fill:var(--accent)">a boundary the design draws</text>

  <line x1="620" y1="150" x2="694" y2="122" stroke="var(--accent)" stroke-width="1.75"/>
  <line x1="620" y1="150" x2="694" y2="180" stroke="var(--accent)" stroke-width="1.75"/>
  <line x1="700" y1="122" x2="792" y2="122" stroke="var(--removed)" stroke-width="1.5" stroke-dasharray="4 4"/>
  <line x1="700" y1="180" x2="792" y2="180" stroke="var(--removed)" stroke-width="1.5" stroke-dasharray="4 4"/>
  <line x1="806" y1="128" x2="862" y2="146" stroke="var(--removed)" stroke-width="1.5"/>
  <line x1="806" y1="176" x2="862" y2="156" stroke="var(--removed)" stroke-width="1.5"/>

  <circle cx="694" cy="122" r="12" fill="var(--accent)" opacity=".18" stroke="var(--accent)" stroke-width="1.5"/>
  <circle cx="694" cy="180" r="12" fill="var(--accent)" opacity=".18" stroke="var(--accent)" stroke-width="1.5"/>
  <circle cx="800" cy="122" r="12" fill="var(--paper)" stroke="var(--removed)" stroke-width="1.5"/>
  <circle cx="800" cy="180" r="12" fill="var(--paper)" stroke="var(--removed)" stroke-width="1.5"/>
  <circle cx="872" cy="151" r="12" fill="var(--paper)" stroke="var(--removed)" stroke-width="1.5"/>
  <circle cx="620" cy="150" r="18" fill="var(--accent)"/>
  <text x="620" y="154" text-anchor="middle" style="font-family:var(--sans);font-size:11px;fill:#fff">taken</text>

  <text class="s-sub" x="661" y="230" text-anchor="middle">what it can reach</text>
  <text class="s-sub" x="836" y="230" text-anchor="middle" style="fill:var(--removed)">beyond the boundary</text>

  <text class="s-sub" x="800" y="300" text-anchor="middle">No space, no oracle. What should the taken part reach?</text>
  <g class="s-legend"><text x="560" y="352">the design decision</text></g>
</svg>
<figcaption>Figure 1 &middot; Two different problems. On the left, when a problem has a bounded space and a crash says when you have won, machines are extraordinary at it. On the right there is no external oracle at all, only a judgment about what a compromise should be allowed to reach, and that judgment is what sets how far the inevitable bug gets.</figcaption>
</figure>
'''

FIGLAYER = '''
<figure class="fig">
<svg viewBox="0 0 1060 430" role="img" aria-labelledby="flyt">
  <title id="flyt">The same design move at three layers: a boundary that decides what a compromise can reach, in code, in the platform, and in the application model</title>

  <text class="s-eyebrow" x="24" y="26">THE SAME MOVE AT EVERY LAYER</text>
  <text class="s-eyebrow accent" x="760" y="30" text-anchor="middle">WHAT IT CANNOT REACH</text>
  <text class="s-sub" x="545" y="70" text-anchor="middle" style="fill:var(--muted)">a boundary the design draws</text>

  <line x1="545" y1="86" x2="545" y2="404" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="5 4"/>

  <text class="s-panelhead" x="24" y="112">IN CODE</text>
  <text class="s-sub" x="24" y="130" style="fill:var(--muted)">processes</text>
  <line x1="326" y1="120" x2="512" y2="120" stroke="var(--accent)" stroke-width="1.75"/>
  <path d="M512 114 l10 6 -10 6z" fill="var(--accent)"/>
  <circle cx="310" cy="120" r="15" fill="var(--accent)"/>
  <text x="310" y="124" text-anchor="middle" style="font-family:var(--sans);font-size:10px;fill:#fff">taken</text>
  <circle cx="760" cy="120" r="15" fill="var(--paper)" stroke="var(--removed)" stroke-width="1.5"/>
  <text class="s-sub" x="760" y="154" text-anchor="middle">host key</text>

  <text class="s-panelhead" x="24" y="232">IN THE PLATFORM</text>
  <text class="s-sub" x="24" y="250" style="fill:var(--muted)">Borg, Kubernetes</text>
  <line x1="326" y1="240" x2="512" y2="240" stroke="var(--accent)" stroke-width="1.75"/>
  <path d="M512 234 l10 6 -10 6z" fill="var(--accent)"/>
  <circle cx="310" cy="240" r="15" fill="var(--accent)"/>
  <text x="310" y="244" text-anchor="middle" style="font-family:var(--sans);font-size:10px;fill:#fff">taken</text>
  <circle cx="760" cy="240" r="15" fill="var(--paper)" stroke="var(--removed)" stroke-width="1.5"/>
  <text class="s-sub" x="760" y="274" text-anchor="middle">other services</text>

  <text class="s-panelhead" x="24" y="352">IN THE APP</text>
  <text class="s-sub" x="24" y="370" style="fill:var(--muted)">iOS sandbox</text>
  <line x1="326" y1="360" x2="512" y2="360" stroke="var(--accent)" stroke-width="1.75"/>
  <path d="M512 354 l10 6 -10 6z" fill="var(--accent)"/>
  <circle cx="310" cy="360" r="15" fill="var(--accent)"/>
  <text x="310" y="364" text-anchor="middle" style="font-family:var(--sans);font-size:10px;fill:#fff">taken</text>
  <circle cx="760" cy="360" r="15" fill="var(--paper)" stroke="var(--removed)" stroke-width="1.5"/>
  <text class="s-sub" x="760" y="394" text-anchor="middle">other apps' data</text>
</svg>
<figcaption>Figure 1 &middot; The same move at three layers. A boundary decides what a compromise reaches, whether it is drawn between processes, between services on a platform, or between apps on a device. A substrate can make that boundary the default, so the contained shape is the one developers get for free.</figcaption>
</figure>
'''

for token, fig in (("@@FIG01@@", FIGK), ("@@FIG11@@", FIGLAYER), ("@@FIG02@@", FIGH), ("@@FIG03@@", FIGA),
                   ("@@FIG04@@", FIG1), ("@@FIG05@@", FIGC),
                   ("@@FIG07@@", FIGF), ("@@FIG10@@", FIGSD),
                   ("@@FIG08@@", FIG2), ("@@FIG09@@", FIG3)):
    body = body.replace("<p>%s</p>" % token, fig).replace(token, fig)

def toc_row(n, sid, label):
    if n == "part":
        return '<li class="toc-part"><a href="#%s">%s</a></li>' % (sid, label)
    return '<li><a href="#%s"><span class="tocnum">%d</span>%s</a></li>' % (sid, n, label)
toc.append(("part", "sources", "Sources"))
toc.append(("part", "quiz", "✓ Check your understanding"))
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
    <ol>
__TOC__
    </ol>
  </nav>

  <article class="prose">
__BODY__
  </article>

  <div class="quiz" id="quiz">
    <h3 class="tail">&#10003; Check your understanding</h3>
    <p class="qintro">Ten questions on controls, composition, and what cheap reasoning changes. Options shuffle every run.</p>
    <div id="qbox"><button class="qbtn" id="qstart">Start the quiz</button></div>
  </div>
</main>

<footer class="foot">
  <p class="related">Companion piece, <a href="https://rmhrisk.github.io/continuous-assurance/">Why Continuous Assurance Did Not Happen Until Now</a>, on the same cost structure in assurance.</p>
  <p class="related">Related &middot; <a href="https://unmitigatedrisk.com/">Unmitigated Risk</a>, essays on PKI, privacy, and digital identity &middot; <a href="https://rmhrisk.github.io/classical-webpki/">A Deep Dive on the Classical WebPKI</a> &middot; <a href="https://rmhrisk.github.io/pq-webpki/">The Post-Quantum WebPKI</a> &middot; <a href="https://rmhrisk.github.io/containing-the-optimizer/">Containing the Optimizer</a> &middot; <a href="https://rmhrisk.github.io/assurance-model/">The Assurance Model Was Built for a World That No Longer Exists</a> &middot; <a href="https://rmhrisk.github.io/fips-140-3-corpus/">FIPS 140-3 Validation, in Practice</a></p>
</footer>

<script>
const QUESTIONS = [
  { q: "Two services link the same OpenSSL and both are hit by Heartbleed. What decides whether one loses its private key and the other does not?",
    a: "How the system was arranged around the controls, which secrets shared the address space",
    w: ["The CVSS base score of the vulnerability", "Whether the SBOM was current", "Which team patched faster"],
    e: "Same library, same CVE, same deadline. The residual is set by the architecture, not by any instrument in the pipeline." },
  { q: "In this essay, what is a security control?",
    a: "A cached answer to a security-design question, with the reasoning that produced it discarded",
    w: ["A guarantee that a property holds", "A test an auditor performs on a schedule", "A product a vendor sells"],
    e: "We scaled security by distributing the answers and dropping the threat model and context behind them." },
  { q: "What two things does the compression drop every time?",
    a: "The threat model that justified the control, and the condition under which it stops applying",
    w: ["The vendor name and the price", "The owner and the audit deadline", "The SBOM and the CVE record"],
    e: "Those two are exactly what you need to know whether a control is still doing its job in this deployment." },
  { q: "Why can choosing a FIPS-validated module leave you slower to fix a disclosed vulnerability?",
    a: "The compliance certificate pins a specific version, so a fix ships code that is no longer the validated version until it is reassessed",
    w: ["Validated modules simply contain more bugs", "FIPS forbids patching altogether", "The module can never be changed once shipped"],
    e: "Of 415 validated modules read from the public record, 324 had no recorded update after initial validation." },
  { q: "Encryption at rest passes every check, yet an over-privileged service account still walks off with the data. Why?",
    a: "Its threat model is physical, so against a caller holding valid credentials it is not defeated, it is simply not present",
    w: ["It was implemented incorrectly", "The encryption key was too short", "The auditor forgot to test it"],
    e: "The control removes none of the paths that actually take the data, while still satisfying the questionnaire." },
  { q: "Why does a path like service to identity to CI to deploy to production to signing survive so much spending?",
    a: "Every edge is somebody's intended behaviour and no single team owns the composition",
    w: ["Each edge is an obvious misconfiguration", "The path violates a named, audited control", "It only works on unpatched systems"],
    e: "Defense follows reporting lines, so a path crossing four teams sits on none of their backlogs." },
  { q: "Why does the machinery keep growing, from SBOM to VEX to reachability to runtime attestation and on?",
    a: "Each artifact serializes another piece of the missing model without recovering the judgment that joins the pieces",
    w: ["Vendors are being dishonest", "Regulation mandates every one of them", "The individual tools do not work"],
    e: "Every increment can be justified on its own terms, which is exactly why the regress can continue indefinitely." },
  { q: "Why does cheap machine reasoning help attackers before it helps defenders?",
    a: "Attacking is almost all reasoning over a representation, while defending is mostly changing systems, which stays slow",
    w: ["Attackers simply have better models", "Defenders are not permitted to use the models", "The models can only write exploits"],
    e: "Searching a system gets cheaper before changing one does, even if model capability froze today." },
  { q: "On the reasoning ladder, which rung changes what the machine is for rather than just making it faster?",
    a: "Architecture, asking why the system needs the long-lived authority at all",
    w: ["Retrieving the relevant rule", "Analysing the current configuration in context", "Generating findings more quickly"],
    e: "Everything below the top rung makes the existing machine faster; only the top rung changes its purpose." },
  { q: "What keeps the proposed design representation from becoming the next SBOM?",
    a: "It is built to be attacked, not certified, and asks for the shortest path that proves the current belief wrong",
    w: ["A coverage percentage and an audit test for currency", "A procurement mandate behind it", "A dashboard that turns green"],
    e: "A representation optimised to be attacked resists institutionalisation in a way one optimised to be certified does not." },
];

function shuffle(arr) { for (let i = arr.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [arr[i], arr[j]] = [arr[j], arr[i]]; } return arr; }

const qbox = document.getElementById("qbox");
let idx = 0, score = 0, deck = [], selected = -1, revealed = false;

function startQuiz() {
  idx = 0; score = 0;
  deck = QUESTIONS.map(item => ({
    q: item.q, e: item.e,
    opts: shuffle([{ t: item.a, ok: true }, ...item.w.map(t => ({ t, ok: false }))]),
  }));
  renderQuestion();
}

function renderQuestion() {
  selected = -1; revealed = false;
  const item = deck[idx];
  qbox.innerHTML = "<div class='q-progress'>Question " + (idx + 1) + " of " + deck.length +
    " &middot; Score " + score + "</div>" +
    "<div class='q-question'>" + item.q + "</div>" +
    item.opts.map((o, j) => "<button class='q-opt' data-j='" + j + "'>" + o.t + "</button>").join("") +
    "<div class='q-explain' id='qexp' style='display:none'></div>" +
    "<button class='qbtn' id='qact' disabled>Check answer</button>";
  qbox.querySelectorAll(".q-opt").forEach(btn => btn.addEventListener("click", () => select(parseInt(btn.dataset.j))));
  document.getElementById("qact").addEventListener("click", reveal);
}

function select(j) {
  if (revealed) return;
  selected = j;
  qbox.querySelectorAll(".q-opt").forEach((btn, k) => btn.classList.toggle("sel", k === j));
  document.getElementById("qact").disabled = false;
}

function reveal() {
  if (revealed || selected < 0) return;
  revealed = true;
  const item = deck[idx];
  qbox.querySelectorAll(".q-opt").forEach((btn, k) => {
    btn.disabled = true; btn.classList.remove("sel");
    if (item.opts[k].ok) btn.classList.add("correct");
    else if (k === selected) btn.classList.add("wrong");
  });
  if (item.opts[selected].ok) score++;
  const exp = document.getElementById("qexp");
  exp.textContent = item.e;
  exp.style.display = "block";
  qbox.querySelector(".q-progress").innerHTML = "Question " + (idx + 1) + " of " + deck.length + " &middot; Score " + score;
  const act = document.getElementById("qact");
  act.textContent = idx + 1 < deck.length ? "Next question" : "See results";
  const fresh = act.cloneNode(true);
  act.replaceWith(fresh);
  fresh.addEventListener("click", () => { idx++; idx < deck.length ? renderQuestion() : renderResults(); });
}

function renderResults() {
  let verdict;
  if (score >= 9) verdict = "You can see the architecture the instruments cannot.";
  else if (score >= 7) verdict = "Solid. You are reasoning about shape, not controls.";
  else if (score >= 4) verdict = "The thesis is there. Walk the path once more.";
  else verdict = "Start again from two services and one bug.";
  qbox.innerHTML = "<div class='q-progress'>Results</div>" +
    "<div class='q-score'>" + score + " of " + deck.length + "</div>" +
    "<div class='q-verdict'>" + verdict + "</div>" +
    "<button class='qbtn' id='qagain'>Try again</button>";
  document.getElementById("qagain").addEventListener("click", startQuiz);
}

document.getElementById("qstart").addEventListener("click", startQuiz);
</script>
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
