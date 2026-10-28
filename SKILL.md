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
- **Aset Pendukung & Satelit 3D Boleh Dipakai secara Terkondisi:** Elemen visual pendukung (seperti kepingan partikel, lencana, koin 3D, atau icon kontekstual) diperbolehkan selama dikondisikan dengan baik: memiliki keterkaitan erat dengan pesan slide, ditempatkan dengan tujuan visual yang terukur, pencahayaannya menyatu dengan lingkungan studio, dan tidak disebar acak-acakan hingga merusak fokus hero asset.
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

### 3.3 Dynamic Headline Architecture for Long Copy (Anti-Monotone Pacing)
Ketika judul relatif panjang (terutama di Cover Slide 1), **DILARANG** merendernya dalam satu ukuran dan bobot yang seragam (*flat monotone*). Pecah judul menjadi 3 tingkatan ritme emosi dan kontras visual:
1. **Lead-In Premise (Muted / Lighter Display):** Kalimat pengantar yang santai (`48px–54px`, `weight: 600`, warna slate/muted `rgba(255,255,255,0.65)` atau `#64748B`).
2. **Core Tension (Heavy Display):** Pokok masalah atau konflik narasi (`72px–76px`, `weight: 800`, kontras tinggi `#FFFFFF` atau `#0F172A`).
3. **Climax Punchline (Monumental Gradient / Pop):** Kata kunci gong pemungkas (`88px–98px`, `weight: 900`, aksen gradasi dinamis) yang menjadi magnet visual utama.

---

## 4. Seamless Asset Blending & Contrast Gate

- **Zero Bounding-Box Seams (Anti-Pasted-Rectangle / Anti-Tempelan Protocol):**
  - Mengapa aset render sering kelihatan "tempelan"? Karena piksel batas terluar (*border pixels*) pada render JPEG sering selisih 2–5 RGB dari warna kanvas target (misal kanvas `#FFFFFF` tapi background gambar `#EAEAEA`, atau kanvas `#060B14` tapi gambar `#040E17`).
  - **The 3-Step Seam Eradication Protocol:**
    1. **Border Tone Clamping:** Geser dan kunci piksel background aset agar warnanya 100% identik dengan target kanvas hex.
    2. **Super-Ellipse Alpha Feathering (PNG):** Konversi aset menjadi PNG dengan channel alpha yang memudar halus (*smoothstep*) menjadi 0.0 pada 15–20% batas terluar.
    3. **CSS Radial Feather Mask:** Pasang `-webkit-mask-image: radial-gradient(ellipse 75% 75% at 50% 50%, black 40%, rgba(0,0,0,0.85) 60%, transparent 92%);` pada elemen `.bg-asset` di HTML untuk melarutkan gambar ke kanvas secara mutlak.
  - Never paste a square render/photo onto a dark or colored canvas if its background RGB (`#0b0d13`) differs even slightly from the canvas hex (`#050609`)—OLED screens expose faint rectangles immediately.
  - Always compose standalone assets with [`prepare_asset.py`](./scripts/prepare_asset.py) `place-seamless`:
    - **Transparent PNG cutouts** (everything in `assets/3d/` and `assets/people/`) keep their original colors; the script trims empty padding and fits the subject inside the zone—never cropped.
    - **Opaque studio renders** get their backdrop tone clamped to the exact canvas hex plus a smooth super-ellipse feather to zero at every edge.
- **Harmonize the cutout** (black point, color temperature, light wrap, cast shadow) per [asset-centric-design.md](./references/asset-centric-design.md). Optional subtle ambient glow: `--glow 0.12 --glow-color "<accent hex>"`.
- **WCAG 4.5:1 Scrim Protection:** Never place light or thin typography directly over bright sky, sunlit leaves, mist, or busy highlights. Always apply a multi-stop CSS scrim behind text zones (recipes in the archetypes reference).

---

## 5. Instagram Carousel Architecture, Brainstorming & Design Briefing

