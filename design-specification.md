# Design specification

The rules behind [`index.html`](index.html). Change the page to fit these rules, or change these rules on purpose and record why in the [audit log](audit-and-validation.md). Never let the two drift apart.

Version: 1.1, 7 October 2026.

## 1. Purpose

| Question | Answer |
| --- | --- |
| What must visitors understand first? | SimpleX is the first network without user IDs. Not a phone number, not a username, not even a random one. |
| What must they find immediately? | One way to get the app, and proof that the claim is true. |
| The journey | Claim → see it working → see how others identify you → check the proof → read independent voices → get the app. |
| Success | A visitor installs SimpleX, or leaves able to explain the difference in one sentence. |

## 2. Design thesis

**The idea is bigger than "a private messenger".** It is a network where nobody has an identity. The page sells that shift with conviction and then earns trust with evidence.

The experience should feel new, calm and certain. It should not feel like hype. This audience distrusts marketing and checks claims, so every moment of expression must be backed by something they can verify.

Choices that follow from this:

- A type-led hero. No stock imagery. A globe or a network of glowing lines says "technology"; it does not say "no identity". The one image is embossed into the background: gravitational waves from two black holes spiralling together, rendered in code. Waves spreading out from a centre that has no body in it is the closest picture we have found for a network with no identity at its centre.
- A live demo that makes the claim visible: what you see, what the server sees, what they see.
- Evidence in the same visual language as the claims, so proof never looks like an afterthought.

The main tradeoff: a dark, type-led page feels premium but can feel cold. The chat bubbles in the demo carry the human warmth. Keep them.

## 3. Audience

| Visitor | What they need to trust | How the page answers |
| --- | --- | --- |
| Privacy-conscious newcomers leaving WhatsApp or Telegram | Plain language, a clear difference, an easy install. | Hero line, demo, store badges. |
| The privacy community (readers of Privacy Guides, Whonix, Kuketz Blog) | Independent sources and accurate limits. | Proof grid, verbatim quotes, limits stated beside claims. |
| Developers and self-hosters | Source code, specs, verifiable builds, servers they can run. | Open source, Run your own, Verifiable builds, protocol links. |
| People on low-end phones or filtered networks | A fast page that works anywhere. | One 41KB image, one small font file, no third-party requests, works without JavaScript. |

## 4. Page structure

Each section answers one question and hands on to the next.

| # | Section | Visitor question | Content rules |
| --- | --- | --- | --- |
| 1 | Hero | What is this? | One headline, one lede, one primary action ("Get SimpleX"), one proof line of three links. Behind them, the embossed wave image, faded so no text sits on its brightest area. |
| 2 | Demo | Is it real? | Three columns: your phone, the server, their phone. Server shows only queue addresses and ciphertext, then "Sender unknown, Recipient unknown, Content encrypted". Caption labels it an illustration and states the limit (private routing protects IP addresses from destination servers). Pause button. |
| 3 | The difference | How is it different? | Ledger of what identifies you on each kind of network, ending "SimpleX: Nothing." Full five-point comparison behind a disclosure, labelled as SimpleX's own. |
| 4 | The shift | Why does it matter? | Two "then" cards, one "now" card. |
| 5 | Proof | Can I check it? | Six facts in a 3 x 2 grid. Each has a short headline, one sentence, one source link. |
| 6 | Independent reviews | Who else says so? | Verbatim quotes only, attributed and linked. Further coverage as a source line. |
| 7 | Get the app | Where do I get it? | Closing line, store badges, direct downloads (desktop, APK from GitHub, iOS beta). |
| — | Footer | Where is everything else? | Concept notice, privacy statement for the page itself, links to source, security, transparency, build verification, privacy and blog. |

Navigation: Why, Proof, Reviews, Guide, and a "Get SimpleX" pill. On phones only the pill shows.

## 5. Copy and voice

- Short sentences. Plain words. One idea per line.
- Headlines in two halves: a statement in full white, a turn in the dimmed colour ("Check everything. That's the point.").
- Use SimpleX's own wording for product claims where it exists ("The first network without user IDs").
- No superlatives without a source. No "unbreakable", "military-grade" or "100% private".
- Never say there are no servers. Say the servers never learn who you are.
- SimpleX is not peer-to-peer. Never describe it as such.
- No em dashes in page copy.

