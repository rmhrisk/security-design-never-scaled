"""Additional figures. Same visual grammar throughout:
accent stroke = a path that remains reachable; dashed grey = an eliminated or
unobservable edge; muted fill = machinery that is real but not the property."""

# ---- section 2: the boundary repeats -------------------------------------
FIGA = '''
<figure class="fig">
<svg viewBox="0 0 1060 320" role="img" aria-labelledby="fat">
  <title id="fat">Three cases in which a validated inner boundary leaves the consequential system outside it</title>
  <text class="s-eyebrow" x="20" y="24">THE SAME SHAPE, THREE TIMES</text>

  <g class="d-outer">
    <rect x="20" y="46" width="320" height="180" rx="4"/>
    <rect x="370" y="46" width="320" height="180" rx="4"/>
    <rect x="720" y="46" width="320" height="180" rx="4"/>
  </g>
  <g class="d-outerlabel">
    <text x="34" y="68">THE PRODUCT</text>
    <text x="384" y="68">THE WORKLOAD</text>
    <text x="734" y="68">THE AUTHORITY</text>
  </g>
  <g class="d-outertext">
    <text x="34" y="90">networking, update system, OS,</text><text x="34" y="106">administration, dependencies</text>
    <text x="384" y="90">the interfaces we deliberately</text><text x="384" y="106">exposed to the code inside</text>
    <text x="734" y="90">who may cause a signature,</text><text x="734" y="106">and whether that remains sound</text>
  </g>

  <g class="d-inner">
    <rect x="60" y="128" width="240" height="56" rx="3"/>
    <rect x="410" y="128" width="240" height="56" rx="3"/>
    <rect x="760" y="128" width="240" height="56" rx="3"/>
  </g>
  <g class="d-innertext">
    <text x="180" y="152" text-anchor="middle">FIPS 140-3 module</text>
    <text x="180" y="170" text-anchor="middle" class="sm">validated, approved mode</text>
    <text x="530" y="152" text-anchor="middle">Enclave or hypervisor</text>
    <text x="530" y="170" text-anchor="middle" class="sm">real property, one adversary</text>
    <text x="880" y="152" text-anchor="middle">Certificate path</text>
    <text x="880" y="170" text-anchor="middle" class="sm">every signature verifies</text>
  </g>

  <g class="d-miss">
    <path d="M180 200 v22"/><path d="M530 200 v22"/><path d="M880 200 v22"/>
    <path class="head" d="M180 234 l-7 -12 h14 z"/><path class="head" d="M530 234 l-7 -12 h14 z"/><path class="head" d="M880 234 l-7 -12 h14 z"/>
  </g>
  <g class="d-misslabel">
    <text x="180" y="256" text-anchor="middle">says nothing about the</text><text x="180" y="272" text-anchor="middle">box it sits in</text>
    <text x="530" y="256" text-anchor="middle">says nothing about what</text><text x="530" y="272" text-anchor="middle">the doors permit</text>
    <text x="880" y="256" text-anchor="middle">says nothing about who</text><text x="880" y="272" text-anchor="middle">should have been able to</text>
  </g>

  <text class="s-caption" x="530" y="306" text-anchor="middle">The inner box is correct in all three cases. The property lives in the outer one.</text>
</svg>
<figcaption>Figure 1 &middot; Validation, isolation, and cryptography each establish something real and each stop at a boundary drawn for their own convenience rather than for the risk.</figcaption>
</figure>
'''

