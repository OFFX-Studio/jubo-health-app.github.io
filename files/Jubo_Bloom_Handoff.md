# Jubo Viva — Project Handoff Brief

*A snapshot of the concept, every decision made, and the open questions — so this can be picked up cleanly in Cowork.*

> **⚠️ Rename (2026-07):** product renamed **Jubo Bloom → Jubo Viva**. "Bloom" collided with **Pikmin Bloom** in the same wellness-game space (trademark risk). "Viva" = *alive / living*, which fits the "your body feeds a living creature" slogan. Verb-taglines reworded (blooms → *comes alive*; "Keep it blooming" → *Keep it alive*; "Bloom together" → *Thrive together*). Premium tier: **Bloom+ → Viva+**. Note: files are still named `jubo_bloom_*` but all in-content branding is Viva. (Heads-up: there's also a smartphone brand "vivo" — worth a TM check.)

---

## One-line concept

**Jubo Viva** is a direct-to-consumer (B2C) gamified wellness app where real health signals — a face scan, steps, sleep, mood — are the *fuel* that grows a little creature companion named **Bobo**. Slogan: **"Your heartbeat brings a little creature to life."** (ZH: 你的心跳，喚醒一隻小夥伴.) Show up for yourself, and Bobo comes alive.

> *Note:* avoid the earlier "your body feeds a living creature / 餵養一隻活生生的生物" phrasing — in Chinese it read as something being eaten. Frame it as vitals/heartbeat *bringing the creature to life*, not feeding it.

It's a consumer companion to Jubo's B2B platform, powered underneath by Jubo's clinical data and care AI.

**Strategic framing (important):** Jubo (智齡科技) is B2B long-term-care SaaS — verified from jubo-health.com: **2,700+ care facilities, 330,000+ professional users, 3B+ (30億) care records**; investors/partners include Wistron (緯創) and Compal Health (仁寶健康科技, 2025 merger → internationalization + capital-markets push). Jubo already ships family-facing pieces (**安心寶 / FamilyLine**, 家庭聯絡簿 AI) and runs a **care-facility matching platform**. **Pitch order (matters):** lead with Bloom as a real consumer business on its own merits — freemium wellness-game economics (free base → cosmetics micro-txns + Viva+ subscription + content/insurer/pharma partnerships). THEN present value-back-to-Jubo as a *multiplier on top*, not as the primary justification. (Earlier "it doesn't need to profit / self-sustaining" framing was rejected as weak.) The strategic upside back to the B2B core: (1) consented consumer signals sharpen Jubo AI, (2) top-of-funnel reaching families before institutional care → feeds the matching platform + B2B pipeline, (3) extends the care continuum upstream to aging-at-home/prevention, (4) public brand + family trust that strengthens B2B sales and the Compal/capital story.

---

## How we got here (discussion arc)

1. **Started from a feature screenshot** — a health app built on AI measurement (contactless facial scan for blood pressure + heart rate), with required features: (1) 10-sec face measurement, (2) history & trends. Plus device integration, sharing, and a professional network.
2. **Researched trending health/wellness apps** in Asian markets and by archetype (companion, gamified self-care, habit, AI journaling).
3. **Clarified the business framing**: this is a proposal *to Jubo* for a **new B2C app** — Jubo is B2B (eldercare SaaS, 2,700+ facilities). The consumer app leverages Jubo's clinical data + care AI as an unfair advantage / moat.
4. **Landed on app *type***: not a pure utility (scanners churn), not a pure AI companion (crowded + regulatory risk). Chose **gamified creature-growth self-care** (養成 / Tamagotchi model) — fits the founder's MoodMons DNA and the strongest retention data.
5. **Worked through game mechanics** by referencing: Candy Crush (rejected its coercive energy-gating), Pokémon GO + Pikmin Bloom (adopted their "real activity fuels the game," passive accrual), Finch (shame-free, no punishment for lapses), Mindllama (collect-a-character-per-goal).
6. **Defined the fuel-tier structure** (below).
7. **Named it**: Jubo Viva, creature Bobo. ("Bloom" carries the grow-as-you-care slogan; considered Jubo Hearts but Hearts names an emotion not the growth mechanic, is less ownable, and "hearts" evokes the Candy-Crush lives currency we designed against. "Heart" kept as a *feature* — the 安心 family-sharing gesture: "send a Heart.")
8. **Built a concept-explainer web page** (the final HTML), themed to Jubo's real brand.

---

## The design: fuel-tier structure

**Core principle:** real healthy actions *earn* progress (never gate it). Fuels are **substitutable** — a good day can come from a scan OR a walk OR a mood check-in. No single action is a chokepoint. This is what keeps it gentle (esp. for elderly / anxious users) and avoids coercion.

**Primary fuel — Daily measurement (AI face scan).** The unique, defensible core → biggest payout. One meaningful scan/day, diminishing returns after (guards against compulsive checking + keeps "wellness, not medical device" positioning). The reading shapes Bobo's mood (calm / energized / tired).

**Secondary fuel — Activity & sleep.** Steps, calories, sleep read passively from Apple Health / Google Fit (Pikmin-style — accrues even when app is closed). Covers days a scan is skipped.

**Tertiary fuel — Mood & breathing.** One-tap mood check-in (Daylio-style) + optional breathing (Mindllama mechanic). Shame-free: a low mood brings Bobo's *care*, never disappointment.

**Secondary tasks (lighter payout):**
- *Tiny AI companion* — Bobo reacts + gives a plain-language nudge. Deliberately small to stay clear of companion-app regulatory risk (Replika, Character.AI).
- *Family check-in (安心)* — one gentle daily touch (Pikmin-postcard model). This is the "send a Heart" gesture. Maps to Jubo's eldercare world (adult child sees "mum scanned + walked, Bobo is happy").
- *Read a health article* — small daily fuel, Jubo-curated → credibility + content-partnership revenue seam.

**Progression (hybrid):** ONE main creature (Bobo) you bond with and grow continuously (Finch warmth) + a **collectible cast** unlocked through consistency/streaks (Mindllama pull). Characters earned by showing up, **never** a paid loot-box. Money (if any) = cosmetics only.

> **⭐ Core mechanism = 水族箱 (living tank / aquarium).** (2026-07 pivot.) The container for the whole creature system is an aquarium: Bobo + all kinds of creatures (blobs, fish, koi 錦鯉, turtles 龜) live in one tank. **Your vitals maintain the WATER, not "feed" a creature** — scan → clarity/oxygen, steps → current, sleep → light, mood → warmth. Healthy you = clear water = thriving tank. Chosen because: (1) 水族箱/養魚 is a deeply familiar 熟悉題材 for Asian/elderly users (zero learning curve), (2) longevity symbolism (龜/錦鯉 = 長壽) fits a health app, (3) **fish never die** = the no-punishment guardrail + longevity promise in one, (4) watching fish genuinely lowers stress/BP — the calm-water metaphor literally echoes what AI measurement measures, (5) family **共養 a shared tank** = the 安心 layer perfected (everyone's healthy days keep one tank sparkling; one glance = peace of mind), (6) production-lean — one reusable tank scene + procedural creatures (blob + fish shapes from the existing generator) + 2D drift animation (cheaper than legged creatures). Distinguishes from Finch (single pet) and Water Llama (flat sticker-unlock) by being a *shared living space*. Standalone mockup: `jubo_viva_aquarium.html` (portrait phone, tank as a rect banner). Integrated into concept page as the `#tank` section (first section after hero) + slogan refined to "Your heartbeat brings a little world to life" / 你的心跳，喚醒一整缸小夥伴.

**Core loop:** real actions → fuel → Bobo grows + unlock characters → share & streak → back around.

---

## Design guardrails (what keeps it healthy, not manipulative)

- **Not Candy Crush** — measurement *earns* energy, never gates it. Never locked out of your own health data.
- **Not a companion trap** — the AI stays tiny; a reactive creature, not an attachment-maximizing chatbot.
- **Pikmin-gentle** — passive accrual, no punishment for lapses; Bobo waits patiently.
- **Wellness, not medical** — AI-measured BP is screening-grade (±5–12 mmHg), NOT diagnostic. Frame as trend-tracking with cuff confirmation. Critical for regulatory positioning in Taiwan / Japan.

---

## Brand & visual direction

- **Name:** Jubo Viva (family-parallel with Jubo Link). **Creature:** Bobo (friendlier than the alternative "Nubo"; swap is a 2-word change if needed).
- **Palette — pulled from Jubo's real site (jubo-health.com):** LIGHT and airy, not dark. Near-white background washing into pale sky-blue + mint gradients. Signature teal **#00b2c0** used sparingly as accent. Soft lavender (**~#8f9bff**) echoes Jubo's headline purple. Deep teal-ink text (**#123039**). White cards with soft shadows.
  - *Note:* an earlier dark-teal version was wrong — Jubo's actual mood is light/bright/lots-of-whitespace. The final HTML is the corrected light version.
- **Bobo sprite:** currently a hand-coded inline-SVG pixel creature (teal body, navy shading, warm belly-glow, pink cheeks, leaf sprout). It's a **placeholder** — founder is a strong pixel/generative artist and should replace it with real MoodMons-style art.

---

## Deliverables in this handoff

- `jubo_bloom_concept.html` — the full concept/proposal page (light Jubo theme, Jubo Viva / Bobo branding). Now a complete product proposal, not just a mechanics explainer. Sections: hero → fuel engine → secondary tasks → progression → core loop → **what it looks like (5 phone screens)** → **family check-in · 安心 (tap-only card system)** → guardrails → **business model + data flywheel** → **trust & privacy (TW PDPA / JP APPI)** → **stage-gate funding roadmap**. Hero wordmark refined (cleaner bloom-sprout glyph + ™).
  - **安心 tap-card system:** no free text. Predefined bilingual cards grouped as 問候/greetings, 關心/care, 提醒/reminders, plus one-tap 回應/replies. Gamification wiring: every tap = a Heart (feeds both creatures), reminder→reply same-day = shared streak (親情連線), family-streak milestones unlock *shared* cosmetics. Accessible for elderly + dodges the companion-chatbot regulatory risk.
  - **Payment model (studio-friendly):** the earlier KPI-gated investor "tranches" were rejected — they tied the studio's pay to user metrics (retention etc.) the studio can't control. Replaced with a standard delivery-milestone payment schedule: **首款 Down 35% (NT$1.05M, on signing) → 驗證款 Validation 30% (NT$900k, on validated core delivered: AI measurement+tank+scan+Bobo tested) → 上線尾款 Launch 35% (NT$1.05M, on App Store launch)**. Plus a lightweight **Viva+ payback estimate** in the budget section (keys pb1–pb4): pricing US$6.99/mo · US$69.99/yr; ~1,600 yearly subscribers recoups the NT$3M build in year one net of ~15% platform fee. Payments release on deliverables the studio controls, NOT KPIs. Then an ongoing **營運 retainer** (content + 維運) post-launch; the data-flywheel/scale phase is a separate Jubo-funded follow-on. %/amounts are placeholders. (roadmap section = pf1–pf13.)
  - **Live service · 持續營運:** section on continuous content (art/creatures/seasonal, articles, tech 維運) + extendable **mini-game slots** (Breathe with Bobo/mind, Step Garden/activity, Memory Match/cognition + open slot), each tied to a fuel. Framed as the studio's recurring revenue line.
  - **Budget = NT$3M total / 8 months (保守時程 = conservative schedule), DEVELOPMENT ONLY.** Team = **2 developers + designer + artist** (the second dev is what lets the same NT$3M deliver in 8 months instead of 12, and removes the solo-dev bottleneck/key-person risk). Allocation: Engineering (2 devs) NT$1.6M (53%), Design NT$520k (18%), Art NT$480k (16%), Overhead & tools NT$400k (13%) = NT$3.0M. Explicitly EXCLUDES online/infra (維運) and marketing (both separate budgets); AI measurement = provided by Jubo at no cost. Budget section (bilingual keys b1–b13).
  - **Marketing + budget:** phased go-to-market (owned Jubo facility/family channel as the low-CAC unfair advantage → community/KOL → paid/partners → always-on) + channel mix + two indicative budget allocation frameworks (build/operate, marketing spend). Numbers are placeholders.
  - **"A day inside Jubo Viva"** rebuilt: the 5 walkthrough screens now use the same polished device frame as the collection phone (light-blue frame, status bar, rounded screen). Home + Collection screens render procedurally-generated Bobos. Now fully bilingual (keys a1–a15) — previously this whole section silently stayed English because an inline SVG made the translator skip it.
  - **Character collection section** (after "progression"): a Mindllama-style in-app collection screen — featured breath card, tabs (Characters/Outfits/Habitats/Themes), 30-slot grid (11 collected + locked silhouettes), "Collect character" button, plus a "content engine" explainer (same Bobo → endless skins/accessories = studio's ongoing 營運 output; cosmetics-only). Creatures are **procedurally drawn** from one pixel Bobo base via a second `<script>` (palettes + accessory system: leaf/cap/beanie/sun/flower/crown/phones). Standalone version also saved as `jubo_bloom_collection.html`.
  - **EN / 中文 toggle:** the page now has a fixed top-right language switch. (Collection section adds bilingual keys c1–c15 to the `var ZH` map.) Full Traditional-Chinese translation of all 293 text units via `data-i18n` + an inline JS map; default EN. To edit copy later, update BOTH the visible EN and its ZH entry in the `var ZH = {...}` script block near the end of the file.
- `jubo_bloom_sections.pdf` — ⚠️ STALE: was 6 pages of the *earlier* HTML, before the new sections (app screens / business / trust / roadmap) were added. Regenerate from the current HTML before external use.
- `Jubo_Consumer_App_Proposal.pptx` — 5-slide deck pitching Jubo on the B2C app (data-moat → B2C play).
- `Jubo_Contactless_Vitals_Pitch.pptx` — earlier 5-slide deck (institutional/vitals-station framing; superseded by the B2C direction but kept for reference).

---

## Open questions / next steps

- [ ] **Final creature name:** Bobo (current) vs Nubo — confirm.
- [ ] **Replace placeholder Bobo sprite** with real art.
- [ ] **Traditional-Chinese version** of the concept page + decks for the actual Jubo audience.
- [x] ~~**Jubo Viva wordmark**~~ — refined in-page (bloom-sprout glyph). Still worth a standalone lockup file for a designer.
- [x] ~~**Verify Jubo's figures**~~ — confirmed on jubo-health.com (2026): 2,700+ facilities, 330,000+ users, 3B+ (30億) care records. Re-check before each external use as numbers grow.
- [x] ~~**Privacy/consent story**~~ — now a full "Trust & privacy" section (opt-in, anonymized/aggregated, wellness-not-medical, user owns data; TW PDPA / JP APPI). Have counsel review before external use.
- [x] ~~**"Jubo Bloom" trademark risk** (Pikmin *Bloom*)~~ — resolved by renaming to **Jubo Viva**. NEW open item: **check "Viva" TM** (smartphone brand "vivo" exists; confirm no conflict in app/health category in TW/JP).
- [x] ~~Fold the concept into the deck~~ — concept page now stands alone as a full proposal; decide whether to also merge into `Jubo_Consumer_App_Proposal.pptx` or point the deck at this page.
- [ ] **Regenerate `jubo_bloom_sections.pdf`** from the updated HTML (now 9 sections).

---

## Founder context (for whoever picks this up)

Indie developer (handle @magicmonx), builds consumer mobile apps; primary product **MoodMons** (mood-tracking where logged emotions generate creature characters — direct lineage to Bobo). Strong in generative art, creative coding, WebGL/Canvas/pixel-art. Communicates concisely, thinks in game references and analogies, favors clean/understated design over flashy effects. Exploring the Jubo partnership for the AI measurement-based B2C health app.