### 5.1 Benchmark Reference (Cara Berpikir, Bukan Template)
- **Living Benchmark:** [http://202.10.47.34/gastrip/halodev/](http://202.10.47.34/gastrip/halodev/)
- **Halodev Brand Synergy:** Jika mendesain konten resmi Halodev, wajib merujuk pada skill [`halodev-branding`](../halodev-branding/SKILL.md) (warna hijau `#06BE72` & biru `#03A9FF`, kanvas biru tua `#060B14` & putih bersih `#FFFFFF`, watermark `@halodev_id` font Poppins tanpa logo grafis).
- **Golden Rule:** **Tiru cara berpikir dalam pembuatannya, BUKAN meniru template visualnya!**
  - Yang ditiru: Empati pembaca modern, hook tajam tanpa sub-teks di cover, teks hemat to-the-point, ritme pergantian warna antar-slide, pencahayaan 3D nyata dengan soft shadows, dan spatial yield (aset tidak tertutup teks).
  - Yang dihindari: Mengulang kombinasi warna atau susunan posisi yang sama secara mekanis di setiap proyek.

### 5.2 Step-by-Step Brainstorming & Viral Content Discovery (Audience-First & Meme-Relatable)
Sebelum masuk ke perancangan visual, agen wajib membedah topik dan merumuskan sudut pandang (*angle*) yang magnetis untuk audiens luas (mahasiswa, pekerja, freelancer, tech enthusiast, kreator):

1. **Step 1: Trend & Friction Scanning (Mencari Keresahan Kolektif)**
   - Cari isu yang sedang hangat dibicarakan di media sosial, industri tech, karir, atau dinamika kehidupan sehari-hari.
   - Temukan friksi emosional: mitos yang dipercaya banyak orang vs fakta sebenarnya, over-hype teknologi baru, atau kebiasaan konyol yang dialami hampir semua orang tapi jarang diakui secara terbuka.
2. **Step 2: The Universality Filter (Ubah Niche Menjadi Relevan untuk Semua Kalangan)**
   - Hindari bahasa teknis atau manajerial yang kaku dan mengintimidasi (misal: "Optimasi Query Database PostgreSQL").
   - Terjemahkan ke analogi manusiawi yang relate ke semua orang (misal: "Kenapa Aplikasi yang Kita Buat Sering Lemot Pas Mau Dipamerin ke Orang?").
   - Uji dengan pertanyaan emas: *"Apakah orang non-expert yang scrolling feed dalam 2 detik langsung paham, penasaran, dan merasa ini relevan buat dia?"*
3. **Step 3: Meme-Relatable Satire & Witty Humor (Cerdas, Jenaka, Tetap On-Point)**
   - Gunakan humor cerdas, sindiran halus (*playful irony*), atau kejujuran santai (*self-deprecating truth*).
   - Jangan gunakan jokes garing atau meme receh yang merusak wibawa desain agensi; gunakan humor berbasis realita ("Di medsos gayanya kayak arsitek sistem masa depan, di kantor aslinya masih panik kalau terminal keluar teks merah").
4. **Step 4: The 2-Second Tension Hook Formulation (Rumus Cover Nendang)**
   - Buat headline cover yang memicu paradoks, rasa penasaran, atau kejutan (*pattern interrupt*).
   - **Haram Sub-Teks di Cover:** Headline utama harus mandiri, tebal, dan kuat tanpa perlu disangga kalimat penjelas panjang di cover.
   - Contoh Perbandingan:
     - ❌ *Biasa/Membosankan:* "Perkembangan Bahasa Pemrograman PHP di Tahun 2026"
     - ✅ *Tension & Relatable:* "PHP Masih Hidup. Dan Diam-Diam Masih Dipakai Buat Nopang Internet."
5. **Step 5: Structuring the 5-Slide Narrative Arc**
   - **Slide 1 (The Hook):** Menangkap perhatian dalam 2 detik, paradoks utama, zero fluff.
   - **Slide 2 (The Illusion / The Common Myth):** Membedah apa yang selama ini salah kaprah atau over-hyped di publik.
   - **Slide 3 (The Reality Check / Data Shock):** Fakta mengejutkan atau komparasi tajam di dunia nyata.
   - **Slide 4 (The Core Mechanism / The Actionable Shift):** Solusi atau cara pandang baru yang mencerahkan.
   - **Slide 5 (The Climax & Bookmark Takeaway):** Pernyataan penutup yang berbobot, takeaway emosional yang layak disimpan/dishare.

### 5.3 Step-by-Step Perancangan Master Design Brief (Slide-by-Slide Blueprint)
Setelah narasi matang, agen wajib merancang **Master Design Brief** secara terstruktur dan terperinci sebelum menulis kode HTML/CSS:

1. **Langkah 1: Fondasi Strategi & Tone Visual**
   - *Target Persona:* Deskripsi ringkas siapa yang membaca (anak muda, tech folks, profesional, umum).
   - *Tone of Voice:* Satir elegan, percaya diri, edukatif, bersahabat.
   - *Archetype Visual:* Memilih dari [agency-design-archetypes.md](./references/agency-design-archetypes.md) (misal: Dark Precision Tech, Swiss Minimalist, Warm Editorial).
2. **Langkah 2: Choreography Pacing Wave (Alur Warna Antar-Slide)**
   - Rancang pergantian kontras warna setiap slide agar pembaca tidak bosan (misal: Slide 1 Dark `#0D0F12` → Slide 2 Cream `#F4EFEA` → Slide 3 Sand `#E6E0D6` → Slide 4 Split `#121316` → Slide 5 Dark Spotlight `#0D0F12`).
3. **Langkah 3: Perumusan Detail Per-Slide (Format Wajib Brief)**
   Setiap slide wajib memiliki spesifikasi teknis lengkap:
   - **Slide Index & Peran Naratif:** (misal: Slide 02 — The Illusion / Duel).
   - **Mood & Hex Background:** (misal: Warm Minimalist `#F4EFEA`).
   - **Copywriting Naskah:**
     - *Kicker/Meta:* (misal: `REALITA VS EKSPEKTASI` | `02 / 05`)
     - *Headline Bold:* (Maksimal 2-3 baris, font besar, tracking ketat dengan word-spacing aman).
     - *Body Hemat:* (Maksimal 1-2 baris, bahasa santai, bebas filler).
     - *Action/Nav:* (`Geser →` atau bookmark takeaway).
   - **Layout Architecture (Form Follows Message):**
     - Sifat pesan menentukan layout (apakah split columns, top-anchored, central totemic, atau asymmetric kinetic).
     - Alokasi rasio negative space (minimal 35-50% area lega).
     - Zona koordinat teks vs aset (Spatial Yield Rule: teks di Y: 100–480px, aset di Y: 520–1280px, atau sebaliknya).
   - **Spesifikasi Aset 3D & Satelit Terkondisi:**
     - Subjek visual utama & material fisik (misal: Blue Sapphire ElePHPant berlapis frosted glass transparan dengan specular highlight).
     - Aset pendukung/satelit (jika ada, harus bermakna dan terkondisi: misal kepingan partikel kristal melayang halus di orbit sudut, tidak menutupi teks).
     - Pencahayaan: 3-point studio lighting (key light lembut, rim light biru, ambient floor bounce) + soft cast shadow di lantai/bidang bawah.
   - **Directional Scrim Protection:**
     - Menentukan arah gradien perlindungan (`linear-gradient(to bottom, #0D0F12 55%, transparent 100%)`) agar teks selalu 100% kontras dan tajam.

### 5.4 Form Follows Message (Tata Letak Mengikuti Sifat Pesan — Anti-Template)
**FORBIDDEN:** Menggunakan cetakan tata letak yang sama di setiap proyek atau mengulang layout grid yang identik di dua slide berturut-turut. Komposisi kanvas harus lahir secara organik dari sifat pesan di slide tersebut:
- **Jika Pesan berupa Data Shock / Angka Besar:** Angka tersebut yang menjadi raksasa taktil di tengah kanvas (misal: `75%` bertekstur kristal), teks pendukung mengalah ringkas di bawahnya.
- **Jika Pesan berupa Mindset Shift / Quotes Kontemplatif:** Komposisi minimalis dengan 70%+ ruang kosong bersih (*wide negative space*), tipografi anggun di tengah tanpa dipaksa dijejali aset besar jika tidak diperlukan.
- **Jika Pesan berupa Duel / Komparasi (Before vs After):** Split horizontal dua sisi, perbandingan dua kartu bernuansa beda (dull vs glowing), atau teks yang dicoret tegas.
- **Jika Pesan berupa Hero Showcase:** Aset 3D mengambil panggung dominan (*macro close-up* / *full-bleed*), teks mengalah di sisi kanvas.
- **Jika Pesan berupa Dialog / Situasi Nyata:** Tata letak mengadaptasi balon obrolan estetik, terminal kode, atau dialog bertingkat.

### 5.5 Dynamic Visual Pacing Wave (Ritme Kontras Antar-Slide)
- **Do NOT lock every slide to solid dark hexes.** Variasikan kontras nilai (*Value Contrast*) dan saturasi agar mata pembaca tidak mengalami kelelahan visual (*visual fatigue*):
  - Kombinasikan slide gelap dramatis, slide terang bersih (*warm cream* `#F4EFEA` atau *crisp white* `#FFFFFF` dengan tipografi arang gelap), dan slide bertema tonal/split.
- **AI-Generated Environmental Backgrounds with Gradient Overlays:**
  - Backgrounds can feature generated scenes (architectural concrete, studio podiums, soft haze, textured plaster, ribbed glass bokeh).
  - **Mandatory Legibility Scrim:** Always overlay a directional `linear-gradient` (from 90-95% opaque tone-matched background where text sits to 0% transparent where the asset and light rays shine) so text is 100% crisp without sacrificing the cinematic depth of the image.

### 5.6 Modern Conversational Copywriting & Reader Empathy
- **Speak to Everyone:** Never force rigid corporate or managerial framing unless explicitly requested. Write for modern ambitious humans—students, freelancers, creators, founders alike.
- **Ruthless Text Economy:** Cut unnecessary filler. Say the point in 1-2 sharp, conversational sentences that hit like a realization ("Oh, ini maksudnya!").
- **Hook Simplicity:** Cover hook must stand on its own without needing cluttered explanations. **Haram ada sub-teks di cover jika headline sudah kuat.**

---

## 6. Execution Workflow (Low-RAM Safe & Self-Verified)

Follow these 7 steps on every design task:

### Step 0: Brainstorming & Viral Angle Discovery
- Lakukan riset trend dan keresahan kolektif audiens sesuai §5.2.
- Rumuskan 2-second tension hook (bebas sub-teks di cover) dan 5-slide narrative arc.

### Step 1: Slide-by-Slide Master Design Brief
- Susun brief produksi lengkap per-slide sesuai format blueprint §5.3 (naskah teks hemat, mood warna hex, layout choreography, spesifikasi aset 3D & material fisik, serta directional scrim).

### Step 2: Memory-Safe Asset Preparation (1GB RAM Guard)
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

### Step 3: Compose Modern HTML/CSS Canvas
- Consult [agency-design-archetypes.md](./references/agency-design-archetypes.md) to pick an archetype that suits the topic's emotional psychology (never reuse the same skeleton across unrelated niches).
- Lock `html, body` to exact dimensions (`1080 × 1350` for 4:5, `1080 × 1080` for 1:1, `1080 × 1920` for 9:16) with `margin: 0; overflow: hidden`.

### Step 4: Render Pixel-Perfect PNG via Helper Script
- Use the low-memory renderer (do NOT write ad-hoc Playwright scripts):
  `python3 {baseDir}/scripts/render_graphic.py <input.html> <output.png> 1080 1350 --preview`
- The renderer waits for webfonts and images, then prints an **automatic `AUDIT:` report** (text < 18px, text inside the 72px side margin or clipped, banned `•`/`●` glyphs). **Every AUDIT issue must be fixed and re-rendered.**

### Step 5: Export True Figma-Editable SVG
- Create a standalone `.svg` (`viewBox="0 0 1080 1350"`) alongside the PNG.
- **Figma Compatibility Rule:** Figma ignores `@import url(...)` inside `<style>`. Set `font-family`, `font-weight`, `font-size`, `letter-spacing`, and `fill` **directly as XML attributes** on `<text>` / `<tspan>` (template in [agency-design-archetypes.md](./references/agency-design-archetypes.md)).

### Step 6: MANDATORY Visual Self-Critique Gate (Before Replying!)
**NEVER send a design without self-reviewing each slide.** After rendering, **inspect every rendered slide image** and audit it against these core design principles:
1. **Holistic Balance & Negative Space Equilibrium:**
   - Balance is NOT just text centering—it is the dynamic equilibrium between **Asset Mass**, **Text Mass**, and **Empty (Negative) Space**.
   - Check every slide: Is any quadrant "jompang" (deserted or overly heavy)? Is empty space distributed harmoniously?
2. **Asset Prominence & Non-Occlusion:**
   - Are assets scaled prominently (never shrunken or timid)?
   - Are assets fully celebrated—never cropped, buried behind cards, or amputated?
   - Do assets play with rich light, volumetric glow, reflections, and realistic soft shadows?
3. **Background Variety & Layering:**
   - Is the carousel dynamic (alternating dark, light/warm cream, and tonal backgrounds)?
   - Are background images layered with tone-matched linear/radial gradients so text has 100% crisp legibility?
4. **Copywriting & Modern Reader Empathy:**
   - Is the language natural, conversational, and instantly understood by anyone?
   - Is the cover hook razor-sharp and free of redundant sub-text?
   - Has all unnecessary fluff been ruthlessly cut?
5. **Zero Slop & Technical Hygiene:**
   - No `•` bullets/dots, pill capsules, fake buttons, unconditioned random clipart/satellites, or UI window titlebars?
   - Word spacing intact (no `WEBSITEKAMU`), `>= 72px` side margins, all copy `>= 18px` with clean contrast?

If **any** check fails, revise the HTML/CSS or asset placement and re-render until you are 100% confident the design is truly publication-grade.
