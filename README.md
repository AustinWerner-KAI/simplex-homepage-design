# SimpleX Chat — homepage design concept

A spacious, imagery-led homepage proposal for [SimpleX Chat](https://simplex.chat/), helping newcomers understand private messaging, inspect its evidence and start a conversation.

**Status:** independent design study. 6 October 2026: first coded homepage ([index.html](index.html)), responsive from 390px up, with a dark sovereignty hero and a light page below. Not an official SimpleX release.

![Coded homepage v1, desktop](renders/coded-v1-desktop.jpg)

Earlier raster mockups: [homepage-desktop.png](homepage-desktop.png) (4 October baseline) and [homepage-desktop-mobile.png](homepage-desktop-mobile.png) (archived).

## Design philosophy

The redesign follows **legible agency**: help people understand the offer, interpret meaningful evidence, choose an action and know what to do next. This is a working design synthesis used by the kings-of-website-design workflow, not a validated universal theory.

The experience should feel technically credible without requiring technical expertise. Preserve SimpleX's globe, luminous connections and detailed network imagery; give those visuals room; use precise, short explanations; and make deeper evidence accessible through descriptive links. Space should explain grouping rather than merely increase page length.

Don Norman's discussion of [signifiers](https://jnd.org/signifiers-not-affordances/) informs the labeled network illustration, visible Menu label and outcome-oriented download actions: people need interpretable cues about what a product does and how to act. The structure and spacing choices here are design judgments, not experimentally demonstrated conversion improvements.

Accessibility is part of the intended design quality. Implementation should target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/), including meaningful labels, keyboard operation, visible focus, contrast and reflow. The image does not establish conformance.

## Why this structure is strong

The page follows the visitor's uncertainty: **What is it? → How is it different? → How do I begin? → Why believe it? → Where can I participate? → What next?**

| Section | Visitor question | Structural strength |
| --- | --- | --- |
| Hero | What is this, and how do I get it? | Names private chat, explains invitation-based connection and makes Download the strongest action. The globe carries the brand character without competing with the copy. |
| Network explanation | What does the architecture mean for me? | Pairs local contacts and profile-identifier language with labeled devices and relays. The illustration is an explanation rather than decoration. |
| Start a conversation | What will I actually need to do? | Groups three concrete steps together, beside an illustrative app preview, with a guide for detail. |
| Security evidence | What has been examined? | Separates report years and review scopes, provides direct paths to findings and places the qualification beside the evidence. |
| Directory | Where can I find people? | Offers a clear directory entry point. Suggested category labels demonstrate navigation without inventing named communities or usage figures. |
| Roadmap and support | Where is the project going, and how can I help? | Keeps future plans concise and funding secondary to the product journey. |
| Final download | Am I ready to try it? | Repeats the useful action after explanation and proof, without introducing a new pitch. |
| Footer | Where is the supporting information? | Groups product, trust and project destinations; supporting destinations stay grouped. |

## Quality decisions

- Blue/cyan identity and luminous network imagery preserve recognisability.
- Quiet surfaces behind text, consistent alignment and fewer decorative elements reduce competing signals.
- Technical quality comes from named evidence, accurate scope, understandable architecture and accessible detail—not unsupported security superlatives.
- Desktop groups related copy and controls with a consistent editorial grid; mobile recomposes the same groups in one column.
- Supporting information stays available through Guide, security findings, privacy, transparency and source-code routes.

## Evidence and provenance

The 2022 report examined the **simplexmq cryptography and networking library**, with other areas explicitly outside its scope. See the [2022 SimpleX announcement](https://simplex.chat/blog/20221108-simplex-chat-v4.2-security-audit-new-website.html).

The 2024 report reviewed the **cryptographic design of protocols** used by the network and applications. It is not equivalent to a comprehensive implementation audit of every current release. See the [2024 SimpleX announcement](https://simplex.chat/blog/20241014-simplex-network-v6-1-security-review-better-calls-user-experience.html).

These are historical review references, not a claim that they are the latest available assessments. Before implementation, check the current security documentation and link to the report versions and findings.

The mockup was generated and iteratively edited with OpenAI's built-in image generation tool. SimpleX imagery and branding were recreated from public website screenshots as design references; these are not extracted production assets. The app conversation is illustrative. Directory categories are proposed, not verified live categories. Third-party names and marks remain associated with their respective owners; this project does not assert endorsement or grant rights to those assets.

## Handoff

- [Design specification](design-specification.md): typography, spacing, responsive composition and interaction requirements.
- [Audit and validation](audit-and-validation.md): findings addressed and remaining checks.
- [Generation brief](generation-brief.md): reproducible creative direction.

The final typography critique is incorporated in the implementation specification. Onboarding explicitly includes link and QR-code invitations, consistent with the [Quick start guide](https://simplex.chat/docs/guide/readme.html#connect-to-friends). The raster mockup still cannot guarantee exact fonts, text sizes, contrast, responsive behavior or working links.

## Current direction

Coded page, mobile and desktop. The hero leads with sovereignty: no user identity, no central server, data on your device. The globe image sets a dark hero band; the rest of the page uses the light palette. Earlier note: desktop website only. The primary mockup uses deep ink text, cobalt actions, blue links and clean ice-blue surfaces. The earlier desktop/mobile image remains as an archived iteration. Color values are implementation targets, not measured raster values.

## Latest audit

See [coded homepage v1 audit](audit-and-validation.md#coded-homepage-v1-audit--6-october-2026): D01, D02, D03 and D06 closed in code; D05 open (image rights); D07 to D09 new.

## Earlier desktop audit

The modern-blue desktop mockup is the current visual baseline. The [latest audit](audit-and-validation.md#current-desktop-audit--4-october-2026) records six open refinements: distinct colour roles, consistent lower-page spacing, differentiated heading weights, precise diagram callouts, approved original imagery and a simpler final download row. Each finding includes priority, remedy and acceptance criteria. The [design specification](design-specification.md#next-desktop-refinement-requirements) incorporates these requirements. They are documented next steps, not completed image edits.
