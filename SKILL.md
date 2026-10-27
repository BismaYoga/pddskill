---
name: pro-graphic-designer
description: >-
  Studio-grade modern graphic design skill for creating contemporary social media
  visuals (Instagram 4:5 carousels and single posts, 1:1 square, 9:16 stories),
  editorial posters, event flyers, product launches, and news graphics using
  HTML/CSS/SVG and low-memory Playwright rendering. Use this skill whenever the
  user asks to design, layout, revise, or critique a graphic, poster, banner,
  carousel, flyer, or visual social media post.
---

# Pro Graphic Designer (Modern Studio Edition)

Design contemporary, high-taste visual communications that look art-directed by a senior human designer at a modern creative studio—never like generic AI templates or web-developer wireframes.

> **Rule precedence:** If a reference file ever conflicts with this SKILL.md, **SKILL.md wins**. All paths below are relative to this skill folder (`{baseDir}`); run scripts as `python3 {baseDir}/scripts/...`.

---

## 1. Anti-AI-Slop Red Lines (Zero Tolerance)

Every element on the canvas must serve visual communication or spatial tension. Strictly ban these amateur AI clichés:

- **NO Web-UI / Div-Box Posters:** Never build a single poster or Slide 1 cover by stacking bordered `.card` boxes, 3 feature cards, dashboard widgets, or neo-brutalist spec tables. Social media graphics must read instantly at mobile scale, not look like a desktop SaaS wireframe.
- **TOTAL BAN on Bullets, Dots & Status Pills:**
  - Never prepend kickers, tags, or headers with `•`, `●`, or pulsing status dots (`● LIVE`, `● ALERT`).
  - Never wrap category kickers in rounded pill borders/capsules (`[ CATEGORY ]`). Pure tracked typography conveys far greater authority.
  - Never use `•` as a metadata separator. Use clean whitespace alignment, a delicate hairline rule, or minimal `//` / `—` only when structurally needed.
- **NO Fake Clickable Buttons:** Never draw website CTA buttons (`[ DAFTAR SEKARANG ]`, `[ APPLY NOW → ]`) on static graphics. For carousels, use a quiet typographic cue (`Geser →`). For events, replace the button with real metadata (date, venue, handle).
- **NO Floating Clipart Satellites:** Never scatter random 3D coins, shields, bells, or floating social icon bubbles around the hero subject. One hero asset per canvas.
- **NO Corner Clutter:** No decorative corner tags (`REPORT // 2026`, `REF // 09`), fake tech badges, corner checkmarks, or arbitrary labels. Keep only essential anchors: quiet slide counter (`01 / 05`) and swipe cue (`Geser →`).
- **NO Stiff ID/Passport Portraits in News:** Never use blank, static bureaucratic pasfoto for news, policy, or crisis stories. Always use **contextual action photography** (passionate podium gestures, field inspections, authentic motion).
- **NO Hard-Edge Cutouts on Food ("Sticker Effect"):** Never isolate food onto a dark/sterile void. Food relies on macro full-bleed sensory context (natural glaze, steam, wood/stone/linen surfaces, warm ambient light).

---

## 2. Spatial Architecture & Optical Balance

### 2.1 The Spatial Yield Rule (Subject vs. Typography)
Hero imagery and display typography must **yield space to each other**—never freeze a subject at the dead `50%` vertical center and cram text above or below it. Default zones on a `1080 × 1350` canvas:

| Layout | Typography zone | Hero asset zone | `prepare_asset.py` |
| :--- | :--- | :--- | :--- |
| **Top-Anchored Typography** | `Y: 100–480px` | `Y: 520–1310px` | `--zone bottom` |
| **Bottom-Anchored Typography** | `Y: 830–1260px` over a smooth scrim | `Y: 60–780px` (immediate visual magnet) | `--zone top` |
| **Headline + Asset + Card stack** | per §2.6 gap math | between headline and card | `--zone center --top Y1 --bottom Y2` |
| **Asymmetric Split Axis** | tight vertical lockup on opposite side | 60–65% of width on one side | `--align left/right` |
| **Pure Typographic Canvas** | core mass at **Optical Center (42–45% from top)**, never droopy `50%` | — | — |