# ---- section 4: the control cliff ----------------------------------------
FIGB = '''
<figure class="fig">
<svg viewBox="0 0 1060 430" role="img" aria-labelledby="fbt">
  <title id="fbt">A step function in which institutional credit stays at zero until the canonical control is reached</title>
  <text class="s-eyebrow" x="20" y="24">RISK REMOVED VERSUS CREDIT GIVEN</text>

  <g class="d-axis">
    <path d="M110 300 H1000"/><path d="M110 62 V300"/>
    <path d="M106 82 h8"/><path d="M106 300 h8"/>
  </g>
  <text class="d-axlabel" x="36" y="86">full</text>
  <text class="d-axlabel" x="30" y="304">none</text>
  <text class="d-axlabel rot" x="-180" y="26" transform="rotate(-90)">institutional credit</text>
  <text class="d-axlabel" x="555" y="410" text-anchor="middle">attack paths actually removed</text>

  <path class="d-line-b" d="M110 300 L330 234 L560 184 L780 140 L960 110"/>
  <text class="d-tag b" x="430" y="264">what the design actually buys</text>

  <path class="d-line-a" d="M110 300 H778 V82 H960"/>
  <text class="d-tag a" x="860" y="72">canonical control</text>

  <g class="d-marks">
    <circle cx="110" cy="300" r="6"/><circle cx="330" cy="300" r="6"/><circle cx="560" cy="300" r="6"/>
    <circle class="hit" cx="778" cy="82" r="7"/>
  </g>
  <g class="d-pt">
    <text x="110" y="324" text-anchor="middle">env var</text>
    <text x="330" y="324" text-anchor="middle">local signer</text>
    <text x="560" y="324" text-anchor="middle">separate host</text>
    <text x="778" y="324" text-anchor="middle">remote HSM</text>
  </g>

  <path class="d-zone" d="M110 344 v12 M770 344 v12 M110 350 H770"/>
  <text class="d-zone-t" x="440" y="382" text-anchor="middle">the dead zone: real paths removed, zero institutional value, so the work never gets funded</text>
</svg>
<figcaption>Figure 5 &middot; The rule encoded good knowledge. Because credit is a step function and risk reduction is not, a team that cannot afford the canonical control rationally does nothing at all.</figcaption>
</figure>
'''

# ---- section 5: the regress ----------------------------------------------
FIGC = '''
<figure class="fig">
<svg viewBox="0 0 1060 436" role="img" aria-labelledby="fct">
  <title id="fct">Each artifact answers the previous question and raises a new one</title>
  <text class="s-eyebrow" x="20" y="24">EVERY ANSWER IS ANOTHER ARTIFACT</text>

  <g class="d-stair">
    <path d="M40 62 H210 V104 H380 V146 H550 V188 H720 V230 H890 V272 H1040"/>
  </g>
  <g class="d-step">
    <text x="46" y="54">what is in it?</text>
    <text x="216" y="96">does it affect this product?</text>
    <text x="386" y="138">how do you know?</text>
    <text x="556" y="180">under which configuration?</text>
    <text x="726" y="222">is production really like that?</text>
    <text x="896" y="264">who can change it?</text>
  </g>
  <g class="d-artifact">
    <text x="46" y="80">SBOM</text>
    <text x="216" y="122">VEX</text>
    <text x="386" y="164">reachability</text>
    <text x="556" y="206">config evidence</text>
    <text x="726" y="248">attestation</text>
    <text x="896" y="290">identity graph</text>
  </g>

  <path class="d-cont" d="M1004 300 C 1034 322 980 336 940 336 H120"/>
  <path class="d-cont-h" d="M118 336 l13 -7 v14 z"/>
  <text class="d-cont-t" x="540" y="358" text-anchor="middle">and what if the identity provider is compromised, and is any of it still true today, and does reconciliation see all relevant state</text>

  <text class="s-caption" x="530" y="390" text-anchor="middle">Regressus ad infinitum</text>
  <text class="s-sub" x="530" y="414" text-anchor="middle">Each step is genuinely useful. None of them is the question anyone started with, and each is easier to fund than the judgment it stands in for.</text>
</svg>
<figcaption>Figure 4 &middot; Serialisation moved pieces of the knowledge around. It never abolished the judgment, and every increment was easier to institutionalise than the thing it replaced.</figcaption>
</figure>
'''

