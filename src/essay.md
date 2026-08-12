# Security Design Never Scaled

### We could not afford the judgment, so we compressed it into rules, controls, and artifacts. Attackers never had to respect the compression. Cheap machine reasoning will make that mismatch more expensive first. Whether it ever fixes the cause is the open question.

::: lede
Security has a habit of mistaking the mechanism for the property.
:::

There is a key, so put it in an HSM. There is third-party software, so demand an SBOM. There is source code, so scan it. There are users, so require MFA. Each of those can be exactly the right thing to do. None of them means the system is secure.

**Security controls are cached answers to security-design questions. We scaled security by distributing the answers and discarding the reasoning that produced them.** Everything else here follows from that.

We have known this for fifty years. Saltzer and Schroeder were writing about least privilege, complete mediation, and unwanted access paths in the 1970s<a class="ref" href="#r-saltzer">[saltzer]</a>. NIST today explicitly treats security as an emergent property of a system, and systems security engineering as a discipline within systems engineering<a class="ref" href="#r-nist160">[nist160]</a>. The problem was never that we forgot security design.

The problem is that security design never scaled, and what we built in its place has been standing in for it ever since.

::: aside
This post is the security-design counterpart to [Why Continuous Assurance Did Not Happen Until Now](https://rmhrisk.github.io/continuous-assurance/). That post argued that three decades of compliance software cut the administrative cost of assurance and never touched the cognitive cost, which is why the periodic model survived everything that was supposed to replace it. The same cost structure produced the security industry, and it produced a sharper failure, because the thing security was substituting for was never a report. It was the design.

Written August 2026. Part of the argument rests on where machine reasoning goes next, which is exactly the kind of claim that ages badly. Treat the capability discussion as a snapshot rather than a current-state reference; the economics should outlast the specifics.
:::

## What we could not afford

Start with the work itself. Understand what the system is trying to accomplish. Understand who and what holds authority. Identify the assumptions the design depends on. Work backward from unacceptable consequences. Trace what becomes possible when an identity, component, or trust boundary fails. Notice when two individually reasonable decisions compose into a dangerous path. Compare alternative architectures. Decide which risks to eliminate, which to contain, which to detect, which to recover from, and which to accept or transfer.

That is contextual reasoning, and every part of it is expensive. It requires holding a whole system in one head, keeping it there as the system changes, and being in the room when the consequential decisions get made. A principal security architect cannot hold five thousand engineers' systems at once. A red team cannot continuously search every new authority path. A threat model does not stay current by itself.

It is worth being precise about why this particular work resisted the automation that arrived for everything around it, because the reason is not that nobody tried.

Design reasoning is non-local. You cannot decide whether an authority relationship is acceptable by examining that relationship, because whether it matters depends on parts of the system you are not looking at. A scanner works when the property it is hunting can be recognised inside a bounded window of the artifact, which is true of a great many defects and false of nearly every design question. Plenty of serious vulnerabilities are compositional too; the difference is that a design question is compositional by definition rather than by accident.

It is counterfactual. The question is never what the system did, it is what becomes possible if some component behaves differently. No quantity of observation of a working system answers it, which is why monitoring, however good, never grew into design.

It has no ground truth. A test passes or fails. A design is correct until an adversary demonstrates otherwise, and the absence of a demonstration is not evidence. There is nothing to regress against, so the loop that made everything else in software tractable, write it and run it and see, does not close.

And it requires knowing what the organization is for. Whether a residual risk is acceptable depends on business intent, which appears in no artifact and changes without notice.

Every one of those properties defeats a technique that worked somewhere else. That is the whole explanation for the shape of the industry.

So we rationed the scarce resource. The highest-risk systems got deep attention. Everything else got something cheaper.

That something cheaper is worth naming precisely, because it is the same operation performed over and over. Expert threat reasoning gets **compressed** into portable substitutes (rules, patterns, requirements, controls, certifications, artifacts, and audit tests) that let thousands of people make mostly-good decisions without repeating decades of analysis. Compression is not a failure. It is how any expert discipline scales past the experts. Building codes are compressed structural engineering. Clinical guidelines are compressed medicine.

But compression is lossy, and it always drops the same two things. The threat model that justified the rule goes, and so does the reasoning that would tell you when the rule no longer applies. That loss is invisible right up until it matters.

It is worth seeing what that costs in one case, because the loss is not abstract. *Keys belong in HSMs* carries none of the things anyone would need in order to weigh it. Not the capital cost. Not the operational burden of ceremonies, quorums, and custodians. Not the latency added to every signing path. Not the throughput ceiling when each operation becomes a round trip to a device with a fixed operations-per-second budget. Not the disaster-recovery story, which is usually the hardest part. And not the only question that actually matters, which is how many of the reachable extraction paths that boundary removes in this system. Strip all of that out and nothing is left to reason with. A key either is in one or it is not.

One item belongs on that list that almost never appears on it, because it runs the wrong way. A certificate attests a specific version in a specific configuration, so a fix to the validated module is either a revalidation, measured in years, or a patch shipped outside the boundary, which quietly ends the state the certificate describes. Choosing validated cryptography therefore buys slower response to disclosed vulnerabilities in precisely the component you were being most careful about.

That is a real trade and frequently a good one. Getting key material out of the application's process is worth something, the separate administrative domain is worth something, and for some systems both are worth the patch latency several times over. It stops being a trade at the moment the choice is made because everyone makes it. Then you are paying an unpriced cost against an unnamed threat, and the thing that was supposed to be an engineering judgment has become a purchasing default wearing its clothes.

Which forecloses the interesting answer before anyone can say it. For a great many services, a key held by a local key-management process, running under its own user context, exposing a narrow signing interface, with a policy on what it will agree to sign and monitoring on what it is asked to sign, removes more of the paths that are actually reachable per dollar spent than a remote appliance does, and leaves a residual the organization can name out loud. That is a defensible engineering position. It is close to unsayable in an institution that kept the rule and discarded the reasoning, because the rule has no grammar for *better against this threat model, at this cost*.


## What the other professions kept

Building codes are compressed structural engineering. A builder sizes a joist from a table instead of re-deriving beam theory, and the table is the accumulated judgment of people who did derive it. Clinical guidelines are compressed medicine. Checklists are compressed operational experience, which is most of what made commercial aviation safe.

All three of those compressions worked, and none of them ate the profession that produced it.

A code does not stamp drawings. A licensed engineer does, their name goes on the seal, and they carry personal liability for the building standing up. A guideline does not treat a patient. A physician departs from it when the patient in front of them is not the patient it was written for, documents the reason, and answers for the outcome. A checklist does not command an aircraft.

In each case the artifact is scaffolding around a judgment that stayed attached to a person, and what kept it attached was that someone's name was on the result and the name was worth something. Deviation was permitted because someone was accountable for deviating well. The compression could never become the outcome, because the outcome already had an owner.

Security compressed and kept nothing.

Nobody signs the architecture. Look at what we have instead and notice how carefully each one avoids the claim. A risk acceptance names a specific risk and says an executive tolerated it, which is not an attestation that the design is sound. An audit opinion says controls operated, and the better auditors will tell you plainly that this is not the same as the system being secure. A vendor warranty covers a product, not your deployment of it. A penetration test reports what was found in scope in the time available, which is a statement about the test.

Try the question directly. In your organization, who is personally answerable for the claim that compromise of the workforce identity provider does not reach production signing authority? Not who would be blamed afterward, which is a different and much more crowded question. Who has put their name to it in advance.

In most organizations the honest answer is nobody, and this is not negligence. There is no instrument for it. No license, no seal, no standard of care, no professional body that can remove your ability to practise, and therefore no mechanism by which a considered deviation from the canonical control becomes a defensible professional act rather than an audit finding.

That absence explains the control cliff better than any account of institutional stupidity. In a profession with signatures, an engineer who chooses a cheaper design and documents why is doing their job. In one without, the same person has simply failed to implement the recommended control, and the only safe move is the canonical one. The rule is not just easier to follow. It is the only thing standing between the practitioner and personal exposure.

The obvious inference is that security should be licensed, and I do not think it follows. A standard of care needs a body of knowledge stable enough that a competent practitioner's obligations can be written down and then adjudicated years later by someone who was not there. Structural engineering has that. Whether security does is a real question, and the field has an unhappy record with credentials that certify familiarity with a vocabulary rather than the ability to reason about a system. Naming a missing instrument is not the same as prescribing that particular one.

It also sets up something that arrives much later in this essay. If a field cannot produce signatures, the closest available substitute is a price. Someone with money at stake, forced to distinguish between two architectures, does the work a professional body would otherwise have done. That is a poor substitute for a profession, and it may be the one actually available.


## Security is the composition, not the collection

The loss shows up first as a boundary problem.

A FIPS 140-3 validation provides meaningful assurance about a defined cryptographic module in an approved mode<a class="ref" href="#r-fips140">[fips140]</a>. It says much less about the product functions, networking, update system, operating system, and administration outside that boundary. A product can correctly use a validated module while depending entirely on behavior nobody validated. That does not make validation bad; it makes the boundary important.

It is also not a hypothesis about how certificates might age, because the record is public and I went and read it. Across a near-census of 415 FIPS 140-3 modules, 324 show no recorded update after their first validation, the median module is presented as current for roughly five years, and among those whose Security Policy could be fully extracted only 62 per cent pin a software or firmware version at all<a class="ref" href="#r-corpus">[corpus]</a>. That last figure is the one worth sitting with. For a large share of the population you cannot determine whether the build running in your datacenter is the build that was validated. The certificate is mandated, procured against, and audited, and in those cases it cannot be reconciled with the thing in production.

Isolation has the same shape, and I have written the long version of this argument elsewhere<a class="ref" href="#r-optimizer">[optimizer]</a>. Containers, VMs, confidential VMs, and dedicated security processors are four mechanisms built for four different adversaries making four different promises, and calling all of them sandboxes makes them impossible to tell apart. But the sharper point is what none of them addresses. A wall with no holes does no work, so every real deployment cuts holes through it, an egress path, a write channel, a tool API, somewhere to keep state, a credential. **Every hole hands back a property the wall was providing.** Move from a container to a confidential VM and you have built a taller, thinner wall around exactly the same holes.

That is the composition problem stated about as sharply as it can be. It is why an optimizer does not need to escape the wall if one of the doors we deliberately cut through it leads to the objective, and why containment is never the primitive you chose. It is the design wrapped around the primitive, which is to say it is security design, arriving in the newest domain we have and behaving exactly as it does in the oldest.

Layering has a version of this that is easy to miss, and it shows up wherever an organization has decided to presume compromise. The standard answer is to authenticate independently at more than one layer, at the network, again at the host, again at the application, so that failure of one does not hand over reachability. That is real design and the instinct behind it is correct. The composition question is whether those layers are actually independent, and the usual honest answer is that nobody has checked. Three authentication layers that chain to the same trust anchor, or that lean on the same identity plane, are three walls on one hinge. They will be counted as three controls and they will fail together.

There is a sharper version of the test. Ask which of those layers still holds if the asymmetric primitive underneath it breaks. Some layers protect their data plane with symmetric keys and survive that break; some do not. But even the symmetric ones are only as independent as their key establishment, and in most deployments the key establishment runs back through the same certificates as everything else. The diagram shows separation. The failure domain does not. This is answerable, it takes a day, and no framework asks for it.

PKI has the same shape too. Cryptography can establish that a key produced a signature. It cannot tell you who should have been able to cause that signature, why a relying party should accept the authority behind the key, or whether the governance that delegated that authority is still sound. The certificate path is one graph. The governance that makes the path meaningful is another.

The pattern repeats because the mistake is structural. The cryptography can be correct and the authorization wrong. The identity can be strongly authenticated and wildly overprivileged. The code can have no known vulnerability and sit in a catastrophic position of trust. The HSM can perfectly prevent extraction while the attacker is fully authorized to ask it to sign the thing they need. The audit can correctly determine that a control operated without establishing that the collection of controls produces the property everyone believes it does.

I have been saying a version of this for years. Breaches happen between systems, in the decisions that connected them. The components are usually fine. They are validated, monitored, patched, and owned. The joins are where the consequence lives, and a join is not a thing anyone bought. It is a decision somebody made, often years ago, often for a good reason, and usually without anyone asking what it made reachable.

The pattern is not confined to engineering, which is the best evidence that it is structural. Government classification is a compressed risk judgment carried on a marking, and almost every individual decision to apply one is defensible. The composition is what failed. The 9/11 Commission concluded that security requirements were nurturing overclassification and excessive compartmentation between agencies<a class="ref" href="#r-c911">[c911]</a>, and it named the incentive that produced them. There are no punishments for failing to share information, while sharing it wrongly carries criminal, civil, and administrative risk. One side of the error is priced and the other is free.

Notice when the bill arrived. The cost of decades of overclassification did not present as a classification failure. It presented as an intelligence failure, years later, attributed to agencies that could not connect what they already separately held<a class="ref" href="#r-moynihan">[moynihan]</a>. That is a trailing indicator, and by the time it becomes legible it is wearing someone else's name.

Security is not the sum of secure things. It is what the relationships among those things permit. That sounds too obvious to state, and our institutions routinely behave as though it were false. And the attacker never had to accept the compression in the first place. While defenders were reducing the system to a set of controls, the system itself stayed exactly where it was.

## One bug, two architectures

Everything so far has been argument. Here is the thing itself, small enough to hold in one head.

A service does three jobs. It terminates TLS, so it parses attacker-controlled bytes with a general-purpose library. It proves its own identity to peers, so it holds a long-lived private key. It runs business logic against a database, so it holds a database credential. Written the ordinary way, that is one process under one uid, and all three jobs share an address space.

Now state a property rather than a control. *Compromise of the code that parses untrusted bytes must not disclose the host identity or the database credential.* No product is named in that sentence, which is the point. It is a claim about what must remain true, and there is more than one shape that makes it true.

One shape is four processes under four uids, talking over local sockets that authenticate their peer. `netd` terminates TLS and holds no long-lived secret. `authd` holds the host key and exposes one operation, sign a well-formed challenge, and never returns key material. `appd` holds the database credential and accepts only a defined message schema, from `netd` and from nobody else. `logd` takes append-only writes. None of this is new. OpenSSH has been built this way since 2002, and Provos, Friedl and Honeyman wrote up the reasoning the following year<a class="ref" href="#r-privsep">[privsep]</a>. Postfix, qmail, and every browser you have used are the same idea.

Now drop Heartbleed into both. A buffer over-read in the TLS heartbeat extension, returning up to sixty-four kilobytes of adjacent process heap per request, repeatable as often as the attacker likes, and invisible in the logs<a class="ref" href="#r-heartbleed">[heartbleed]</a>. Not code execution. A read primitive, which is exactly why it is the right example. What an attacker gets is precisely and only what happens to be in the address space.

In the monolith, the address space is everything. The host private key is on that heap. So is the database credential, the session state, and the decrypted traffic of every other user currently connected. Whether a given read returns the key is a matter of heap layout and patience, and in 2014 the answer turned out to be patience: Cloudflare put a server up as a challenge and researchers extracted the private key from it within a day. Recovery means rotating an identity, reissuing, notifying relying parties, and assuming the database was read.

In the separated design the same bug is in `netd`, and `netd`'s heap holds TLS session state for the connections it is currently serving. That is all it holds. The host key is in `authd`, under a different uid, in a different address space, and a read primitive cannot cross an address space. The database credential is in `appd`, likewise.

What still leaks is the in-flight plaintext of connections `netd` is handling, which is genuinely bad and which no amount of process separation fixes, because handling that plaintext is the job. The design did not make the bug harmless. It decided, in advance, which secrets were allowed to be in the room when a bug like this arrived.

It is worth asking the same question for a different bug class, because that is what design reasoning actually looks like. Had the defect been code execution rather than disclosure, the monolith outcome is unchanged, since the attacker already had everything. In the separated design the attacker would additionally be able to speak the IPC protocol, driving `appd` through its schema and asking `authd` to sign well-formed challenges. Real capabilities, bounded by an interface somebody designed, rather than unbounded by an address space that happened to contain everything. Same architecture, two threat classes, two different residuals, and you can only see either one by reasoning about the shape.

@@FIGK@@

Here is the part that matters for this essay.

Nothing in the security pipeline can tell these two systems apart. They link the same library, so the SBOM is identical. They are affected by the same disclosure, so the CVE is identical. The base score is computed on the vulnerable component rather than on your deployment, so that is identical too, and both land in the same remediation bucket under the same policy with the same deadline. The scanner output matches. The audit tests whether critical vulnerabilities were patched within the window, and both pass or both fail together. The pentest is scoped to the exposed interface, which is the same interface. Every instrument agrees the two systems are in the same condition, and one of them loses its identity key while the other does not.

Heartbleed makes this concrete in a way that is almost too neat. NVD gave it a CVSS v2 base score of 5.0, Medium. It was later rescored 7.5, High, under v3.1. The bug that forced a global certificate reissue was rated medium, and the rescoring did not fix anything, because both numbers describe the component rather than your deployment of it, and the whole question was what your deployment kept in that address space.

CVSS does have a slot for the answer. The environmental metrics exist so a consumer can re-score against their own architecture, and almost nobody populates them. Not from laziness. Doing it correctly requires knowing what compromise of that component reaches in your system, which is the expensive reasoning this entire essay is about. The industry built the field and then discovered the input was the scarce thing.

There is a second thing a severity number cannot carry, and it gets worse as isolation moves into hardware. A score rates how bad the exposure is. It says nothing about whether stopping it is a maintenance window, a configuration change you live with, a hardware refresh cycle, or decommissioning a platform generation and rotating every secret ever sealed to it<a class="ref" href="#r-optimizer">[optimizer]</a>. Those are four different budgets with four different owners and four different timelines, and severity distinguishes none of them. Both gaps have the same cause. The score describes the defect, and every question anyone actually needs answered is about the system around it.

And the separated design costs more. Four supervised processes instead of one. Serialization on a path that used to be a function call. Latency. New failure modes when a socket goes away. Harder debugging, more deployment surface, and a schema that has to be maintained as a real interface because it is now a security boundary. Somebody has to argue for all of that.

Against what? No framework awards points for it. No auditor tests for it. No procurement questionnaire asks. The engineer proposing it is asking for budget to change a property that every instrument reports as unchanged, and the engineer who does not propose it is not out of compliance with anything.

That is the whole argument in one service. The reasoning that distinguishes these two systems is exactly what compression discarded, the market cannot see the difference, no instrument records it, nobody signs for it, and the attacker experiences nothing else.


## The compressed version is the one you can buy

Once judgment has been compressed into artifacts, the artifacts are what the market can transact.

A scanner is easy to buy. A pentest has a scope, a start date, and a report. An HSM has a SKU. MFA has a deployment percentage. An SBOM is a file. Each can be assigned a budget, an owner, a vendor, a metric, and a procurement process.

Now try buying this: *understand the system well enough to determine whether its authority relationships, trust boundaries, dependencies, and failure modes create unacceptable attack paths, then compare alternative architectures and keep doing that as the system changes.*

Which produces a corollary to Clarke's third law:

> **Sufficiently advanced security design is indistinguishable from hand-waving to the buyer.**

One vendor says: *hardware-backed key storage, zero trust, AI-assisted code review, continuous scanning, MFA, immutable logging, FIPS-validated cryptography.* Another says: *we removed the authority relationship between our workforce identity plane and our signing system; compromise of the workforce IdP no longer creates a path to signing authority, administrative recovery is separately governed, and the signing interface cannot export key material.*

The second statement carries far more information. It is also far harder to evaluate. Does the path really disappear? Is the recovery identity actually independent? Can another role recreate the relationship? Does disaster recovery quietly reconnect the two domains? To check the claim, the customer needs much of the expertise they were trying to buy. The first vendor gives them familiar nouns instead, all of them legible, testable, trackable, and slide-ready.

This requires no gullible buyers and no dishonest sellers. It is what any market does when quality is hard for the buyer to observe. The observable proxy displaces the unobservable property, and the displacement is stable. But there is a sharper structural point underneath it, and it does not require anyone to be acting in bad faith. **The intermediate machinery holds its position as the thing being purchased precisely because the alternative cannot be evaluated directly.** If a buyer could cheaply verify whether an architecture produced the properties they needed, a great deal of what currently gets sold would be repriced as an input rather than an outcome. Nobody has to defend that arrangement for it to persist. It persists because nothing in the market currently makes the alternative visible.

CISA's Secure by Design and Secure by Demand efforts are attempts to shift this equilibrium by giving purchasers better questions<a class="ref" href="#r-cisa">[cisa]</a>. The underlying information problem remains. The buyer wants to know whether the thing is secure enough for what they are going to do with it. What the market can cheaply supply is a list of the security things it contains.

There is a second problem, and it is worse. Good security design produces almost no theater. If you redesign a system so a compromised workforce identity cannot reach a signing service, nothing flashes red. There is no blocked-attack counter, no chart showing 14,218 threats prevented this month, no queue demonstrating how busy the product has been. A dangerous path simply does not exist. That turns out to be a very difficult outcome to sell.

::: keylesson
Good design produces almost no theater. A path that no longer exists emits no alert, fills no queue, and shows up on no dashboard, so the strongest security work is also the work that is hardest to show anyone. That is a market problem before it is an engineering one, and it is why the intermediate machinery keeps its position as the thing being purchased.
:::

## When the threat model falls out of the rule

Compression has a second failure mode, and this one is internal to the engineering organization rather than the market.

A key gets stolen. We learn that software-only storage is vulnerable to whole classes of compromise. We build smartcards, secure elements, HSMs, remote KMS. The institutional rule that survives is *keys belong in HSMs*. The original argument was *against these adversaries, for a key with these consequences, this boundary removes important extraction paths at a cost justified by the risk.* The compressed rule is enormously useful. It is also where dogma starts, because the justification is exactly the part that got discarded.

Suppose the key belongs to a small service, and a remote HSM is expensive, operationally heavy, or latency-sensitive enough that the team will not do it. The security model now has two states: HSM-backed is good, not HSM-backed is bad. The team cannot afford good. So the key lives in an environment variable.

There was an intermediate design available. Run the signing key in a separate process under a different user on the same host, and give the application access only to a narrow signing interface. Is that an HSM? Obviously not. Root still wins, a compromised kernel still wins, and depending on the interface, application compromise may still permit unauthorized signing. But code execution as the application user no longer discloses the key. Dumping the environment no longer discloses it. Accidental logging no longer discloses it. The interface can constrain operations, and key access becomes separately auditable. Several attack paths vanish for almost no cost.

If the security institution gives that design no credit because it is not the canonical control, implementing it becomes irrational. That is the **control cliff**: when only the canonical control counts, meaningful improvements below the threshold acquire zero institutional value, and teams jump from the ideal to nothing at all. The rule that encoded good security knowledge produces a worse security outcome, not because the rule was stupid, but because the threat model that justified it is no longer attached to it. Design asks which threats a mitigation addresses, which remain, what it costs, and whether the trade is right here. Dogma asks whether the implementation conforms to the approved pattern. **Dogma replaces optimization with classification.**

::: keylesson
A rule is compressed threat reasoning with the threat model stripped out. That compression is what lets an organization scale past its experts, and it is also what makes a rule capable of blocking a cheaper design that would have removed more consequential paths.
:::

Retiring one takes decades. Shoe removal became universal in 2006, five years after Richard Reid's attempt, and ended in July 2025 because scanning equipment had improved rather than because anyone reopened the question<a class="ref" href="#r-tsa">[tsa]</a>. The tell is that PreCheck members were exempt throughout, so a traveller who paid a fee stood outside the control for its entire life. The rule was defensible in 2002, when the scanners genuinely could not see what Reid carried. It then ran for nineteen years without the reasoning that justified it.
The cliff has a mirror, and the mirror is worse because it looks like success. Encryption at rest is the cleanest example in wide deployment. The control is real, usually implemented correctly, and its threat model is physical: a stolen drive, a decommissioned array, a backup tape that leaves the building in a van. Against those, it works exactly as designed.

Now name the thing that actually takes the data. An over-privileged service account. An injection flaw. A compromised application host. A support tool with a standing query path and a bored contractor. In every one of those the database is asked politely for plaintext by something holding valid credentials, and it complies, because complying is its entire job. At-rest encryption is not defeated in those scenarios. It is not present in them.

And it satisfies everything. The questionnaire asks whether data is encrypted at rest. The auditor tests whether the feature is enabled. The framework awards the control and the report comes back clean. An organization can hold that report on the strength of a mechanism that does not participate in its most likely path to loss, and no one anywhere in the chain has said anything false.

So the two failures are symmetric, which is how you know they share a cause. The control cliff withholds credit from a design that removes real paths. Its mirror grants full credit to a control that removes none of the paths that matter. Both are what happens after the threat model has been stripped off, because the threat model is the only thing that would have told you which case you were standing in.

And the compression obscures what the key was ever for. The key matters because some other system accepts operations performed with it. The asset is usually not the key material but the authority it represents. Put the key in the finest HSM money can buy, then expose `sign(anything)` to a compromised caller. The key is perfectly nonextractable and the authority is completely unprotected. The attacker never needed to steal it; they needed the HSM to perform the operation. What the device actually buys you is the removal of key material from the application's process and the creation of a separate administrative domain around its use, and neither of those is what the certificate speaks to<a class="ref" href="#r-corpus">[corpus]</a>. Which makes the real questions larger than storage: who can request an operation, what can they request, what happens when the caller is compromised, how durable is the resulting authority, and which downstream systems accept it. Now the HSM sits where it belongs, as one candidate transformation of the attack graph rather than the objective.

## Why the artifacts keep multiplying

The third failure mode is that compression begets compression.

For decades, software vendors effectively said *trust us*. Customers stopped accepting that and asked a reasonable question: what is in it? Enter the SBOM, which is genuinely useful. When a catastrophic vulnerability lands in a widely deployed library, knowing which products contain it turns a scavenger hunt into a query.

But what the buyer cares about is not whether component X is present. It is whether the vulnerability in X can hurt them in this system as they operate it, which requires knowing whether the code was compiled, whether the feature is enabled, whether the function is reachable, whether attacker-controlled input reaches it, what privilege the process holds, what isolation surrounds it, and what the resulting capability actually gets you.

The SBOM does not answer that. It was never supposed to. But institutions convert the thing they can require into the thing they wanted to know, and so:

Does the vulnerability affect this product? Add VEX. How do you know? Add reachability analysis. Under which configuration? Add configuration evidence. How do you know production is configured that way? Add attestation. Can an attacker change it? Add authorization data. Who can become that administrator? Add identity relationships. What if the IdP is compromised? Add upstream trust relationships. What does that access accomplish? Add consequence analysis. Is any of it still true today? Add continuous reconciliation. How do we know reconciliation sees all relevant state?

**Regressus ad infinitum.**

Serialization moved pieces of the knowledge around. It did not abolish judgment.

The regress is self-sustaining for a reason that has nothing to do with anyone's intentions. **Every new proxy is easier to institutionalize than the judgment it stands in for.** A proxy can have an owner, a budget, a tool, a maturity model, a reporting cadence, and an executive sponsor. Judgment can have a person. So the proxy wins the allocation fight, every time, and keeps winning it long after its next increment produces less risk reduction than changing the underlying design would. That is not waste in the accounting sense. Each program delivers something. It is opportunity cost, and it compounds.

*Cui bono?* Not as conspiracy, but as budget. The vendor gets a product. The security team gets a program. Procurement gets a requirement. The regulator gets something enforceable. The auditor gets a repeatable test. Management gets a dashboard. Everyone receives something tangible from the intermediate.

Follow it far enough and you get the reductio. Every product has a perfect SBOM. Every vulnerability has a current VEX statement. Every configuration is continuously attested. Every identity relationship is represented. Every control emits evidence. Every dashboard is green. And there remains a three-step path from an internet-facing system to the authority required to destroy the thing the organization cares about.

We have built a perfectly documented insecure system.

::: keylesson
The regress is budgetary before it is epistemological. A proxy can have an owner, a tool, and an executive sponsor; judgment can have a person. So the proxy wins the allocation fight and keeps winning it long after the next increment stops buying risk reduction.
:::

## Two different cost functions

None of the compression is visible to the attacker, and this is where the mismatch stops being philosophical.

There is a name for the mechanism and it is not a security idea. Conway observed in 1968 that any organization designing a system is constrained to produce a design that copies the organization's own communication structure<a class="ref" href="#r-conway">[conway]</a>. The interfaces people can negotiate become the interfaces that get built.

Security has a sharper version of the same law, because defenses are not built by whoever designed the system. They are built by whoever was funded to build them. The system mirrors the organization that produced it, the defenses mirror the organization that paid for them, and nothing requires those two to agree with each other or with anything an attacker cares about.

Look at how the money divides. Endpoint, identity, AppSec, cloud, network, SOC, vulnerability management, GRC. That list is not a taxonomy of risk. It is a set of reporting lines. The defender's allocation problem is to cover *every* domain adequately, because an uncovered domain is an unbounded liability and because each domain has an owner who must answer for it. Spend is spread by structure, and each team produces real coverage of the surface it was handed.

So the boundaries we defend are organizational boundaries, while the boundaries that matter are trust boundaries. Where the two coincide the defense is good. Where they diverge nothing is watching, because a path crossing four teams is not on four backlogs. It is on none.

**Your security architecture is your org chart, not your risk graph.**

The attacker has a different function entirely. They allocate nearly everything to identifying and exercising the single cheapest viable route, and they abandon the rest. They do not have to be adequate anywhere except along one path.

It is worth killing the obvious fix before anyone reaches for it. The inverse Conway maneuver says reshape the organization until it produces the architecture you want, and in product engineering that often works. It cannot work here. No org chart is isomorphic to an attack graph. The graph is denser than any reporting structure, it runs through vendors and customers you do not employ, and it changes every time somebody grants a permission on a Tuesday afternoon. You cannot reorganize your way into owning every composition, because the compositions outnumber the people. Either the consequential paths keep going unowned, or something other than a team has to hold them.

These are not two perspectives on the same problem. They are asymmetric cost functions over the same graph. The defender pays for breadth; the attacker pays for depth on one line. That asymmetry has always favored the attacker at the margin, and it is the reason a path like

**internet-facing service → application identity → CI system → deployment credential → production administration → signing service**

survives so much spending. No step is astonishing. Every team has a reasonable story for its own edge. The path is the problem, and no team owns it.

The path diagram above is that law drawn out. Six owners across the top, one route underneath, and the reason the route survives is not that anyone was careless. It is that no reporting line contains it.

This is why BloodHound mattered. Individual directory permissions were not hidden before BloodHound; what changed was the representation. Put identities, privileges, groups, sessions, and administrative relationships into a graph and ask what they compose into. Its OpenGraph work now extends that analysis across cloud, SaaS, and developer platforms<a class="ref" href="#r-bloodhound">[bloodhound]</a>. The interesting unit stopped being the permission and became reachability. Not *is this permission appropriate* but *what becomes possible because this permission exists alongside the rest*.

A security product operates on the graph it is given. Security design changes the graph: strengthen an edge, remove an edge, split a failure domain, change an identity model, eliminate a credential, or deliberately leave the path and reduce the consequence instead. The point is not that every path should disappear. The point is that someone should know why the consequential ones exist.

::: keylesson
Defenders and attackers are not two perspectives on one problem. Budgets are allocated to domains because domains have owners. Nothing is allocated to the composition, because the composition has none. That is not a funding mistake anyone made; it is what allocation by organisational structure produces, and the attacker's whole method is to work in what it leaves out.
:::

## AI makes this worse first

Now hold that asymmetry fixed and drop in cheaper reasoning.

Two claims sit next to each other here and they are not equally durable. Take the durable one first, because it survives almost any forecast about what models can do.

Removing a dangerous trust edge is coordination work, and coordination did not get cheaper because reasoning did. A machine can identify the edge in seconds. Removing it may require changing an API, migrating customers, rewriting authorization, reissuing credentials, altering disaster recovery, accepting latency, coordinating four teams, and supporting the old architecture for another year. None of those costs are made of reasoning. This holds even if model capability stopped improving today, and it is the half of the argument I would defend hardest.

For scale, take the largest coordination problem currently running. Google has been working on post-quantum migration for roughly a decade and targets 2029 for Google Cloud, with some hardware riding natural replacement cycles past that date, while NIST's transition guidance anticipates final deprecation of the quantum-vulnerable algorithms somewhere between 2030 and 2035<a class="ref" href="#r-pqc">[pqc]</a>. That is close to the best-resourced actor available, migrating a stack it controls end to end, on a fifteen-year clock. Larger signatures and slower verification make it harder than previous migrations rather than easier. None of that work is reasoning. It is inventory, dependency analysis, negotiation, standards, and physical replacement, and not one hour of it gets cheaper because a model got better.

The assurance apparatus is part of that cost, which is the part nobody budgets. As of mid-2026 essentially no FIPS certificates existed for the core post-quantum algorithms, and validation runs two to three years end to end, with the post-submission stage alone averaging 579 days<a class="ref" href="#r-corpus">[corpus]</a>. Regulated buyers cannot deploy what is not validated. So the instrument built to give those buyers confidence is now among the things setting the pace of the migration it was supposed to make safe. That is not an argument against the program. It is what happens once an artifact becomes load-bearing.

The second claim is a prediction and could be wrong. Adversarial path search is almost pure reasoning over a representation, enumerate and compose and evaluate and discard and repeat, so it should capture the saving almost immediately. That would fail if search turned out to be bottlenecked on something other than reasoning, which is not obviously false.

There is a measurement pointing the right way. In 2026 Anthropic evaluated frontier models building working exploits directly from disclosed patches<a class="ref" href="#r-anthropic">[anthropic]</a>, producing eight code-execution exploits across eighteen Firefox patches and privilege escalation for eight of twenty-one Windows kernel vulnerabilities where no source was available. The number that matters is not the count. The first working Firefox exploit arrived in under an hour, and the release carrying the fix was still eighteen days away. Microsoft ships most kernel patches on a monthly cadence with staged rollout behind it. Anthropic's own reading is that such cadences were built on the assumption that weaponizing a disclosed patch costs expert-weeks and that few people can do it. Whether or not that is why the schedules were designed as they were, an interval measured in tens of minutes against a release measured in weeks is the thing defenders now have to reconsider.

So the near-term effect of cheap reasoning is not a defensive renaissance. It is a widening gap, because information moves at machine speed while organizations change at organizational speed. The mismatch we have lived with for thirty years becomes acutely more expensive before anything structural improves.

Which raises the question of what would actually notice.

## Somebody has to pay for getting the architecture wrong

Not every risk should be eliminated. NIST's own risk language recognizes acceptance, mitigation, avoidance, and transfer as legitimate responses<a class="ref" href="#r-nist37">[nist37]</a>. If eliminating a class of loss requires a $20M redesign, and the loss is quantifiable enough that an insurer will absorb much of it for a far smaller premium, buying the contract can be the correct engineering decision. Insurance does not make the system secure; it changes who bears the consequence when it is not. So does containment, so does recovery, so does acceptance. The objective was never to maximize controls but to allocate finite resources across prevention, containment, detection, recovery, and transfer.

Insurance is more interesting than another control, though, because insurers eventually have to price the result. Today they use the same visible proxies everyone else does: MFA, EDR, backups, vulnerability management, IR plans. Munich Re describes the feedback loop plainly. Claims history matters, but underwriters also have to anticipate new exposures and adjust modeling as threats change<a class="ref" href="#r-munichre">[munichre]</a>. Marsh reports underwriters already scrutinizing aggregation risk and AI exposure even while rates fall<a class="ref" href="#r-marsh">[marsh]</a>.

So picture the correction running its course. Cheap adversarial search changes the real loss distribution, losses eventually show up in claims, insurers reprice, and somewhere down that chain architecture acquires a number the CFO can read without becoming an architect. Every link in it is slow, but slowness is not the interesting part.

The binding constraint is that **the underwriter has exactly the same observation problem the buyer does.**

They price MFA and EDR because MFA and EDR are observable. If an underwriter could cheaply verify *workforce identity has no path to signing authority*, they would already be pricing it. The incentive is enormous and free of the buyer's conflicts. They are not, because establishing that claim requires reasoning across identity, infrastructure, configuration, code, and operations at once, and that has always cost more than the answer was worth to any single party.

@@FIGE@@

So the loop cannot close on claims data alone. Loss experience can say that something changed; it cannot say which architectural feature to price, or verify it at underwriting time across a book of thousands. And as with classification, the harm arrives late and wearing someone else's name, which is precisely the condition under which a feedback loop teaches nothing.

The market cannot reward a property it cannot observe. Insurers are worth the detour because they have unusually strong incentives to observe it and still end up pricing proxies. That points at the real bottleneck. It is not demand for better security information. It is the cost of producing it.

Which reframes the question. The interesting one is not whether AI can do security architecture. It is whether machine reasoning can make architectural claims cheap enough to *inspect*, because the moment they are inspectable, there is already a party waiting to price them, and the correction runs much faster than the artifact market would ever produce on its own.

::: keylesson
The insurance loop cannot close on claims data alone. An underwriter has the same observation problem the buyer does, which is why architecture is unpriced despite an enormous incentive to price it. Inspectability, not loss experience, is the binding constraint.
:::

## The representation we never built

Making architecture inspectable is a representation problem, and we are further along than it looks.

Joern constructs Code Property Graphs so properties of large codebases can be explored through graph queries<a class="ref" href="#r-joern">[joern]</a>. CodeQL similarly extracts a queryable representation including syntax, control flow, and data flow<a class="ref" href="#r-codeql">[codeql]</a>. BloodHound represents identities and privileges so paths can be searched. OpenTelemetry's ecosystem derives service graphs from observed traces<a class="ref" href="#r-otel">[otel]</a>. SBOMs give composition. IAM systems give principals and permissions. Configuration gives intended state. Policy extraction gives intended constraints.

Each of those is a small, already-shipped demonstration of the same claim. **A better representation converts reasoning that was previously artisanal into reasoning that is merely a query.** A Code Property Graph means nobody rereads a million lines to trace one data flow. An identity graph means nobody reconstructs nested group membership from screenshots to find out who can reach an administrator. A service graph turns millions of traces into relationships. None of them answers a security question. All of them changed what it costs to ask one.

The gap is that every one of these begins too late. They start from something already built.

Before there is a function call, there is an intended capability. Before there is a private key, there is an authority someone decided the system needed. Before there is a network connection, there is a relationship the architecture permits. Before there is an IAM role, there is a principal someone decided should be able to cause a state transition. The starting objects are not functions and variables, and it is worth being declarative about them, because a wishlist is not a specification. Six kinds of thing, and a representation missing any of them cannot do the work.

**The property** somebody decided must remain true. **The principals and authority relationships** it depends on, which is the question of who can cause what. **The design decision** taken to make the property hold, together with the alternatives that were considered and rejected. **The assumptions** that decision rests on, written down so they can be checked rather than silently inherited. **The residual risk** knowingly accepted, which is the part a rule never records because a rule has no way to say *and we decided this was fine*. And **the conditions under which the claim stops holding**, which is the piece compression always drops and the only one that lets the representation invalidate itself.

The longer inventory a real system needs, capabilities and information flows and failure domains and attacker models and operational constraints, is what those six grow into. The six are the ones you cannot leave out.

A Code Property Graph asks what security-relevant properties emerge from the code we wrote. The missing representation asks **what architecture would produce the properties we need**. Call it a design graph or call it nothing yet; the name matters less than the direction.

The categorical difference is worth stating plainly, because it is the same difference the opening described. Existing graphs represent facts about a system. A design graph also represents the claims about why the system is shaped this way, the threats those choices were meant to defeat, and the conditions under which the claims stop holding. Those are precisely the three things compression discards. A representation that carries them is a cache that remembers why it was populated.

::: keylesson
A minimal version is smaller than it sounds. One consequential property, the authority relationships it rests on, the decision that was supposed to make it hold, and one query against evidence you already collect that would prove it false. If that fits on a page and survives contact with the IAM graph, it is a design graph. Everything else is scale.
:::

And it is a design tool, not a documentation tool. Say the desired property is *compromise of the application must not disclose persistent signing authority*. That is not an HSM requirement. It is a property, and the candidates are comparable. The environment-variable design yields `app compromise → key disclosure → persistent signing authority`. A separately permissioned local signer yields `app compromise → constrained signing operation`. A separate host changes it again, a remote KMS again, an HSM again, and a protocol redesign that eliminates the long-lived key removes the question entirely. That is the reasoning the control cliff destroyed, made explicit enough to compare.

Walk one decision through the loop. Suppose the team takes the second row, a separately permissioned signer on the same host, because a remote KMS is not justified by the residual host-compromise risk. That choice is now an assertion with content. The application cannot read key material, the signing interface accepts only transaction-shaped payloads, and the signer runs under an identity no workforce account can assume.

Each of those is falsifiable by evidence somebody is already collecting. The first meets code analysis, which finds a debug endpoint that maps the signer's memory for crash reporting. The second meets a runtime trace showing the interface accepting an arbitrary byte string from an integration harness that shipped by accident. The third meets the IAM graph, which finds a break-glass role granting assume rights to on-call, and on-call is a workforce group. Three contradictions, and nobody had to imagine the attack in advance. The design said what had to remain true, and the implementation disagreed in three places.

That reversal is the whole point. Once the implementation exists, the design stops being a document and starts being something reality can contradict.

**desired property → threat model → design → implementation → observation → contradiction → redesign**

That is where design and continuous assurance finally meet. Assurance asks whether reality supports the claims we made. Design asks whether those were the right claims. Continuous assurance without continuous design is just a faster way to prove the wrong architecture is behaving exactly as specified.

Threat modeling is already moving toward the front of this chain. Adam Shostack's PHANTOM-B, presented at Black Hat USA 2026, is a practical elicitation framework for asking what can go wrong in the LLM-specific parts of a system<a class="ref" href="#r-phantomb">[phantomb]</a>, evidence that the discipline adapts to new system classes rather than ossifying. But elicitation is upstream of what I am describing. A taxonomy helps you remember what kinds of things go wrong. A threat model asks what can go wrong here. A design model asserts what must remain true and which architectures make it true, then stays connected to the implementation that is supposed to deliver it. Connecting those stages is the open problem.

The danger is obvious enough to name before anyone builds it. The instant this becomes *Design Graph Coverage: 94%*, with a standard, a procurement mandate, and an audit test for currency, we have invented the next SBOM, a new compression sold as the outcome with the judgment squeezed back out. The defense is in what the representation is *for*. Not *here is the graph, therefore we understand the system*, but **here is our current model of the system; find the shortest path that proves us wrong.** A representation optimized to be attacked resists institutionalization in a way one optimized to be certified does not.

::: keylesson
A representation of a design survives only while its purpose is to be attacked rather than certified. The moment anyone can report coverage against it, it has become the next artifact, and the judgment it was built to carry gets squeezed back out of it exactly as it was the first time.
:::

## What has to get better

You can already watch the bottleneck move, one layer down.

Generation has become close to free. An assistant can emit thousands of lines in an afternoon, and a large share of newly written code now comes out of one. Net additions to shipped systems have not moved remotely as far, because typing the implementation was never the constraint. Most engineering time went to understanding existing systems, designing changes, debugging, testing, reviewing, and coordinating with other people.

@@FIGG@@

The gap is the judgment, and it did not get cheaper when typing did.

Lines of code is a discredited metric, and that is the useful part. It counts the thing that just got cheap and not the thing that was ever scarce, which is the error this essay has been describing since its first page.

Put more precisely, machine reasoning collapsed the marginal cost of implementation faster than it collapsed the cost of deciding what should be implemented. For security that is not neutral. A flawed architectural assumption used to propagate at the speed of a person implementing it and can now cross thousands of lines and many components before lunch, in a form that looks finished. None of that is implementation capacity. Deciding what should be built, what should be able to reach what, which assumptions are safe, what an attacker can influence, and which properties must hold when the system is under stress is the scarce resource this essay opened with, showing up in a domain where the cost of typing used to hide it.

The design representation in the previous section only helps if machine reasoning reaches a specific level, and the trajectory matters more than the current capability.

The unit over which machine reasoning is economically useful has been growing, from token to line to function to task to repository. But the more informative axis is not size, it is method. Early code generation was autocomplete over nearby context. Then came genuinely complex implementation achieved by brute-force iteration (write, compile, run, fail, mutate, repeat) that works but scales with the number of loops you can afford. What has been changing more recently is the ratio, with more of the work coming from an internal model of the system and fewer loops spent discovering it empirically. That distinction is the one that matters here, because architecture is precisely the domain where brute force is unavailable. You cannot iterate your way to a trust-boundary decision by trying it in production and observing the failure. Design reasoning requires holding a model and interrogating it. A system that only reaches good answers through iteration will never reach architecture; a system whose competence comes from the model might.

The rungs above implementation apply the same test to larger objects. **Adversarial system reasoning** is where the object stops being code at all. The objects are identities, authority, trust boundaries, dependencies, configuration, deployment, and operational assumptions, and the characteristic question becomes what a compromise of this component makes possible. **Design optimization** sits above that, where the question stops being what is wrong with this system and becomes whether it should have been shaped this way, given the threat model, the constraints, the available mitigations, their cost, and the residual risk each one leaves.

Everything below that last step makes the existing machine faster. Only the last step changes what the machine is for.

You can watch that ladder in one example. *Sensitive keys should be stored in an HSM* is retrieval. *This key is in an environment variable, so application compromise discloses it* is contextual analysis. *A remote HSM removes additional extraction paths but costs materially more and adds a service dependency; in this threat model a local constrained signer eliminates the highest-likelihood paths far more cheaply, and the residual host-compromise risk is accepted* is design tradeoff reasoning. *The key exists only because the protocol requires long-lived signing authority here; change the protocol and the key and several authority paths disappear together* is architecture.

A model can emit all four sentences today. That is not the bar. The bar is deriving them from the actual system, supporting the premises, noticing missing evidence, finding alternatives nobody proposed, and staying correct as the implementation changes. We are plainly not there. Today's systems reason impressively over bounded technical problems, while maintaining a reliable model of a large, evolving organization and making good architectural tradeoffs inside it remains much harder.

The open question is whether that gap is a categorical limitation or simply the next point on the same curve. I do not know, and neither does anyone else. But the reason to care is not that a machine would replace the architect. It is that the architect's reasoning would become something a buyer, an auditor, or an underwriter could inspect.

## The obvious objections

Four of these are worth taking seriously, because the first three are what I would say if someone handed me this essay.

**Design review has never scaled and never will. This is a fantasy about a bottleneck that is structural.** The objection is right about history and wrong about the cause. Nothing in the preceding sections claims that a human design review scales. The claim is narrower, that the reasoning underneath it is expensive rather than impossible, and that its cost is the thing determining how much of it gets done. If the cost is a property of reasoning itself then it can move, and if it is a property of the problem then it cannot. I think it is the first and I have argued why in section 12, but I hold that more loosely than anything else here.

**Attack-path tooling already does this.** It does a specific and valuable part of it, and the difference is categorical rather than a matter of coverage. An identity graph finds the paths that exist in the system you built. It cannot tell you whether that system should have been shaped this way, because it holds no representation of what anyone intended, which threats a choice was meant to defeat, or what would have to change for the choice to stop being right. Ask BloodHound whether a path should exist and the question is not expressible. That is not a gap in the product. It is a consequence of starting from facts about an implementation rather than claims about a design.

**This is threat modeling with a new noun.** Partly, and that is a point in its favour rather than against. The lineage is the right one and I would rather inherit from it than pretend otherwise. The difference is in what happens after the workshop. A threat model is a document, produced at a moment, accurate about a system that then changes underneath it. What I have described is a maintained assertion that implementation evidence is continuously allowed to falsify, which is a different object with a different failure mode. Threat modeling asks what can go wrong. This asks what we claimed would stay true, and whether it still does.

**If controls are so inadequate, why did the industry work?** Because they were not inadequate. Multi-factor authentication ended an entire category of account compromise. Memory-safe languages retired classes of defect that consumed a generation of researchers. Hardware key storage genuinely prevents extraction. Every one of those is compression working exactly as intended, and the argument here depends on that being true. A compression that produced nothing would have been abandoned decades ago. The problem is not that the substitutes are worthless. It is that they are worth enough to have become the thing we buy, measure, mandate, and mistake for the property.


## What changes

The bifurcation is clean. **If machine reasoning stops at code, it accelerates the security economy we already have. If it reaches architecture, it starts competing with that economy's unit of value.**

The first branch is easy to picture, because it is already underway. More code written, more findings generated, more evidence collected, more controls tested, more alerts triaged. Genuinely useful, and not a change in kind. The compressed substitutes keep their position as the thing being purchased; they just get produced faster.

The second branch is the one where today's artifacts stop terminating in dashboards and start functioning as premises. The SBOM becomes evidence about composition. The Code Property Graph becomes evidence about implementation. The identity graph becomes evidence about authority. The service graph becomes evidence about observed interaction. Threat intelligence becomes evidence about changing attacker capability. The threat model becomes an assertion about what can go wrong; the design model, an assertion about what must remain true. None of them gets to pretend to be security. The compressed substitutes we built because judgment was unaffordable become inputs to reasoning that operates on the system again, which makes today's pipelines more valuable, not less.

Then the language changes. Instead of *do we have an HSM*, ask which key-extraction and signing-abuse paths remain. Instead of *do we have an SBOM*, ask which component failures create reachable paths in this deployment. Instead of *is MFA deployed*, ask what authority stays reachable after compromise of a factor, a session, a device, a recovery process, or the identity provider itself.

And then the money moves. The existing security market earns most of its revenue applying controls to systems that have already been designed, which is the only available response when redesign costs more than monitoring. Change that ratio and some portion of the spend migrates upstream, from buying another mechanism to watch a dangerous relationship to removing the relationship. That is not a smaller market. It is a different one, transacting in a different unit, and the incumbent position in it is far less secure than the current one.

And a design system worth having should argue back. Propose an HSM and it asks what happens when the authorized caller is compromised. Propose network isolation and it finds the management plane crossing the boundary. Propose MFA and it inspects recovery. Propose a process boundary and it shows what root still gets. Propose insurance and it separates transferable financial loss from operational, legal, and reputational consequence. Propose doing nothing and it tells you which fact would make that irrational.

The objective is not the canonical answer. It is to make the current answer survive stronger adversarial scrutiny than the people who wrote it could generate on their own.

That does not eliminate human judgment; it concentrates it where it belongs: materiality, proportionality, business intent, novel threats, operational tradeoffs, risk acceptance, and accountability. And it hands the machine the part machines may become extraordinarily good at, which is searching more paths, holding more context, and challenging more assumptions than any one person can.

We never stopped knowing how to do security design. We compressed it, sold the compression, mandated the compression, audited the compression, and then mistook it for the thing it stood in for. Attackers never had to participate in any of that. They got the graph, and searched it.

Cheap reasoning will hurt before it helps, because it lands on the attacker's side of an asymmetry we built ourselves.

But the rationing that produced all of this was never a law of computing.

It was a price.

If that price falls far enough, security design scales. Not because anyone recovers a lost principle, but because the reasoning behind the ones we already have could run against every system that matters instead of the few we could afford to think about.

Which leaves a question that is not technical.

> **Whether we keep buying compressions of security judgment after the reasoning they replaced stops being scarce.**

### What this post does not establish

The limits, stated plainly. The compression model in Part I is my explanation for the shape of the security industry, not a demonstrated result; it fits the observed pattern, which is not the same as having been tested against one. The control cliff is drawn from practice rather than from a study, and I have not measured how often teams actually jump from the canonical control to nothing.

The lines-of-code figures in section 12 are illustrative rather than measured. The pre-assistant range traces to old and much-argued studies, and no one has yet published a credible measurement of net shipped code per developer in the assistant era, so the second number is an estimate. The argument depends only on the two curves diverging, which is observable, and not on where either one sits.

The claim that adversarial search captures cheaper reasoning faster than remediation does is reasoned, not observed. It follows from the structure of the two activities, and someone should go and measure it.

The insurance argument is the most speculative thing here. I have not spoken to underwriters about whether architectural inspectability would change how they price, and the entire chain from cheaper search through claims, repricing, procurement, and vendor behaviour is a prediction with several slow links in it, any of which could fail to move.

The comparison with licensed professions in section 2 is an argument by analogy and should be read as one. I have not established that professional liability is what preserved the judgment layer in engineering or medicine rather than one of several things that did, and the counter-case, that security is too fast-moving for a standard of care to be definable, is not obviously wrong.

The design graph is a proposal. Nothing in this post demonstrates that anyone has built one, that it holds up on a real system, or that it resists becoming the next compliance artifact once someone writes a standard for it. The capability discussion in section 12 rests on where machine reasoning goes next, which is genuinely open; I do not know whether the gap between bounded technical reasoning and architectural reasoning is the next point on a curve or a wall, and neither does anyone else.

### Sources

Links are given where I verified them. Entries without a link are cited by identifier only.

- <span id="r-saltzer"></span>Saltzer, J. H. and Schroeder, M. D., *The Protection of Information in Computer Systems*, Proceedings of the IEEE 63(9), 1975. Least privilege, complete mediation, separation of privilege, and unwanted access paths. [Full text](https://www.cs.virginia.edu/~evans/cs551/saltzer/) &middot; doi:10.1109/PROC.1975.9939
- <span id="r-nist160"></span>Ross, R., Winstead, M. and McEvilley, M., *Engineering Trustworthy Secure Systems*, [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), November 2022. Systems security engineering as a subdiscipline of systems engineering.
- <span id="r-pqc"></span>Haridas, J. and Bachman, M., [*PQC in Plaintext: Google Cloud's post-quantum cryptography roadmap*](https://cloud.google.com/blog/products/identity-security/pqc-in-plaintext-google-clouds-post-quantum-cryptography-roadmap/), August 2026, and [NIST IR 8547](https://csrc.nist.gov/pubs/ir/8547/ipd) on the transition from quantum-vulnerable algorithms.
- <span id="r-heartbleed"></span>CVE-2014-0160, the [Heartbleed](https://nvd.nist.gov/vuln/detail/cve-2014-0160) buffer over-read in OpenSSL's TLS heartbeat extension, disclosed April 2014. NVD base score 5.0 Medium under CVSS v2, later 7.5 High under v3.1.
- <span id="r-corpus"></span>Hurst, R., [*FIPS 140-3 validation, in practice*](https://rmhrisk.github.io/fips-140-3-corpus/), 2026. A near-census of 415 validated modules read from the public CMVP record, covering what the boundary excludes, how the certified state ages, and validation timelines.
- <span id="r-optimizer"></span>Hurst, R., [*Containing the Optimizer*](https://rmhrisk.github.io/containing-the-optimizer/), 2026. What each isolation primitive actually promises, why containment is the design around the primitive rather than the primitive itself, and why remediability rather than severity sizes the response.
- <span id="r-privsep"></span>Provos, N., Friedl, M. and Honeyman, P., [*Preventing Privilege Escalation*](https://www.usenix.org/legacy/event/sec03/tech/full_papers/provos_et_al/provos_et_al.pdf), 12th USENIX Security Symposium, 2003. Privilege separation in OpenSSH, and the reasoning behind it.
- <span id="r-fips140"></span>NIST FIPS 140-3, *Security Requirements for Cryptographic Modules*. The cryptographic boundary, approved modes, and the operational environment.
- <span id="r-c911"></span>National Commission on Terrorist Attacks Upon the United States, *The 9/11 Commission Report*, 2004, at 417. Security requirements nurturing overclassification and excessive compartmentation among agencies, and the absence of any penalty for failing to share.
- <span id="r-moynihan"></span>Commission on Protecting and Reducing Government Secrecy (the Moynihan Commission), *Secrecy*, 1997, and the [Reducing Over-Classification Act](https://www.govinfo.gov/link/statute/124/2648), Pub. L. 111-258, 2010, whose findings adopt the 9/11 Commission's conclusion.
- <span id="r-tsa"></span>Transportation Security Administration and Department of Homeland Security, [end of the shoe removal requirement](https://www.cnn.com/2025/07/08/travel/tsa-shoes-security-checkpoints), 8 July 2025. Rule implemented nationwide in 2006 following the December 2001 Reid incident; PreCheck members exempt throughout.
- <span id="r-nist37"></span>NIST SP 800-37 Rev. 2, *Risk Management Framework for Information Systems and Organizations*. Acceptance, mitigation, avoidance, and transfer as responses to risk.
- <span id="r-cisa"></span>CISA, [Secure by Design](https://www.cisa.gov/resources-tools/resources/secure-by-design) and the [Secure by Demand Guide](https://www.cisa.gov/resources-tools/resources/secure-demand-guide). Shifting the equilibrium toward customer security outcomes and giving purchasers better questions.
- <span id="r-conway"></span>Conway, M. E., [*How Do Committees Invent?*](https://www.melconway.com/Home/pdf/committees.pdf), Datamation 14(5), April 1968. Organizations are constrained to produce designs that copy their own communication structures.
- <span id="r-bloodhound"></span>SpecterOps, [BloodHound OpenGraph](https://specterops.io/opengraph/) and the [BloodHound documentation](https://bloodhound.specterops.io/get-started/introduction). Attack-path analysis over identities and privileges, extended beyond directory services.
- <span id="r-joern"></span>[Joern](https://docs.joern.io/) and the [Code Property Graph specification](https://cpg.joern.io/), after Yamaguchi, F. et al., *Modeling and Discovering Vulnerabilities with Code Property Graphs*, IEEE S&amp;P 2014.
- <span id="r-codeql"></span>GitHub, CodeQL. Extracting a queryable representation of code including syntax, control flow, and data flow.
- <span id="r-otel"></span>OpenTelemetry, service graph generation from observed traces.
- <span id="r-munichre"></span>Munich Re, cyber risk publications. Claims history, anticipated exposures, and adjustment of underwriting and risk modelling as threats change.
- <span id="r-marsh"></span>Marsh, cyber insurance market commentary. Underwriter scrutiny of aggregation risk and AI exposure in a softening rate environment.
- <span id="r-anthropic"></span>Anthropic, [Measuring LLMs' impact on N-day exploits](https://www.anthropic.com/research/n-days), June 2026. Firefox and Windows kernel evaluations, and the collapse of the reverse-engineering bottleneck.
- <span id="r-phantomb"></span>Shostack, A., *PHANTOM-B: A STRIDE Analog for LLMs*, [whitepaper](https://shostack.org/resources/whitepapers) and [Black Hat USA 2026 talk](https://shostack.org/blog/phantom-b-talk-summary/). A threat-elicitation tool for the LLM-specific parts of a system, designed to complement STRIDE rather than replace it.
