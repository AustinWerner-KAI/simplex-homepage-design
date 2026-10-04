# Design specification

## Brief

Product: marketing homepage for a privacy-focused messenger. Primary audience: newcomers, including people without protocol expertise. Primary task: understand the difference, inspect trust evidence, obtain the correct app and connect with someone. Supporting audiences: community participants, developers and supporters.

The tension is adoption versus explaining complex privacy architecture and funding the project. Put download and comprehension first; retain report scope and limitations before commitment; give support a quieter, later position.

## Typography

Use one appropriately licensed sans-serif family with regular, medium and semibold weights. Choose the exact family against SimpleX's established assets before implementation; the raster image does not identify a production font.

| Role | Desktop starting size | Mobile starting size | Treatment |
| --- | --- | --- | --- |
| Hero | 64–72px | 40–44px | Semibold, line-height 1.1–1.2 |
| Section heading | 36–40px | 28–32px | Medium or semibold; lighter emphasis than hero |
| Body and primary links | 18px | 16–18px | Regular, line-height about 1.5 |
| Supporting labels | 14–16px | 14–16px | Regular, readable contrast |

These are starting values, not extracted measurements or universal rules. Keep qualifications readable. Do not reduce mobile type merely to fit the page. Use tabular numerals for report years. Give all links a consistent treatment and purposeful line breaks.

## Layout and visual roles

Use navy for primary text and actions, brighter blue for links and pale sky/white for surfaces. The globe and gold arcs carry expression; their detailed regions should remain away from reading areas. Preserve the isometric network's detail while adding callouts anchored to actual devices and server racks.

Start with a maximum content width around 1200px; desktop horizontal margins around 64–80px and mobile margins around 24px. Use roughly 96–128px desktop section padding and 64–80px mobile section padding where content warrants it. Adjust at intermediate widths instead of enforcing fixed heights. Keep tighter spacing within groups and larger spacing between jobs.

Hero: copy and action on the quiet sky; globe low/right. Network: paired explanation and illustration. Onboarding: heading and steps in one group, app preview beside it. Reports: aligned year/scope/action rows. Directory: meaningful navigation preview with proposed-state labeling. Roadmap: compact summary and detail link. Footer: three desktop groups, vertically stacked mobile groups.

## Interaction requirements for implementation

- Onboarding step 03 reads “Share a link or scan a QR code.” Both invitation routes are described in the [SimpleX Quick start guide](https://simplex.chat/docs/guide/readme.html#connect-to-friends). The concept does not display a fake working code. Any production QR code must encode a verified destination, have an equivalent link and clearly distinguish downloading the app from connecting to a contact.
- Download navigates to a platform-selection page. A device suggestion may help, but all supported platforms remain available. Explain architecture names in ordinary language. Distinguish stable releases from beta builds.
- Links navigate using real URLs and preserve browser history and new-tab behavior. Buttons change state. Do not simulate successful downloads.
- Menu is a named button with expanded state. Support keyboard opening, Escape dismissal, visible focus and appropriate focus restoration. If an overlay is modal, implement the corresponding focus and background behavior.
- Report links identify reviewer, year and scope. Qualification and limitations links remain adjacent to their claims.
- An unavailable download offers a mirror or retry route. Broken directory queries provide a clear recovery path. No invented progress percentages.
- Define default, hover, focus-visible and pressed states for controls. Loading and error states are required only where real asynchronous behavior uses them.

## Responsive and access acceptance

Validate at 390px, an intermediate width such as 768px, and 1280px or wider, plus browser zoom and text expansion. Do not hide decision-critical qualifications on narrow screens. The image's side-by-side presentation is not a responsive implementation.

Use semantic headings and navigation, meaningful image alternatives, descriptive link names and decorative-image handling. Target WCAG 2.2 AA. Check text contrast (generally 4.5:1, or 3:1 for qualifying large text), relevant non-text contrast, keyboard access and reflow. Prefer generous mobile targets, around 44px as a design goal; WCAG's 24px minimum criterion has exceptions and is not the same recommendation.
