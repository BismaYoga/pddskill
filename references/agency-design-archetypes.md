# Contemporary Studio Design Archetypes & Figma SVG Reference

Curated modern design systems inspired by contemporary creative studios (Pentagram, Linear, Apple Editorial, Kinfolk, Nike Brand Studio, and modern visual newsrooms). Zero UI-slop, zero fake buttons, zero bullet/pill clutter.

---

## 1. Six Modern Studio Archetypes

### Archetype A: Dark Precision Tech & Cybersecurity (Linear / Apple Pro Aesthetic)
- **Best For:** Software engineering, AI, cybersecurity incidents, SaaS architecture, developer deep-dives.
- **Color System:**
  - Canvas Base: `#050609` (Deep Obsidian)
  - Primary Text: `#f8fafc` (Crisp Ice White)
  - Muted Editorial Copy: `#94a3b8` (Slate 400)
  - Focal Highlight Gradient: `#fdba74` → `#f97316` (Magma Amber) or `#7dd3fc` → `#0284c7` (Electric Ice)
- **Typography Pairing:**
  - Display Headline: `Plus Jakarta Sans` (`800`–`900`, `letter-spacing: -2.5px`, `word-spacing: 10px`)
  - Sub-hook Accent: `Instrument Serif` (`400 Italic`, `36px–42px`, `color: #cbd5e1`)
  - Kicker / Counter: `JetBrains Mono` or `Fira Code` (`500`, `18px–20px`, `letter-spacing: 0.2em`, pure uppercase, **no dots or pills**)
- **Spatial Treatment:**
  - Single dramatic 3D sculptural hero asset seamlessly blended (`prepare_asset.py place-seamless`) into the lower (`Y: 520px+`) or upper (`Y: 60px–760px`) zone. Subtle radial ambient glow behind subject (`opacity: 0.12`), 45% pure negative space.

---

### Archetype B: Swiss Minimalist Editorial & Carousel Grid (Pentagram / International Style)
- **Best For:** Design essays, business strategy carousels, startup insights, cultural commentary, minimalist Slide 2–5 breakdowns.
- **Color System:**
  - Canvas Base: `#f5f3ee` (Warm Gallery Paper) or `#ededeb` (Swiss Stone)
  - Primary Ink: `#111215` (Carbon Ink)
  - Secondary Copy: `#52525b` (Warm Graphite)
  - Signal Accent: `#e11d48` (Editorial Vermilion) or `#1d4ed8` (International Klein Blue)
- **Typography Pairing:**
  - Display Headline: `Plus Jakarta Sans` (`800`) or `Inter` (`800`, tight tracking + `word-spacing: 8px`)
  - Accent Keyword / Pull-Quote: `Instrument Serif` (`Italic`)
  - Structural Index Numbers (`01`, `02`): `Plus Jakarta Sans` (`700`, `20px`)
- **Spatial Treatment:**
  - Asymmetric 12-column grid, crisp `1px solid rgba(17, 18, 21, 0.12)` architectural hairlines (never boxed cards with drop shadows), generous `84px` outer margins, bold typographic contrast.

---

### Archetype C: Quiet Luxury Travel & Architecture (Kinfolk / Architectural Digest)
- **Best For:** Hospitality, boutique resorts, travel destinations, real estate, slow living, nature sanctuaries.
- **Color System:**
  - Full-Bleed Photography Base + Dark Botanical/Espresso Scrim (`#0c1612` or `#17120e`)
  - Primary Text: `#faf6f0` (Warm Ivory Linen)
  - Warm Metallic Accent: `#e2b887` (Sunlit Travertine / Champagne Ochre)
- **Typography Pairing:**
  - Display Title: `Cormorant Garamond` (`600`, `84px–104px`, wide luxury tracking `letter-spacing: 0.14em` for single-word titles) or `Instrument Serif` (`400`, `88px`)
  - Poetic Subhead: `Cormorant Garamond` (`400 Italic`, `36px`)
  - Architectural Metadata: `Plus Jakarta Sans` (`500`, `18px`, `letter-spacing: 0.22em`, uppercase)
- **Spatial Treatment:**
  - `100%` full-bleed golden-hour photography. Delicate `1px solid rgba(250, 246, 240, 0.22)` inset editorial frame (`44px` inset) optional. Multi-stop scrim over sky/shadows so text never fights bright foliage or mist. Zero pill badges.

---

### Archetype D: Kinetic Sport & Cultural Event Poster (Nike Studio / Contemporary Print)
- **Best For:** Running clubs, tournaments, music festivals, street culture, high-energy product drops.
- **Color System:**
  - Base: `#f2efe9` (Raw Poster Stock) or `#090a0c` (Asphalt Black)
  - High-Voltage Accent: `#ccff00` (Volt Acid) or `#ff4400` ( Track Blaze)
- **Typography Pairing:**
  - Monumental Display: `Syne` (`800`) or `Anton` (`400`, `96px–128px`, `line-height: 0.90`, `word-spacing: 10px`)
  - Technical Spec Copy: `Space Grotesk` (`500`–`700`, `20px–24px`)
- **Spatial Treatment:**
  - Full-bleed motion photography or rim-lit dynamic athlete overlapping monumental typography. Corner registration crosshairs (`+`) or clean coordinate stamps (`JKT // 10K`) instead of web cards.

---

### Archetype E: Sensory Culinary & Artisanal F&B (Bon Appétit / Modern Bistro)
- **Best For:** Restaurants, coffee roasters, craft burgers, bakeries, seasonal menus, gourmet promos.
- **Color System:**
  - Warm Appetite Palette: `#1a120d` (Roasted Espresso), `#fffbeb` (Warm Buttercream), `#f59e0b` (Honey Glaze), `#dc2626` (Chili Warmth)
