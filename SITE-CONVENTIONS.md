# SITE-CONVENTIONS.md

The Thames Club website — design, copy, and deploy conventions.

Repo: `https://github.com/Blipscan/ThamesClub-Website` (branch `master`)
Live: `https://thamesclub-website.onrender.com` (HTTP basic auth — see *Deploy*)

This document is the canonical reference. If a page disagrees with this file, the page is wrong. Update the page, not the doc — unless a deliberate decision changes the rule, in which case update the doc first, link the commit, then propagate.

---

## 1. Identity

- **Full name:** The Thames Club
- **Short name:** Thames Club (in body copy when "The" is awkward)
- **Never** abbreviate as "TC" in body copy. Filenames and CSS class prefixes (`tc-…`) are fine.
- **Founded:** February 8, 1869
- **Short founding line:** *Est. 1869*
- **Location:** 290 State Street, New London, CT 06320
- **Tagline (current):** "Connecticut's oldest private social club."
- **Voice:** Understated, member-facing, plainspoken with occasional formality. Edwardian-adjacent without being twee. The dining room is "a room that knows its members," not "an exclusive culinary destination."

### Locked names (do not vary)

| Use this                | Never use                              |
|-------------------------|-----------------------------------------|
| Above & Below           | Above & Beyond, Above and Below         |
| Est. 1869               | Estd. 1869, Founded 1869 (in short form)|
| New London, CT          | NL, New-London                          |
| 290 State Street        | 290 State St., #290 State              |

### Contact (canonical)

- **Email:** `thamesclub.nl@gmail.com`
- **Phone:** `959-264-2733` — display as `959-264-2733` or `(959) 264-2733`; `tel:` href is unformatted: `tel:9592642733`
- **Office contact:** `thamesclub.nl@gmail.com` (same address; no separate office line)

---

## 2. Color tokens

Defined in `:root` on every page. All values literal hex unless noted.

```css
:root{
  /* Dark surfaces */
  --deep:    #07101a;   /* hero background, page bottom */
  --navy:    #0c1c2e;   /* nav bar, image placeholders */
  --mid:     #0e1c2c;   /* mid-dark sections */

  /* Parchment surfaces */
  --cream:   #f4edd8;   /* primary cream section bg */
  --cream-d: #e8dfc8;   /* body text on dark surfaces */
  --cream-dim:#a89e87;  /* dim cream — secondary text on dark */

  /* Gold accents */
  --gold:    #a6894a;   /* eyebrows, dividers (mid) */
  --gold-b:  #c9a96e;   /* eyebrows on dark, prices, links */
  --gold-dim:rgba(166,137,74,.25);  /* hairline rules */

  /* Ink */
  --ink:     #1a1208;   /* body text on cream */

  /* Layout */
  --max:     1120px;    /* content max-width */
}
```

### Section background utility classes

| Class | Background      | Foreground use |
|-------|-----------------|----------------|
| `.sc` | `#f4edd8` cream | `--ink` body text |
| `.scd`| `#ede4cf` cream-deep | `--ink` body text |
| `.scl`| `#f0e8d0` cream-light (parchment) | `--ink` body text |
| `.sn` | `#0c1c2e` navy | cream text |
| `.sm` | `#0e1c2c` mid | cream text |
| `.sd` | `#07101a` deep | cream text |
| `.sw` | `#0a1520` / `#0b0906` (varies by page) | cream text |

---

## 3. Readability rule (load-bearing — do not break)

This is the rule that gets forgotten: **dark backgrounds need pure-dark hex; light backgrounds need pure-dark text.** "Almost dark" parchment text on cream is the problem to avoid.

| Surface | Background hex range | Text hex range |
|---------|---------------------|-----------------|
| Hero / dark sections | `#1a–#2a` and darker (e.g. `#07101a`, `#0c1c2e`) | `#e8dfc8`, `#a89e87` (cream tones) |
| Parchment / cream sections | `#e8–#f4` (cream tones) | `#2a2a3a` or darker; **never lighter than `#4a`** |

Quick check before shipping a page: open in browser, screenshot, drop saturation to zero — text must remain legible. If grey-on-grey looks washed out, the text is too light.

`--cream-dim: #a89e87` is **for use on dark backgrounds only**. Do not use it as body text on cream. Use `var(--ink)` (`#1a1208`) on cream surfaces.

---

## 4. Typography

### Stack

```html
<link rel="preconnect" href="https://fonts.googleapis.com/">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500&display=swap">
```

| Role | Family | CSS var | Used for |
|------|--------|---------|----------|
| Display | Cormorant Garamond | `var(--display)` | h1, h2, hero, pull-quotes, prices |
| Body serif | Libre Baskerville | `var(--serif)` | body copy, prose, eyebrows, footer copy |
| UI sans | Inter | (no var) | nav links, dropdowns, footer links |

Fallbacks: `Georgia, serif` for serif; `system-ui, sans-serif` for sans.

### Sizes (canonical)