# ---- section 7: which cost function moves --------------------------------
FIGD = '''
<figure class="fig">
<svg viewBox="0 0 1060 400" role="img" aria-labelledby="fdt">
  <title id="fdt">The cost of adversarial search falls steeply while the cost of remediation stays flat</title>
  <text class="s-eyebrow" x="20" y="24">WHICH SIDE’S COST FUNCTION MOVES</text>

  <g class="d-axis">
    <path d="M110 320 H1000"/><path d="M110 56 V320"/>
  </g>
  <text class="d-axlabel rot" x="-200" y="26" transform="rotate(-90)">cost per unit of work</text>
  <text class="d-axlabel" x="555" y="356" text-anchor="middle">as machine reasoning gets cheaper</text>

  <path class="d-fill" d="M150 92 C 380 100 620 214 960 268 L960 96 C 620 96 380 94 150 92 Z"/>

  <path class="d-line-a flat" d="M150 96 H960"/>
  <text class="d-tag a" x="170" y="66">remediation</text>
  <text class="s-sub" x="170" y="82">API changes, customer migrations, reissued credentials, four teams, a year of dual support</text>

  <path class="d-line-b steep" d="M150 92 C 380 100 620 214 960 268"/>
  <text class="d-tag b" x="1000" y="296" text-anchor="end">adversarial path search</text>
  <text class="s-sub" x="1000" y="314" text-anchor="end">enumerate, compose, evaluate, discard, repeat</text>

  <path class="d-gap" d="M880 100 V262"/>
  <text class="d-gap-t" x="892" y="188">the gap</text>

  <text class="s-caption" x="530" y="378" text-anchor="middle">Search is almost pure reasoning, so it captures the saving immediately.</text>
  <text class="s-sub" x="530" y="398" text-anchor="middle">Coordination does not get cheaper because reasoning did.</text>
</svg>
<figcaption>Figure 6 &middot; The near-term effect of cheap reasoning is not a defensive renaissance. It is a widening gap, because only one side of the asymmetry is made of the thing that got cheaper.</figcaption>
</figure>
'''

# ---- section 8: the broken link in the pricing chain ----------------------
FIGE = '''
<figure class="fig">
<svg viewBox="0 0 1060 392" role="img" aria-labelledby="fet">
  <title id="fet">A pricing feedback chain with a broken link at the point where architecture would have to be observed</title>
  <text class="s-eyebrow" x="20" y="24">WHY THE MARKET DOES NOT CORRECT</text>

  <g class="s-node">
    <rect x="20"  y="66" width="150" height="58" rx="4"/>
    <rect x="210" y="66" width="150" height="58" rx="4"/>
    <rect x="400" y="66" width="150" height="58" rx="4"/>
    <rect x="700" y="66" width="150" height="58" rx="4"/>
    <rect x="890" y="66" width="150" height="58" rx="4"/>
  </g>
  <g class="s-nodetext">
    <text x="95"  y="90"  text-anchor="middle">cheaper</text><text x="95"  y="108" text-anchor="middle">search</text>
    <text x="285" y="90"  text-anchor="middle">real losses</text><text x="285" y="108" text-anchor="middle">change</text>
    <text x="475" y="90"  text-anchor="middle">claims</text><text x="475" y="108" text-anchor="middle">arrive</text>
    <text x="775" y="90"  text-anchor="middle">premiums</text><text x="775" y="108" text-anchor="middle">reprice</text>
    <text x="965" y="90"  text-anchor="middle">procurement</text><text x="965" y="108" text-anchor="middle">and vendors</text>
  </g>

  <g class="s-path">
    <path d="M170 95 H198"/><path d="M360 95 H388"/><path d="M850 95 H878"/>
    <g class="s-head">
      <path d="M192 89 l8 6 -8 6z"/><path d="M382 89 l8 6 -8 6z"/><path d="M872 89 l8 6 -8 6z"/>
    </g>
  </g>

  <path class="d-broken" d="M550 95 H700"/>
  <g class="d-x">
    <path d="M614 79 L640 111"/><path d="M640 79 L614 111"/>
  </g>

  <path class="d-drop" d="M625 124 V168"/>
  <g class="d-panel">
    <rect x="300" y="172" width="666" height="112" rx="4"/>
  </g>
  <text class="d-panel-h" x="322" y="196">TO PRICE THE DIFFERENCE, AN UNDERWRITER MUST OBSERVE IT</text>
  <g class="d-panel-t">
    <text x="322" y="222">MFA enabled, EDR deployed, backups tested</text>
    <text x="936" y="222" text-anchor="end" class="ok">observable, priced</text>
    <text x="322" y="252">workforce identity cannot reach signing authority</text>
    <text x="936" y="252" text-anchor="end" class="no">not observable, not priced</text>
  </g>
  <path class="d-panel-rule" d="M322 232 H944"/>

  <text class="s-caption" x="530" y="322" text-anchor="middle">The underwriter has the buyer’s problem, with more money riding on it.</text>
  <text class="s-sub" x="530" y="344" text-anchor="middle">Loss experience can say that something changed. It cannot say which architectural</text>
  <text class="s-sub" x="530" y="362" text-anchor="middle">feature to price, or verify it across a book of thousands.</text>
</svg>
<figcaption>Figure 7 &middot; The chain is slow at every link, but only one link is broken. That is why the correction waits on inspectability rather than on claims data.</figcaption>
</figure>
'''