### 2.2 Optical Equilibrium (Anti-Lopsided Rule)
- **Never** pair a horizontally centered hero asset with a massive left-aligned top headline while leaving the top-right corner empty—minimalist canvases without filler cards will visibly tip left-heavy.
- When the hero asset is centered horizontally, either align the typographic lockup along the **Symmetrical Central Axis** (`text-align: center`) OR shift to a **Bottom-Anchored** full-width editorial lockup.

### 2.3 Safe Margins & Gestalt Proximity
- **Safe Margins:** Enforce `72px–88px` outer side padding on a `1080px` canvas (top edge margin `100–120px`, see §2.6). Never clip or crowd letters near canvas edges.
- **Gestalt Lockups:** Never distribute elements evenly (`space-between` / `space-evenly` across 4+ blocks). Group related thoughts tightly (`10px–16px` gap between kicker, headline, and sub-hook) and leave **35%–50% intentional negative space** separating major zones.

### 2.4 The Quadrant Equilibrium Rule (Anti-Jompang)
Divide the canvas into 4 visual quadrants (Top-Left, Top-Right, Bottom-Left, Bottom-Right):
- **Never leave an entire quadrant as a hollow desert** while the opposite quadrant is overloaded with visual mass.
- If a directional subject (e.g., cybernetic robot arm) enters from Bottom-Left pointing toward Top-Right, the Top-Left must hold the headline lockup, and Bottom-Right must hold the grounding copy to complete the diagonal kinetic counterweight.
- **Bottom Sheet Containment Ratio:** Any bottom sheet or container card must tightly hug its typography (`padding: 48px–56px`). Never leave a 150px–200px blank void at the bottom of a card—this creates a hollow "jompang" bottom.

### 2.5 Negative Space & Asset Harmony (Anti-Crowding & Anti-Occlusion)
Balance is the harmonious relationship between **Asset Mass**, **Text Mass**, and **Negative Space**:
- **Negative Space Equilibrium:** Distribute empty space intentionally. Never trap 60% of the canvas as a dead void at the top while cramming text and asset into the bottom 40%.
- **Asset Integrity & Non-Occlusion:** Never cover, bury, crop, or amputate critical hero assets behind cards or the canvas edge. If an asset overlaps a bottom sheet, it must stay 80%+ visible and elevated above the card with a directional drop shadow.

### 2.6 The Harmonic Vertical Spacing System (Equalized Gap Theorem)
When stacking **Headline → Asset → Card** on a `1080 × 1350 px` canvas, spacing must follow a disciplined rhythm:
- **Never allow extreme gap ratios:** `36px` above an asset and `160px` below it makes the asset look glued to the headline and detached from the card.
- **Standard gap band:**
  - **Top Edge Margin:** `100px – 120px`
  - **Gap A (Headline block → Asset):** `70px – 85px`
  - **Gap B (Asset → Card):** `70px – 85px` *(must equal Gap A within ±10px)*
  - **Card → Bottom Margin:** `60px – 70px`
- **How to hit it exactly:** measure the headline bottom (`Hb`) and card top (`Ct`) in your HTML, then run `prepare_asset.py place-seamless ... --zone center --top $((Hb+78)) --bottom $((Ct-78))`. The script prints `ASSET_BOX ... top=… bottom=…`, which gives you the real gaps to verify.

---

## 3. Typography, Copywriting & Mobile Legibility

### 3.1 Modern Social Editorial Copywriting (The "Scroll-Stopper" Hook)
A poster or carousel lives and dies by its editorial hook. Never write like an academic paper or stiff corporate documentation:
- **Embody the Modern Reader:** Write as an ambitious, curious professional/creator scrolling their feed. The hook must trigger curiosity, FOMO, or a paradigm shift in under 2 seconds.
- **Tension-Driven Hooks:** Use contrast and provocation over bland descriptions:
  - ❌ *Boring/Academic:* "Analisis Fitur Extended Reasoning Pada Model Claude 3.7 Sonnet"
  - ✅ *Punchy & Relatable:* "Claude AI Itu Bukan ChatGPT. Ini Alasan Kenapa Banyak yang Mulai Pindah."
- **Text Economy:** Never force paragraphs where space is tight. Say more with fewer, sharper, jargon-free words.

### 3.2 Type Scale & Legibility Rules
- **Maximum 3 Hierarchy Tiers per canvas:** (1) Micro Kicker/Meta, (2) Hero Display Headline, (3) Editorial Sub-hook.
- **Tight Tracking Requires Word-Spacing Compensation:**
  - Heavy display headlines (`72px–104px`, weight `800–900`) look sharp with tight tracking (`letter-spacing: -2px` to `-3px` / `-0.03em`).
  - **MANDATORY:** Whenever `letter-spacing <= -1.5px`, add **`word-spacing: 8px–12px` (`0.08em–0.12em`)** so uppercase words (`WEBSITE KAMU`) never collide into `WEBSITEKAMU`.