| Element | Size |
|---------|------|
| h1 (page hero) | `clamp(42px, 7vw, 88px)` — section heroes; `clamp(50px, 7.8vw, 100px)` for site index hero |
| h2 (section title) | `clamp(32px, 5vw, 60px)` |
| Deck / lead | 15px, line-height 1.7, max-width 560–640px |
| Prose body | 15px, line-height 1.8, max-width 640px (or 17px / 1.88 / 600px on long-form) |
| Pull-quote | `clamp(16px, 1.9vw, 22px)` italic |
| Eyebrow / `sec-label` | 9px, weight 700, letter-spacing .3em, uppercase |
| Caption | 9px, letter-spacing .13em, uppercase |
| Nav link | 10.5px, weight 500, letter-spacing .10em, uppercase |
| Menu price | 16px display |

Letter-spacing on uppercase eyebrows / nav: never less than `.1em`. Larger uppercase (page hero eyebrows) goes to `.3em`.

---

## 5. Navigation (canonical structure)

Top nav is **sticky** (`position:sticky;top:0`). Mobile breakpoint: **960px** — at and below, the link list collapses behind a hamburger.

### Link order (left to right, after brand)

1. **Dining** (`dining.html`)
2. **Events** ▾ (dropdown)
   - Events calendar (`events.html`)
   - Event rooms (`event-rooms.html`)
   - Private events (`event-planners.html`)
3. **Above & Below** (`above-below.html`)
4. **About** ▾ (dropdown)
   - History (`history.html`)
   - Restoration (`restoration.html`)
   - Pierson Gallery (`pierson-gallery.html`)
   - *— divider —*
   - Photo gallery (`gallery.html`)
   - Duckpin bowling (`bowling.html`)
   - Community (`community.html`)
5. **Membership** (`membership.html`)
6. **Reciprocal Clubs** (`reciprocal-clubs.html`)
7. **Visit** (`visit.html`) — styled as `.nav-cta` (rounded outline)

The current page's link gets `class="active"` (gold color).

### Brand block

```html
<a class="site-shell-brand" href="index.html">The Thames Club<small>New London · Est. 1869</small></a>
```

The canonical mark: brand serif uppercase, gold-toned `Est. 1869` subtitle. Do not substitute "New London, CT" or "Founded 1869" here.

---

## 6. Header & footer (copy-paste blocks)

### Header (paste verbatim into new pages)

The full nav block lives in `dining.html` (`<nav class="site-shell-nav">…</nav>` plus the `<div class="nav-mobile">` mirror). Copy from there. Set the current page's link to `class="active"` and remove `class="active"` from any other link.

### Footer (paste verbatim)

```html
<footer class="site-shell-footer">
  <div class="site-shell-foot-inner">
    <div>
      <div class="site-shell-foot-brand">The Thames Club</div>
      <div class="site-shell-foot-copy">
        290 State Street · New London, CT 06320<br>
        <a href="mailto:thamesclub.nl@gmail.com">thamesclub.nl@gmail.com</a> · (959) 264-2733
      </div>
    </div>
    <div class="site-shell-foot-links">
      <a href="index.html">Home</a>
      <a href="dining.html">Dining</a>
      <a href="events.html">Events</a>
      <a href="restoration.html">Restoration</a>
      <a href="pierson-gallery.html">Pierson Gallery</a>
      <a href="community.html">Community</a>
      <a href="publications.html">Publications</a>
      <a href="membership.html">Membership</a>
      <a href="reciprocal-clubs.html">Reciprocal Clubs</a>
      <a href="visit.html">Visit</a>
    </div>
  </div>
</footer>
```

The footer link list is intentionally shorter than the nav — it omits dropdown children (Event rooms / Private events / Photo gallery / etc.) since they're already accessible from the parent destinations.

---

## 7. Image conventions

### Aspect ratio

**4:3 is the site default for content photos.** Use the `.photo-4-3` pattern:

```html
<div class="photo-4-3"><img src="images/section_NN.jpg" alt="…"></div>
```

```css
.photo-4-3{width:100%;aspect-ratio:4/3;overflow:hidden;border-radius:8px;display:block;position:relative;background:#0c1c2e}
.photo-4-3 img{width:100%;height:100%;object-fit:cover;object-position:center;display:block;transition:transform 6s ease;filter:contrast(1.07) saturate(1.04);image-rendering:-webkit-optimize-contrast}
.photo-4-3:hover img{transform:scale(1.02)}
```

Image pairs (side-by-side) use 3:2 instead and lose the border-radius:

```css
.image-pair .photo-4-3{aspect-ratio:3/2;border-radius:0}
```

### Sharpen filter

Every photo gets `filter:contrast(1.07) saturate(1.04)` plus `image-rendering:-webkit-optimize-contrast`. This is built into `.photo-4-3 img` — do not apply per-image. The values are deliberately conservative:

- `contrast(1.04) saturate(1.02)` — too subtle to perceive
- `contrast(1.07) saturate(1.04)` — **current; right for most photos**
- `contrast(1.10) saturate(1.06)` — starts to look "processed"

The filter does not fix actual focus blur. Re-shoot if a photo is genuinely soft.

### File naming

```
images/<section>_<NN>.<ext>          original
images/<section>_<NN>__AIE.<ext>     AI-enhanced variant
```