## 6. Evidence rules

These rules are what make the page credible. They are not optional.

1. Every product claim links to a primary source: simplex.chat, its docs, its release notes or its code.
2. Self-published comparisons are labelled as such ("SimpleX's own comparison, not independently verified").
3. Third-party quotes are verbatim. Trims are marked with an ellipsis. The publisher is named and linked. Context the publisher gives (for example, Whonix ordering by usability with Whonix) goes in the caption.
4. No invented numbers, testimonials, endorsements or users.
5. Example identifiers are fictional and labelled illustrative. The phone number is from Ofcom's drama range (07700 900xxx).
6. Limits sit beside the claim they limit, not in a footnote elsewhere.
7. Recheck every source before each release. Record the date in the audit log.

### Source register

| Claim on the page | Source | Checked |
| --- | --- | --- |
| First network without user IDs; servers cannot see who you talk to | simplex.chat home page | 6 Oct 2026 |
| Comparison against Signal, XMPP/Matrix and P2P | simplex.chat/docs/simplex.html, "Comparison with other protocols" | 6 Oct 2026 |
| Trail of Bits reviews, 2022 (library) and 2024 (protocol design) | SimpleX blog posts of 8 Nov 2022 and 14 Oct 2024; simplex.chat/security/ | 6 Oct 2026 |
| Quantum-resistant end-to-end encryption, v5.6 | SimpleX blog, 23 Mar 2024 | 6 Oct 2026 |
| Private message routing on by default, v6.0; protects IP addresses from destination servers | SimpleX blog, 14 Aug 2024 | 6 Oct 2026 |
| Verifiable builds | simplex.chat/reproduce/ | 6 Oct 2026 |
| Anyone can run a server | simplex.chat/docs/server.html | 6 Oct 2026 |
| Privacy Guides quote | privacyguides.org, real-time communication, SimpleX Chat | 6 Oct 2026 |
| Whonix quote and ordering note | whonix.org/wiki/Chat, Recommendation | 6 Oct 2026 |

Verified but deliberately not used: the 2024 investment from Jack Dorsey and Asymmetric Capital Partners (funding is not proof of privacy), and "tens of millions of messages a day" (self-reported, no method published).

## 7. Typography

**Manrope**, SIL Open Font License 1.1. It is the body face of simplex.chat, so the page reads as SimpleX. SimpleX's site uses GT Walsheim for headings; that font is commercial and is not shipped here. SimpleX could swap it in for headings under its own licence.

The font is subset to the characters on the page, limited to weights 400 to 700, and embedded as text in [`assets/manrope.css`](assets/manrope.css) (about 12KB). This keeps the repo free of binary files and the page free of third-party requests. Loading fonts from Google would send every visitor's IP address to Google, which this audience would rightly object to (LG München I, 3 O 17493/20, 20 January 2022).

**When copy changes, regenerate the subset**, or new characters fall back to the system font:

```
pyftsubset Manrope[wght].woff2 --text-file=page-characters.txt --flavor=woff2 \
  --layout-features='kern,liga,calt,tnum' --output-file=manrope-sub.woff2
python3 -c "from fontTools.ttLib import TTFont; from fontTools.varLib import instancer; \
f=TTFont('manrope-sub.woff2'); f=instancer.instantiateVariableFont(f,{'wght':(400,700)}); \
f.flavor='woff2'; f.save('manrope-400-700.woff2')"
```

Then base64-encode the result into `assets/manrope.css`. For translated versions, add the Latin Extended, Cyrillic and Greek ranges; Arabic and CJK fall back to system and Noto fonts.

System monospace (`ui-monospace`, SF Mono, Menlo, Consolas) is used only for technical artefacts: the server log, example identifiers and the then/now labels.

| Role | Size | Weight | Notes |
| --- | --- | --- | --- |
| Hero headline | clamp(56px, 10.5vw, 156px) | 600 | Line height 0.92, tracking -0.055em |
| Section headline | clamp(40px, 6.4vw, 92px) | 600 | Line height 1, tracking -0.045em, max 14em wide |
| Proof fact | clamp(28px, 3vw, 40px) | 600 | |
| Quote | clamp(20px, 1.9vw, 26px) | 400 | Line height 1.4 |
| Lede | clamp(18px, 1.6vw, 22px) | 400 | Max 30em wide |
| Body | 16 to 18px | 400 | Line height 1.6. Never lighter than 400. |
| Labels, captions | 13 to 15px | 400 to 600 | |