- **Mobile Legibility Floor (`18px` minimum on a `1080px` canvas):** A `1080px` post shrinks ~3× on phones, so `12px–14px` text becomes unreadable `4px` dust. **NEVER set any text below `18px`.**
- **Recommended `1080×1350` scale:**
  - **Hero Headline:** `72px–104px`, `line-height: 0.95–1.02`
  - **Sub-hook / Editorial Serif:** `30px–42px`, `line-height: 1.22–1.32`
  - **Kicker / Counter / Swipe Cue:** `18px–22px`, `letter-spacing: 0.16em–0.22em`
- **Genre-Matched Font Personas:** Pick Google Font pairings and color systems from [agency-design-archetypes.md](./references/agency-design-archetypes.md). Never put aggressive condensed fonts (*Bebas Neue*, *Anton*) on food, luxury hospitality, or clinical healthcare. Details: [typography-and-whitespace.md](./references/typography-and-whitespace.md).

---

## 4. Seamless Asset Blending & Contrast Gate

- **Zero Bounding-Box Seams (Anti-Pasted-Rectangle):**
  - Never paste a square render/photo onto a dark or colored canvas if its background RGB (`#0b0d13`) differs even slightly from the canvas hex (`#050609`)—OLED screens expose faint rectangles immediately.
  - Always compose standalone assets with [`prepare_asset.py`](./scripts/prepare_asset.py) `place-seamless`:
    - **Transparent PNG cutouts** (everything in `assets/3d/` and `assets/people/`) keep their original colors; the script trims empty padding and fits the subject inside the zone—never cropped.
    - **Opaque studio renders** get their backdrop tone clamped to the exact canvas hex plus a smooth super-ellipse feather to zero at every edge.
- **Harmonize the cutout** (black point, color temperature, light wrap, cast shadow) per [asset-centric-design.md](./references/asset-centric-design.md). Optional subtle ambient glow: `--glow 0.12 --glow-color "<accent hex>"`.
- **WCAG 4.5:1 Scrim Protection:** Never place light or thin typography directly over bright sky, sunlit leaves, mist, or busy highlights. Always apply a multi-stop CSS scrim behind text zones (recipes in the archetypes reference).

---

## 5. Instagram Carousel Architecture

### 5.1 Slide Content Rules
- **Slide 1 (Thumb-Stopping Hook Cover):**
  - **Under 15 words total**: clean Kicker + High-Tension Hook Headline (max 3 lines) + 1-line Provocative Sub-hook + quiet Slide Counter (`01 / 05`) & Swipe Cue (`Geser →`).
  - Zero paragraphs, zero step lists, zero data boxes. One monumental hero asset.
- **Slides 2 to N-1 (Editorial Value Breakdown):** Clean Swiss architectural grids, `1px` hairline dividers (`rgba(255,255,255,0.10)` on dark / `rgba(17,18,21,0.12)` on light), oversized index numbers (`01`, `02`), consistent `80px` alignment grid, **maximum 40 words per slide**.
- **Final Slide:** A clear, quiet takeaway plus a bookmark/share cue in typography—never a fake button.

### 5.2 Dynamic Carousel Pacing Wave (Anti-Monotony Directive)
**FORBIDDEN:** Repeating the same layout template (e.g., identical bottom-sheet card) across 3+ consecutive slides. Follow a **visual pacing wave** (adapt colors to the chosen archetype):
1. **Slide 1 (The Hook):** Centered monumental hero asset + punchy headline + zero paragraph clutter.
2. **Slide 2 (The Paradigm Shift / Two-Tone Split):** Dark top (60%) + accent-tinted curved bottom sheet (40%) with the 3D asset overlapping it, casting a deep directional shadow.
3. **Slide 3 (The Mechanics / Isometric Split):** Isometric asset floating in the upper field with dual-column or stepped highlights below.
4. **Slide 4 (Action / Diagonal Kinetic Vector):** Directional asset (e.g., hand interacting with a screen) with cross-diagonal text placement.
5. **Slide 5 (The Grand Climax / Zero-Sheet Release):** Break out of the container. Full-bleed deep canvas, one iconic symbolic sculpture, a masterclass editorial quote, and the quiet bookmark/share takeaway.