Examples: `dining_01.jpg`, `dining_01__AIE.png`, `events_03.jpg`.

`NN` is two-digit zero-padded. `AIE` = "AI Enhanced." Keep both originals and enhanced versions in `images/` — the page chooses which to reference.

### Photoreal only

No illustrations, no flat icons, no AI-generated stylized images for member-facing photos. AI enhancement of real photos (denoise, sharpen, exposure) is fine; AI-generated subjects are not.

### Self-contained delivery (publications only)

For the `above-below-*.html` issue archive — and any future single-file publication intended to be emailed or downloaded — embed images as base64 data URIs. This is **not** the convention for regular site pages; only for publication HTML where portability matters.

### Dimension targets

| Use | Target |
|-----|--------|
| Section hero photo | 1600 × 1200 (4:3), JPG quality 85 |
| Image pair | 1200 × 800 (3:2), JPG quality 85 |
| Gallery thumbnails | 800 × 600 (4:3), JPG quality 80 |
| AI-enhanced source | PNG, no max — they're large, that's fine |

---

## 8. Layout primitives

```css
.w           /* content wrapper, max-width 1120px, 44px gutters */
.two-col     /* 1fr 1fr, gap 48px, align-items:start */
.two-col-c   /* 1fr 1fr, gap 48px, align-items:center */
.three-col   /* repeat(3,1fr), gap 32px */
.image-pair  /* 1fr 1fr, gap 24px */
```

Mobile (≤768px) collapses all multi-column grids to single-column.

Section padding: `88px 0` (most), `60px 0` (mobile), `72px 0` (compact).

---

## 9. Component patterns

| Class | What it is |
|-------|-----------|
| `.sec-label` (gold-b) / `.sec-label-d` (deep gold) | Eyebrow above section title |
| `.serif` / `.serif-dk` | h2 — cream / navy variants |
| `.prose` / `.prose-dk` | Body copy — dark / cream backgrounds |
| `.pull` `.dk` / `.lt` | Pull-quote with gold left border |
| `.gold-rule` | Hairline gold gradient divider |
| `.cta-btn` / `.cta-btn-dk` | Outline buttons — dark / cream backgrounds |
| `.menu-section` + `.menu-item` | Dining-style price list |
| `.card-lt` | Cream-bg card with gold border |

When adding a new pattern, document it here in the same format.

---

## 10. Page inventory

### Live site pages (canonical)

`index` · `dining` · `events` · `event-rooms` · `event-planners` · `above-below` · `bowling` · `community` · `history` · `restoration` · `pierson-gallery` · `gallery` · `membership` · `reciprocal-clubs` · `visit` · `publications` · `room` · `submarineland`

### Issue archive (publications)

`above-and-below-issue-001.html` · `above-and-below-issue-2.html` · `issue1.html` · `above-below-replaced2.html` · `reciprocal-clubs-print.html`

---

## 11. Voice & copy rules

- Sentence-case section eyebrows ("Bar & Cellar," not "BAR & CELLAR" — uppercase happens via CSS `text-transform`).
- Em-dashes — not hyphens — for parenthetical asides.
- Oxford comma yes.
- Numbers under ten spelled out ("nine dollars," not "$9") in prose; price tags numeric.
- "Members and accompanied guests" is the canonical phrase for who can dine. Don't paraphrase.
- Avoid marketing voice. "Our Mission" / "We Believe" copy doesn't belong here. State what the room does, who uses it, when it's open.

---

## 12. Deploy

### How a change gets to the live site

1. **Edit on `master` branch** in `C:/Users/super/Documents/Projects/ThamesClub-Website-deploy`.
2. **Commit** with a descriptive message (lowercase area prefix, e.g. `dining: …`, `nav: …`, `images: …`).
3. **Push to `origin/master`** (`https://github.com/Blipscan/ThamesClub-Website.git`).
4. **Render auto-deploys** from `master`. Live in 1–3 minutes.
5. **Hard-refresh** (`Ctrl+F5`) on the live URL to bypass image cache.

### Live preview auth

The Render deployment is gated by HTTP Basic Auth (defined in `server.js`):

- User: `tcTest`
- Pass: `290state`

Override via `AUTH_USER` / `AUTH_PASS` env vars on Render. Do not commit different defaults.

### Pre-push checklist

- [ ] All image `src` paths resolve (no orphan references after a rename)
- [ ] New page has the canonical nav block, with the right `class="active"` set
- [ ] New page has the canonical footer block
- [ ] Page validates against the readability rule (Section 3)
- [ ] No `font-family` declarations bypass the three-family stack
- [ ] No new color literals — use the CSS variables from Section 2
- [ ] Naming rules respected — search the page for "Above & Beyond," "TC," "Founded 1869"

---

## 13. Known TODOs

- Audit pages for `--cream-dim` used as body text on cream backgrounds (readability rule violations)
- Decide whether to retire `above-below-replaced2.html` and `issue1.html` (legacy)
- Internal title/header inside `above-and-below-issue-2.html` may still read "Above & Beyond" — audit and update if so