- **Typography Pairing:**
  - Expressive Display: `Fraunces` (`800`–`900`, soft warm curves) or `Bricolage Grotesque` (`800`)
  - Supporting Copy: `Plus Jakarta Sans` (`500`, `24px–28px`)
- **Spatial Treatment:**
  - Macro full-bleed food photography showing real texture, steam, crumbs, wood/stone/parchment, and warm directional sunlight. **Strict zero-cutout rule**—blend typography into dark ambient wood/tabletop depth-of-field via warm espresso scrims.

---

### Archetype F: Modern Visual Newsroom & Public Policy (Financial Times / Tempo / Vox Style)
- **Best For:** Breaking news, presidential/government policy, economic reports, investigative journalism, market movers.
- **Color System:**
  - Deep Newsroom Base: `#090b10` (Midnight Press)
  - Primary Headline: `#ffffff`
  - Key Phrase Emphasis: `#ef4444` (Urgent Editorial Red) or `#facc15` (Signal Amber)
- **Typography Pairing:**
  - Headline: `Plus Jakarta Sans` (`800`–`900`, `68px–84px`, `line-height: 1.0`, tight lockup)
  - Context Deck: `Plus Jakarta Sans` (`400`–`500`, `26px–30px`, `#cbd5e1`)
  - Rubric Kicker: `Plus Jakarta Sans` (`700`, `19px`, `letter-spacing: 0.18em`, uppercase accent color with a clean `3px` left accent bar or `40px` top rule—no pill capsule, no dot)
- **Spatial Treatment:**
  - **Action Journalism Photography** in upper 62% (expressive podium gesture, field visit, dramatic lighting), transitioning via a deep smooth 4-stop linear scrim (`transparent` at `38%` → `rgba(9,11,16,0.88)` at `64%` → `#090b10` at `82%`) into an authoritative lower-third headline lockup.

---

## 2. CSS Multi-Stop Scrim Recipes (Guaranteed 4.5:1 Legibility)

```css
/* Bottom-Anchored Typography Scrim (Smooth film falloff, never harsh gray band) */
.scrim-bottom {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(6, 9, 14, 0.35) 0%,
    rgba(6, 9, 14, 0.00) 32%,
    rgba(6, 9, 14, 0.72) 60%,
    rgba(6, 9, 14, 0.95) 78%,
    #06090e 100%
  );
  pointer-events: none;
}

/* Top-Anchored Typography Scrim */
.scrim-top {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(6, 9, 14, 0.92) 0%,
    rgba(6, 9, 14, 0.65) 28%,
    rgba(6, 9, 14, 0.00) 52%
  );
  pointer-events: none;
}
```

---

## 3. Figma-Native Editable SVG Template

Figma ignores `@import url(...)` inside SVG `<style>` tags. Always declare `font-family`, `font-weight`, `font-size`, `letter-spacing`, and `fill` **directly as XML attributes** on `<text>` and `<tspan>` nodes so layers open cleanly as editable text in Figma:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" width="1080" height="1350">
  <defs>
    <linearGradient id="bg-scrim" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#050609" stop-opacity="0.92"/>
      <stop offset="46%" stop-color="#050609" stop-opacity="0"/>
      <stop offset="100%" stop-color="#050609" stop-opacity="0.88"/>
    </linearGradient>
    <linearGradient id="accent-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fdba74"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>

  <!-- Layer 1: Unified Canvas Image -->
  <image id="Canvas-Backdrop" href="data:image/jpeg;base64,..." x="0" y="0" width="1080" height="1350" preserveAspectRatio="xMidYMid slice"/>
  <rect id="Contrast-Scrim" width="1080" height="1350" fill="url(#bg-scrim)"/>

  <!-- Layer 2: Editable Typography Group (Direct XML Font Attributes for Figma) -->
  <g id="Editorial-Header" transform="translate(540, 130)" text-anchor="middle">
    <text id="Kicker" y="0" font-family="JetBrains Mono, Fira Code, monospace" font-size="19" font-weight="600" letter-spacing="4" fill="#94a3b8">CYBERSECURITY REPORT</text>
    <text id="Headline-Line-1" y="88" font-family="Plus Jakarta Sans, Inter, sans-serif" font-size="84" font-weight="800" letter-spacing="-2" fill="#f8fafc">WEBSITE KAMU</text>
    <text id="Headline-Line-2" y="172" font-family="Plus Jakarta Sans, Inter, sans-serif" font-size="84" font-weight="800" letter-spacing="-2" fill="#f8fafc">MASIH PAKAI <tspan fill="url(#accent-grad)">PHP?</tspan></text>
    <text id="Subhook" y="238" font-family="Instrument Serif, Georgia, serif" font-style="italic" font-size="38" font-weight="400" fill="#cbd5e1">Kemarin, 70% sistem website dunia nyaris bobol.</text>
  </g>

  <!-- Layer 3: Minimal Footer Metadata -->
  <g id="Slide-Footer" transform="translate(0, 1272)">
    <text x="80" y="0" font-family="JetBrains Mono, monospace" font-size="19" font-weight="600" letter-spacing="2" fill="#f8fafc">01 <tspan fill="#64748b">/ 05</tspan></text>
    <text x="1000" y="0" text-anchor="end" font-family="Plus Jakarta Sans, sans-serif" font-size="19" font-weight="600" letter-spacing="2" fill="#94a3b8">GESER →</text>
  </g>
</svg>
```
