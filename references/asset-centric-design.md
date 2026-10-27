# Seamless Asset Harmonization & Graphic Accent Engineering

In professional creative agency design (Pentagram, Studio Dumbar, high-end Behance showcases), a composite is only successful when the viewer **cannot tell where the background ends and the cutout asset begins.**

---

## 1. Why Raw Cutouts Look Like "Tempelan" (Pasted Stickers)

1. **Black-Point Disconnect:** The background is `#090a0f`, but the cutout's darkest shadows are lifted at `RGB(35, 35, 42)`. The cutout appears milky, flat, and floating.
2. **Light Temperature Conflict:** The background has a cool midnight cobalt atmosphere, but the subject was photographed under warm office lighting.
3. **No Light Wrap:** In real physics, intense background light wraps and spills over the silhouette edges of any physical subject.
4. **Missing Cast Shadow:** Without a directional perspective shadow cast onto the floor plane, the feet appear suspended in mid-air.

---

## 2. The 4-Step Harmonization Pipeline

```
Raw Transparent PNG
      │
      ▼
1. Levels & Luminance Matching ──► Crush lifted blacks to match canvas dark point
      │
      ▼
2. Color Grading & Shadow Tint ──► Push shadows cool (or warm) to match ambient mood
      │
      ▼
3. Edge Light Wrap (Rim Bleed) ──► Blend 3-6px of background accent color into outer contours
      │
      ▼
4. Directional Cast Shadow     ──► Affine-skew silhouette onto ground plane with progressive blur
```

---

## 3. Negative Space: Graphic Accents vs Text Clutter

Empty space is sacred in editorial design. When a layout feels too empty:
- **WRONG (Amateur AI approach):** Fill the void with paragraphs of text, fake SaaS metric cards (`+38%`), or rounded pill boxes with pulsing green dots (`● LIVE`).
- **RIGHT (Professional Human approach):** Introduce **disciplined graphic elements** that provide structural tension without cognitive clutter:
  - **Scale & Air First:** Usually the right fix is to enlarge the hero asset or headline, not add things. Empty space is a feature.
  - **Hairline Structure:** A single `1px` hairline rule or a subtle vector arc that guides the eye toward the hero focal point.
  - **Ambient Light:** A soft radial glow (`opacity ≤ 0.15`) behind the subject in the accent hue (`prepare_asset.py --glow 0.12`).
  - **Poster-only accents (Archetype D):** Delicate registration crosshairs (`+`) used sparingly — never on news, luxury, or carousel value slides.
  - ❌ Never add decorative corner tags, serial codes (`REF // 09`), seals with `•` separators, or fake badges (SKILL.md §1 Corner Clutter).

---

## 4. The Two Cardinal Sins of Feed Graphics

### A. The "Fake Clickable Button" Trap
On a social media post (Instagram 4:5 or 1:1), placing a rounded web button (`[ DAFTAR SEKARANG → ]`) is completely irrational—a graphic on a feed cannot be clicked. Professional art directors replace buttons with **valuable typographic metadata**:
- Date and Start Time: `MINGGU — 05:45 WIB`
- Exact Venue / Geographical Coordinates: `GBK SENAYAN, JAKARTA` or `8°39' S  119°34' E`
- Official Handle or Tagline: `@KLUBLARINUSANTARA` or `EDISI OKTOBER 2026`

### B. Asset Chroma Discipline (No Rogue Colors)
The asset must live inside the same color universe as the graphic:
- **Sport (Carbon & Volt Lime):** Asset sports dark gear with volt lime running accents and volt rim lighting.
- **Liburan (Sunset Navy & Amber):** Asset is color-graded with warm golden hour sunlight and terracotta reflections.
- **Health (Deep Sage & Emerald Mint):** Asset wears serene sage activewear harmonized with soft botanical green lighting.