# ---- section 10: the discontinuity ---------------------------------------
FIGF = '''
<figure class="fig">
<svg viewBox="0 0 1060 436" role="img" aria-labelledby="fft">
  <title id="fft">Five rungs of machine reasoning with a discontinuity before the last</title>
  <text class="s-eyebrow" x="20" y="24">THE RUNG THAT MATTERS IS THE LAST ONE</text>

  <g class="d-rung">
    <rect x="60" y="322" width="600" height="46" rx="3"/>
    <rect x="60" y="266" width="600" height="46" rx="3"/>
    <rect x="60" y="210" width="600" height="46" rx="3"/>
    <rect x="60" y="154" width="600" height="46" rx="3"/>
    <rect x="60" y="70"  width="600" height="46" rx="3" class="top"/>
  </g>
  <g class="d-rungtext">
    <text x="80" y="350">Local generation</text><text x="640" y="350" text-anchor="end" class="sm">nearby context</text>
    <text x="80" y="294">Task completion</text><text x="640" y="294" text-anchor="end" class="sm">by brute-force iteration</text>
    <text x="80" y="238">Model-based engineering</text><text x="640" y="238" text-anchor="end" class="sm">fewer loops, more model</text>
    <text x="80" y="182">Adversarial system reasoning</text><text x="640" y="182" text-anchor="end" class="sm">the object stops being code</text>
    <text x="80" y="98"  class="hi">Design optimisation</text><text x="640" y="98" text-anchor="end" class="sm hi">should it be shaped this way at all</text>
  </g>

  <path class="d-cut" d="M40 133 H1040"/>
  <text class="d-cut-t" x="44" y="122">iteration is unavailable above this line</text>

  <g class="d-brace">
    <path d="M690 70 h16 v46"/>
    <path d="M690 368 h16 V154"/>
  </g>
  <text class="d-side" x="720" y="94">changes what</text><text class="d-side" x="720" y="112">the machine is for</text>
  <text class="d-side muted" x="720" y="254">makes the existing</text><text class="d-side muted" x="720" y="272">machine faster</text>

  <text class="s-sub" x="530" y="398" text-anchor="middle">You cannot reach a trust-boundary decision by trying it in production and watching it fail.</text>
  <text class="s-sub" x="530" y="416" text-anchor="middle">Competence that comes from the model, rather than from the loop, is the thing to watch.</text>
</svg>
<figcaption>Figure 9 &middot; The informative axis is method rather than size. A system that only gets there by iterating never reaches the top rung, because the top rung is the one where you do not get to iterate.</figcaption>
</figure>
'''