---

## 6. Execution Workflow (Low-RAM Safe & Self-Verified)

Follow these 5 steps on every design task.

### Step 1: Memory-Safe Asset Preparation (1GB RAM Guard)
- **NEVER** open raw master images (`>2500px` or `>10MB`) with plain `Image.open()`—this triggers Linux OOM kills (`exit 137`). When downloading from Wikimedia/web APIs, fetch `1280px–1600px` thumbnails.
- Use [`prepare_asset.py`](./scripts/prepare_asset.py):
  - Full-bleed photo cover crop:
    `python3 {baseDir}/scripts/prepare_asset.py cover <input_img> <output.jpg> --width 1080 --height 1350 --focus top`
  - Seamless studio placement (Spatial Yield + zero seams):
    `python3 {baseDir}/scripts/prepare_asset.py place-seamless <asset> <canvas.jpg> --zone bottom --bg "#050609"`
  - Precise placement between headline and card (§2.6):
    `python3 {baseDir}/scripts/prepare_asset.py place-seamless <asset> <canvas.jpg> --zone center --top 470 --bottom 930 --bg "#050609"`
  - Split layouts: add `--align left|right`; vertical anchoring inside the zone: `--anchor top|center|bottom`.
- Use the resulting JPG as the full-canvas `background` of the HTML so asset and canvas share one exact hex.

### Step 2: Compose Modern HTML/CSS Canvas
- Consult [agency-design-archetypes.md](./references/agency-design-archetypes.md) to pick an archetype that suits the topic's emotional psychology (never reuse the same skeleton across unrelated niches).
- Lock `html, body` to exact dimensions (`1080 × 1350` for 4:5, `1080 × 1080` for 1:1, `1080 × 1920` for 9:16) with `margin: 0; overflow: hidden`.

### Step 3: Render Pixel-Perfect PNG via Helper Script
- Use the low-memory renderer (do NOT write ad-hoc Playwright scripts):
  `python3 {baseDir}/scripts/render_graphic.py <input.html> <output.png> 1080 1350 --preview`
- The renderer waits for webfonts and images, then prints an **automatic `AUDIT:` report** (text < 18px, text inside the 72px side margin or clipped, banned `•`/`●` glyphs). **Every AUDIT issue must be fixed and re-rendered.**

### Step 4: Export True Figma-Editable SVG
- Create a standalone `.svg` (`viewBox="0 0 1080 1350"`) alongside the PNG.
- **Figma Compatibility Rule:** Figma ignores `@import url(...)` inside `<style>`. Set `font-family`, `font-weight`, `font-size`, `letter-spacing`, and `fill` **directly as XML attributes** on `<text>` / `<tspan>` (template in [agency-design-archetypes.md](./references/agency-design-archetypes.md)).

### Step 5: MANDATORY Visual Self-Critique Gate (Before Replying!)
**NEVER send a design blind.** After rendering, **view the generated PNG/preview** and audit it against these 9 criteria:
1. **Zero Slop:** No `•` bullets/dots, pill capsules, fake buttons, floating clipart, or UI window titlebars?
2. **Word Spacing & Margins:** No collided uppercase words (`WEBSITEKAMU`), `>= 72px` side margins, and a clean `AUDIT` line?
3. **Seamless Blending:** Zero visible rectangular seam/box around the hero subject?
4. **Negative Space & Harmonic Spacing:** Gap above the asset equals the gap below within ±10px (no 30px vs 160px)? Empty space intentional, no dead voids or hollow quadrants?
5. **Asset Visibility & Integrity:** Is the hero asset fully celebrated—not cropped, covered, or suffocated behind containers?
6. **Reader Empathy & Hook Strength:** Would a modern human stop scrolling? Is the headline punchy and conversational, not a stiff textbook or robot translation?
7. **Clean Canvas:** Corners free of metadata noise (fake report tags, checkmarks)? Focus 100% on what matters?
8. **Text Economy & Pacing:** Copy concise and easy to digest? Carousel layouts varied per the pacing wave?
9. **Mobile Contrast & Scale:** All copy `>= 18px` and crisp (`>= 4.5:1` contrast)?

If **any** check fails, revise the HTML/CSS or asset placement and re-render until the graphic is truly publication-grade.