## 8. Colour

One dark canvas, one accent. Contrast measured against `--bg`.

| Token | Value | Role | Contrast |
| --- | --- | --- | --- |
| `--bg` | #05070C | Page background | |
| `--bg-2` | #0A0E17 | Server panel | |
| Wave highlight | up to #4A6682 | Brightest crest of the hero image | Text over it stays at or above 4.5:1 (3:1 for the headline), measured per element |
| `--line` | #1A2233 | Hairlines and grid rules | Decorative |
| `--text` | #F3F6FA | Headlines, key text, primary button | 18.6:1 |
| `--soft` | #A7B1C4 | Body copy, secondary links | 9.3:1 |
| `--faint` | #7D889E | Labels, captions, sources | 5.7:1 |
| Dimmed headline half | #5E6A88 | Second half of headlines | 3.7:1, large text only |
| `--accent` | #4FC3FF | Kickers, "Nothing.", focus ring, your chat bubbles | 10.2:1 |
| `--accent-ink` | #04121C | Text on accent bubbles | 9.6:1 on accent |

Use the accent sparingly: one or two moments per section. Never use it for body text.

## 9. Layout and spacing

- Content width up to 1240px, gutters clamp(20px, 5vw, 72px).
- Sections separated by a hairline and clamp(96px, 14vw, 180px) of space.
- Grids are drawn with hairlines, not boxes or cards: three columns for the demo, shift and proof, two for quotes.
- Below 860px every grid becomes one column, the ledger rows stack, and the nav shows only the "Get SimpleX" pill.
- Wide tables (the full comparison) scroll inside their own container; the page never scrolls sideways.

## 10. Motion

Motion explains; it never decorates. The hero image does not move.

- The demo plays once: each message appears on your phone, the server logs noise, then it arrives on theirs. After three messages, "Be no one." brightens from dim to full white. The server keeps logging noise slowly.
- A thin accent line sweeps the server panel.
- A "Pause animation" button stops all of it (WCAG 2.2 SC 2.2.2). It appears only when JavaScript runs and motion is allowed.
- With reduced motion, everything shows at once and nothing moves.
- Without JavaScript, the headline and every chat bubble are visible.

## 11. Components and states

| Component | States |
| --- | --- |
| Primary button (pill, white on dark) | Default, hover (lifts 1px), active, focus ring |
| Nav pill | Default, hover (border brightens), focus |
| Text links | Underline in hairline colour; brightens on hover |
| Proof line links | 44px tall tap area, underline at the base |
| Fact links | 44px tall, underline |
| Full comparison | Closed (+), open (−), keyboard operable (native details/summary) |
| Pause button | "Pause animation" and "Play animation" |
| Focus | 2px accent ring, 4px offset, on every interactive element |

## 12. Accessibility

Target WCAG 2.2 AA. Checks done are recorded in the audit log.

- Semantic landmarks: header, nav, main, sections labelled by their headings, footer.
- One h1. One h2 per section, including a visually hidden one for the demo.
- Tables for tabular data (ledger, comparison) with row headers and captions.
- The animated server log is hidden from screen readers; the "Sender unknown, Recipient unknown, Content encrypted" summary is read instead.
- Tap targets at least 44px, except links inside sentences, which WCAG exempts.
- Skip link to main content.

## 13. Performance and privacy of the page itself

- One image in the hero: the gravitational wave render, a 41KB WebP at assets/gravity-waves.webp. It is generated by [assets/gravity-waves.py](assets/gravity-waves.py); rerun that script to change it. The only other images are three small SVG badges at the bottom.
- One stylesheet with the embedded font (about 16KB), styles and script inline in the page.
- No trackers, no analytics, no cookies, no third-party requests. Keep it that way: the page must practise what it describes.

## 14. Open questions for SimpleX

1. "Be no one" is bold. Test it against "Talk to anyone. Stay unknown." with newcomers.
2. Should the page say more about what servers can still observe (timing, connection metadata) and how private routing and Tor reduce it?
3. Should funding (Jack Dorsey, Asymmetric, Village Global) appear on an investor-facing version?
4. Swap in GT Walsheim for headings under SimpleX's licence?