# ---- section 10: gross generation versus net shipped ---------------------
FIGG = '''
<figure class="fig">
<svg viewBox="0 0 1060 400" role="img" aria-labelledby="fgt">
  <title id="fgt">Gross generated code rising steeply while net shipped code rises modestly</title>
  <text class="s-eyebrow" x="20" y="24">WHAT GOT CHEAP, AND WHAT DID NOT</text>

  <g class="d-axis">
    <path d="M110 320 H1000"/><path d="M110 56 V320"/>
  </g>
  <text class="d-axlabel rot" x="-250" y="26" transform="rotate(-90)">relative production capacity</text>
  <text class="d-axlabel" x="150" y="348">before assistants</text>
  <text class="d-axlabel" x="960" y="348" text-anchor="end">now</text>

  <path class="d-fill" d="M150 296 C 420 288 700 190 960 84 L960 258 C 700 282 420 292 150 296 Z"/>

  <path class="d-line-b steep" d="M150 296 C 420 288 700 190 960 84"/>
  <text class="d-tag a" x="640" y="112">implementation generated</text>

  <path class="d-line-a flat" d="M150 296 C 420 292 700 282 960 258"/>
  <text class="d-tag b" x="640" y="286">integrated production change</text>

  <path class="d-gap" d="M905 96 V264"/>
  <text class="d-gap-t" x="895" y="200" text-anchor="end">review, integration, debugging,</text>
  <text class="d-gap-t" x="895" y="216" text-anchor="end">testing, and deciding whether</text>
  <text class="d-gap-t" x="895" y="232" text-anchor="end">it should exist at all</text>

  <text class="s-caption" x="530" y="382" text-anchor="middle">The gap is the judgment. It did not get cheaper when typing did.</text>
</svg>
<figcaption>Figure 8 &middot; Shape rather than measurement. There is no reliable published figure for either curve; what is not in dispute is that they diverged, and that only one of them was ever the constraint.</figcaption>
</figure>
'''

# ---- section 1: the anatomy of a compression -----------------------------
FIGH = '''
<figure class="fig">
<svg viewBox="0 0 1060 400" role="img" aria-labelledby="fht">
  <title id="fht">Expert threat reasoning compressed into a portable rule, with the justification discarded</title>
  <text class="s-eyebrow" x="20" y="24">WHAT COMPRESSION KEEPS, AND WHAT IT DROPS</text>

  <g class="c-src"><rect x="20" y="52" width="330" height="212" rx="4"/></g>
  <text class="c-head" x="38" y="76">EXPERT THREAT REASONING</text>
  <g class="c-item">
    <text x="38" y="108">the adversaries assumed</text>
    <text x="38" y="138">the consequences weighed</text>
    <text x="38" y="168">the alternatives compared</text>
    <text x="38" y="198">the cost judged acceptable</text>
    <text x="38" y="228">the conditions under which it holds</text>
  </g>

  <g class="c-keep">
    <path d="M356 112 H514"/><path class="head" d="M524 112 l-13 -7 v14 z"/>
    <text x="435" y="100" text-anchor="middle">compresses to</text>
  </g>
  <g class="c-rule"><rect x="534" y="84" width="330" height="56" rx="4"/></g>
  <text class="c-ruletext" x="699" y="118" text-anchor="middle">Keys belong in HSMs</text>
  <text class="c-good" x="884" y="106">portable, teachable,</text>
  <text class="c-good" x="884" y="124">auditable, enforceable</text>
  <text class="s-sub" x="534" y="164">This is not a mistake. It is how a discipline scales past its experts.</text>

  <g class="c-drop">
    <path d="M356 224 C 430 224 452 266 508 274"/><path class="head" d="M522 276 l-14 -5 -1 14 z"/>
    <text x="404" y="292" text-anchor="middle">discards</text>
  </g>
  <g class="c-dropbox"><rect x="534" y="238" width="490" height="86" rx="4"/></g>
  <text class="c-drophead" x="552" y="262">WHAT FALLS OUT</text>
  <g class="c-dropitem">
    <text x="552" y="288">the threat model that justified the rule</text>
    <text x="552" y="312">the means of knowing when it stops applying</text>
  </g>

  <text class="s-caption" x="530" y="368" text-anchor="middle">Everything downstream in this essay follows from the second line.</text>
</svg>
<figcaption>Figure 1 &middot; The rule is the useful residue. The reasoning that produced it is not carried along with it, which is why the rule cannot tell you when it has stopped being the right answer.</figcaption>
</figure>
'''

# ---- section 3: the legibility plane -------------------------------------
FIGI = '''
<figure class="fig">
<svg viewBox="0 0 1060 430" role="img" aria-labelledby="fit">
  <title id="fit">Security claims plotted by how much they tell you against how easily a buyer can check them</title>
  <text class="s-eyebrow" x="20" y="24">WHY THE MARKET CLEARS WHERE IT DOES</text>

  <rect class="p-zone" x="130" y="66" width="380" height="164"/>
  <rect class="p-zone want" x="620" y="228" width="370" height="118"/>

  <g class="d-axis"><path d="M120 350 H1000"/><path d="M120 60 V350"/></g>
  <text class="d-axlabel rot" x="-300" y="26" transform="rotate(-90)">how easily a buyer can check it</text>
  <text class="d-axlabel" x="560" y="392" text-anchor="middle">how much it tells you about actual security</text>

  <g class="p-pt">
    <circle cx="196" cy="104" r="6"/><text x="210" y="108">FIPS validated</text>
    <circle cx="252" cy="146" r="6"/><text x="266" y="150">MFA at 98%</text>
    <circle cx="188" cy="188" r="6"/><text x="202" y="192">SOC 2 unqualified</text>
    <circle cx="300" cy="220" r="6"/><text x="314" y="224">SBOM current</text>
  </g>
  <text class="p-zonelabel" x="140" y="88">WHAT THE MARKET TRANSACTS IN</text>

  <g class="p-pt want">
    <circle cx="880" cy="296" r="8"/>
  </g>
  <text class="p-want" x="636" y="256">&#8220;Compromise of the workforce identity</text>
  <text class="p-want" x="636" y="274">provider does not reach signing authority.&#8221;</text>
  <text class="p-zonelabel want" x="636" y="338">HIGH INFORMATION, ALMOST UNCHECKABLE</text>

  <path class="p-arrow" d="M856 314 C 720 324 540 292 348 252"/>
  <text class="p-arrowlabel" x="760" y="214" text-anchor="middle">verifying it needs the expertise they were trying to buy</text>

  <text class="s-caption" x="560" y="416" text-anchor="middle">Nobody has to be dishonest. The observable claim wins because it is observable.</text>
</svg>
<figcaption>Figure 3 &middot; Clarke&#8217;s corollary drawn out. The upper left is legible and nearly contentless; the lower right carries the information a buyer actually wants and cannot be checked without the expertise they lack.</figcaption>
</figure>
'''

# ---- section 4: the half-life of a rule ----------------------------------
FIGJ = '''
<figure class="fig">
<svg viewBox="0 0 1060 340" role="img" aria-labelledby="fjt">
  <title id="fjt">Timeline of the shoe removal rule from the 2001 incident to its 2025 retirement</title>
  <text class="s-eyebrow" x="20" y="24">HOW LONG A COMPRESSION LASTS</text>

  <g class="t-band"><rect x="216" y="80" width="560" height="34" rx="3"/></g>
  <text class="t-bandtext" x="236" y="102">shoe removal universal, nineteen years</text>

  <g class="t-exempt"><rect x="120" y="124" width="656" height="24" rx="3"/></g>
  <text class="t-exempttext" x="140" y="141">PreCheck members exempt throughout</text>

  <g class="d-axis"><path d="M110 178 H1010"/></g>
  <g class="t-tick">
    <path d="M120 172 v12"/><path d="M216 172 v12"/><path d="M776 172 v12"/><path d="M980 172 v12"/>
  </g>
  <g class="t-year">
    <text x="120" y="202" text-anchor="middle">2001</text>
    <text x="216" y="202" text-anchor="middle">2006</text>
    <text x="776" y="202" text-anchor="middle">2025</text>
    <text x="980" y="202" text-anchor="middle">2040?</text>
  </g>
  <g class="t-note">
    <text x="120" y="66" text-anchor="middle">Reid attempt</text>
    <text x="776" y="66" text-anchor="end">retired because scanners improved,</text>
    <text x="776" y="50" text-anchor="end">not because anyone reopened the question</text>
  </g>

  <g class="t-open"><rect x="240" y="224" width="740" height="30" rx="3"/></g>
  <text class="t-opentext" x="260" y="244">liquids rule, adopted 2006, still in force; equipment replacement described as possibly running to 2040</text>

  <text class="s-caption" x="530" y="300" text-anchor="middle">The rule was defensible in 2002. Nothing about it was re-examined for nineteen years.</text>
</svg>
<figcaption>Figure 4 &middot; The exemption band is the tell. A control that a paying traveller could opt out of for its entire life was not the thing holding the risk down.</figcaption>
</figure>
'''

# ---- worked example: one CVE, two architectures --------------------------
FIGK = '''
<figure class="fig">
<svg viewBox="0 0 1060 490" role="img" aria-labelledby="fkt">
  <title id="fkt">Heartbleed reaching every secret in a monolith and only session state in a separated design</title>
  <text class="s-eyebrow" x="20" y="24">HEARTBLEED, TWO SHAPES</text>
  <text class="s-eyebrow accent" x="1040" y="24" text-anchor="end">IDENTICAL SBOM, CVE, AND BASE SCORE</text>

  <text class="w-head" x="20" y="60">MONOLITH &#183; one process, one uid, one heap</text>
  <g class="w-box"><rect x="20" y="76" width="440" height="150" rx="4" class="hot"/></g>
  <g class="w-inner">
    <rect x="40" y="100" width="180" height="42" rx="3"/><rect x="240" y="100" width="200" height="42" rx="3"/>
    <rect x="40" y="158" width="180" height="42" rx="3"/><rect x="240" y="158" width="200" height="42" rx="3"/>
  </g>
  <g class="w-text">
    <text x="130" y="126" text-anchor="middle">TLS heartbeat</text>
    <text x="340" y="126" text-anchor="middle">host private key</text>
    <text x="130" y="184" text-anchor="middle">session state</text>
    <text x="340" y="184" text-anchor="middle">database credential</text>
  </g>
  <text class="w-verdict" x="20" y="246">The over-read returns whatever is next to it.</text>
  <text class="w-verdict" x="20" y="266">All of this is next to it.</text>

  <text class="w-head" x="600" y="60">SEPARATED &#183; four uids, authenticated local IPC</text>
  <g class="w-box">
    <rect x="600" y="76" width="200" height="60" rx="4" class="hot"/>
    <rect x="840" y="76" width="200" height="60" rx="4"/>
    <rect x="600" y="156" width="200" height="60" rx="4"/>
    <rect x="840" y="156" width="200" height="60" rx="4"/>
  </g>
  <g class="w-text">
    <text x="700" y="101" text-anchor="middle" class="hot">netd</text><text x="700" y="120" text-anchor="middle" class="sm">TLS, session state only</text>
    <text x="940" y="101" text-anchor="middle">authd</text><text x="940" y="120" text-anchor="middle" class="sm">host key, sign() only</text>
    <text x="700" y="181" text-anchor="middle">appd</text><text x="700" y="200" text-anchor="middle" class="sm">logic, db credential</text>
    <text x="940" y="181" text-anchor="middle">logd</text><text x="940" y="200" text-anchor="middle" class="sm">append only</text>
  </g>
  <g class="w-link">
    <path d="M800 106 H836"/><path d="M700 140 V152"/><path d="M800 186 H836"/>
  </g>
  <text class="w-verdict" x="600" y="246">A read cannot cross an address space.</text>
  <text class="w-verdict" x="600" y="266">Only netd&#8217;s own heap is next to it.</text>

  <path class="s-rule" d="M20 292 H1040"/>
  <text class="w-colhead" x="20" y="318">WHAT THE OVER-READ RETURNS</text>
  <g class="w-cmp">
    <text x="20" y="348">host private key</text><text x="330" y="348" class="yes">recovered in practice, 2014</text><text x="680" y="348" class="no">different address space</text>
    <text x="20" y="376">database credential</text><text x="330" y="376" class="yes">on the same heap</text><text x="680" y="376" class="no">different address space</text>
    <text x="20" y="404">other users&#8217; in-flight plaintext</text><text x="330" y="404" class="yes">disclosed</text><text x="680" y="404" class="yes">disclosed</text>
    <text x="20" y="432">everything else the service held</text><text x="330" y="432" class="yes">disclosed</text><text x="680" y="432" class="no">nothing else is there</text>
  </g>
  <text class="s-sub" x="20" y="466">The third row is the honest one. Separation decided which secrets were in the room. It did not stop the bug.</text>
</svg>
<figcaption>Figure 3 &middot; Same library, same disclosure, same patch deadline, same scanner output, same audit result. One of these systems reissues its identity and the other does not, and no instrument in the pipeline can tell them apart beforehand.</figcaption>
</figure>
'''
