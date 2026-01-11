# Performance Optimization Plan - ApexPalantir Website

## Critical Issue: Largest Contentful Paint (LCP)

**Current State:** LCP = 6.8 seconds ❌ (Target: < 2.5s)
**Priority:** CRITICAL - Must fix before mobile responsiveness work

---

## Executive Summary

The website has severe performance issues affecting user experience and SEO rankings. The Largest Contentful Paint (LCP) of 6.8 seconds is nearly 3x worse than Google's "good" threshold of 2.5 seconds. This means users wait almost 7 seconds before seeing the main content.

**Performance Metrics:**
- 🔴 **LCP: 6.8s** (Target: <2.5s) - CRITICAL
- 🟡 **FCP: 2.7s** (Target: <1.8s) - Needs improvement
- 🟢 **Speed Index: 3.0s** (Target: <3.4s) - Acceptable
- 🟢 **TBT: 0ms** - Excellent
- 🟢 **CLS: 0** - Excellent

---

## Root Cause Analysis

### 1. Unoptimized Images (PRIMARY CAUSE)
**Team member images** on [/about](about.html) page:
- 7 external images from LinkedIn/Pravatar
- No compression or optimization
- No lazy loading implementation
- Loading at full resolution (300x300px minimum)
- Each image: ~50-100KB = 350-700KB total

**Logo file:**
- `APEX-PALANTIR_LARGE.png` - Likely uncompressed
- Loaded immediately in header (render-blocking)

**Impact:** Team images are likely the LCP element, causing 6.8s delay

### 2. No Lazy Loading
All images load immediately on page load, including:
- Below-the-fold team member images
- Hero decorative elements
- Blog post thumbnails

**Impact:** Delays LCP and wastes bandwidth

### 3. External Image Dependencies
Team member images loaded from:
- `media.licdn.com` - External domain requiring DNS lookup + SSL
- `i.pravatar.cc` - External domain requiring DNS lookup + SSL

**Impact:** Additional 200-500ms latency per external domain

### 4. No Resource Hints
Missing critical performance optimizations:
- No `<link rel="preconnect">` for external domains
- No `<link rel="preload">` for critical assets
- No `<link rel="dns-prefetch">` for third-party resources

### 5. Render-Blocking Resources
- Tailwind CSS (potentially large)
- Google Fonts (external resource)
- Lucide icons loaded synchronously

---

## Implementation Plan

### Phase 0: Quick Wins (IMMEDIATE - 1 hour)
**Goal:** Reduce LCP from 6.8s → 4s
**Priority:** CRITICAL

#### 0.1 Add Lazy Loading to Team Images
**File:** `_includes/about/about_team.html`

Add `loading="lazy"` to all team member images:

```html
<!-- BEFORE -->
<img src="https://media.licdn.com/..." alt="Alex" class="...">

<!-- AFTER -->
<img src="https://media.licdn.com/..." alt="Alex" class="..." loading="lazy">
```

**Apply to all 7 team images (lines: 17, 50, 83, 115, 147, 179, 211)**

**Expected Impact:** -1.5s LCP (reduces from 6.8s → 5.3s)

#### 0.2 Add Resource Hints to Header
**File:** `_layouts/default.html`

Add to `<head>` section:

```html
<!-- DNS Prefetch & Preconnect for external images -->
<link rel="dns-prefetch" href="https://media.licdn.com">
<link rel="dns-prefetch" href="https://i.pravatar.cc">
<link rel="preconnect" href="https://media.licdn.com" crossorigin>
<link rel="preconnect" href="https://i.pravatar.cc" crossorigin>

<!-- Preconnect for Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Preload critical logo -->
<link rel="preload" as="image" href="{{ '/assets/images/logos/APEX-PALANTIR_LARGE.png' | relative_url }}">
```

**Expected Impact:** -0.5s LCP (reduces from 5.3s → 4.8s)

**Testing Checkpoint:** Run Lighthouse, verify LCP drops below 5s

---

### Phase 1: Image Optimization (HIGH PRIORITY - 2-3 hours)
**Goal:** Reduce LCP from 4.8s → 3s
**Priority:** HIGH

#### 1.1 Optimize Logo File
**Current:** `APEX-PALANTIR_LARGE.png` (size unknown, likely 100-200KB)

**Actions:**
1. Check current file size
2. Compress PNG with TinyPNG or similar (target: <30KB)
3. Create WebP version (target: <20KB)
4. Implement responsive logo sizes

```html
<!-- Modern approach with WebP -->
<picture>
  <source srcset="{{ '/assets/images/logos/APEX-PALANTIR_LARGE.webp' | relative_url }}" type="image/webp">
  <img src="{{ '/assets/images/logos/APEX-PALANTIR_LARGE.png' | relative_url }}"
       alt="Apex Palantir Logo"
       class="h-8 sm:h-9 md:h-10 w-auto"
       width="120"
       height="40">
</picture>
```

**Expected Impact:** -0.3s LCP

#### 1.2 Download & Optimize Team Images
**Problem:** External images from LinkedIn/Pravatar are slow

**Solution:** Host locally and optimize

**Process:**
```bash
# Create team images directory
mkdir -p assets/images/team

# Download images (manually or via script)
# Then optimize with:
# - ImageOptim (Mac)
# - TinyPNG (Web)
# - squoosh.app (Web)

# Target sizes:
# - Original: 256x256px (md breakpoint)
# - WebP: <15KB per image
# - PNG fallback: <25KB per image
```

**Update references in `_includes/about/about_team.html`:**

```html
<!-- BEFORE -->
<img src="https://media.licdn.com/dms/image/v2/C4D03AQFcgFOcpA-JIg/..." alt="Alex" class="..." loading="lazy">

<!-- AFTER -->
<picture>
  <source srcset="{{ '/assets/images/team/alex.webp' | relative_url }}" type="image/webp">
  <img src="{{ '/assets/images/team/alex.jpg' | relative_url }}"
       alt="Alex"
       class="..."
       loading="lazy"
       width="256"
       height="256">
</picture>
```

**Expected Impact:** -1.5s LCP (hosting locally saves external DNS/SSL time)

#### 1.3 Add Explicit Width/Height to All Images
Prevent Cumulative Layout Shift (CLS) and help browser optimize:

```html
<!-- Add width/height to prevent CLS -->
<img src="..." alt="..." class="..." width="256" height="256" loading="lazy">
```

**Apply to:**
- All team images
- Logo
- Blog post images
- Any decorative images

**Expected Impact:** Maintains CLS at 0, slightly improves LCP

**Testing Checkpoint:** Run Lighthouse, verify LCP < 3.5s

---

### Phase 2: Font Optimization (MEDIUM PRIORITY - 1 hour)
**Goal:** Reduce FCP from 2.7s → 1.5s
**Priority:** MEDIUM

#### 2.1 Optimize Google Fonts Loading
**Current:** Likely render-blocking Google Fonts

**File:** `_layouts/default.html`

**Replace blocking font load with optimized version:**

```html
<!-- BEFORE (if exists) -->
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<!-- AFTER - Optimized with display=swap -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<!-- Optional: Add font-display CSS -->
<style>
  @font-face {
    font-family: 'Plus Jakarta Sans';
    font-display: swap;
  }
</style>
```

**Expected Impact:** -0.5s FCP

#### 2.2 Consider Self-Hosting Fonts
For maximum performance, self-host Google Fonts:

```bash
# Download fonts using google-webfonts-helper
# https://gwfh.mranftl.com/fonts/plus-jakarta-sans

# Add to assets/fonts/
# Update CSS to reference local files
```

**Expected Impact:** Additional -0.3s FCP (optional)

---

### Phase 3: CSS/JS Optimization (MEDIUM PRIORITY - 2 hours)
**Goal:** Further reduce FCP and improve Speed Index
**Priority:** MEDIUM

#### 3.1 Audit Tailwind CSS Bundle Size
**Check current size:**
```bash
ls -lh assets/css/tailwind.css
```

**If >100KB, consider:**
1. Purging unused CSS (should be automatic with Tailwind)
2. Splitting critical CSS inline
3. Loading non-critical CSS async

#### 3.2 Inline Critical CSS
Extract above-the-fold CSS and inline it:

```html
<head>
  <!-- Inline critical CSS -->
  <style>
    /* Critical styles for header, hero, above-fold content */
    .header { ... }
    .hero { ... }
  </style>

  <!-- Load full CSS async -->
  <link rel="preload" href="{{ '/assets/css/tailwind.css' | relative_url }}" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="{{ '/assets/css/tailwind.css' | relative_url }}"></noscript>
</head>
```

**Expected Impact:** -0.5s FCP

#### 3.3 Optimize Lucide Icons Loading
**Current:** All icons loaded synchronously

**Consider:**
- Loading Lucide icons async
- Using SVG sprites for frequently used icons
- Inlining critical icons

---

### Phase 4: Advanced Optimizations (LOW PRIORITY - Optional)
**Goal:** Achieve LCP < 2s, perfect Lighthouse score
**Priority:** LOW (only after Phases 0-3)

#### 4.1 Implement Next-Gen Image Formats
- Use AVIF format where supported (better than WebP)
- Progressive JPEG for photo content
- SVG for logos (if possible)

#### 4.2 Add Service Worker for Caching
- Cache static assets
- Implement offline fallback
- Prefetch likely navigation routes

#### 4.3 Implement HTTP/2 Server Push
If server supports it:
- Push critical CSS
- Push logo image
- Push fonts

#### 4.4 Consider CDN for Static Assets
- Use Cloudflare or similar CDN
- Enables faster global delivery
- Automatic image optimization with Cloudflare Polish

---

## Testing Strategy

### After Each Phase:

#### Lighthouse Testing
```bash
# Run Lighthouse (Chrome DevTools)
# Target scores:
# - Performance: 90+
# - Accessibility: 100
# - Best Practices: 95+
# - SEO: 100

# Test on:
# - Desktop (1920x1080)
# - Mobile (375x667)
# - Tablet (768x1024)
```

#### WebPageTest
```
# Use webpagetest.org for detailed metrics
# Test from multiple locations:
# - Frankfurt, Germany (close to target audience)
# - New York, USA
# - Singapore (worst case)

# Focus on:
# - Start Render time
# - Largest Contentful Paint
# - Total Blocking Time
# - Waterfall chart (identify slow resources)
```

#### Real User Monitoring
Consider adding:
- Google Analytics Core Web Vitals report
- Chrome User Experience Report data

---

## Expected Results

### Performance Improvements:

| Metric | Current | Phase 0 | Phase 1 | Phase 2 | Final Target |
|--------|---------|---------|---------|---------|--------------|
| **LCP** | 6.8s | 4.8s | 3.0s | 2.5s | <2.5s ✓ |
| **FCP** | 2.7s | 2.5s | 2.0s | 1.5s | <1.8s ✓ |
| **Speed Index** | 3.0s | 2.8s | 2.5s | 2.2s | <3.4s ✓ |
| **TBT** | 0ms | 0ms | 0ms | 0ms | <200ms ✓ |
| **CLS** | 0 | 0 | 0 | 0 | <0.1 ✓ |

### Lighthouse Score Projection:

| Phase | Performance | Accessibility | Best Practices | SEO |
|-------|-------------|---------------|----------------|-----|
| Current | ~65 | 100 | 95 | 100 |
| Phase 0 | ~75 | 100 | 95 | 100 |
| Phase 1 | ~85 | 100 | 95 | 100 |
| Phase 2 | ~92 | 100 | 100 | 100 |
| Phase 4 | ~98 | 100 | 100 | 100 |

---

## File Checklist

### Critical Files to Modify:

**Phase 0:**
- [ ] `_includes/about/about_team.html` - Add lazy loading
- [ ] `_layouts/default.html` - Add resource hints

**Phase 1:**
- [ ] `assets/images/logos/APEX-PALANTIR_LARGE.png` - Optimize
- [ ] `assets/images/team/*.{jpg,webp}` - Create optimized team images
- [ ] `_includes/about/about_team.html` - Update image references
- [ ] `_includes/shared/header.html` - Update logo reference

**Phase 2:**
- [ ] `_layouts/default.html` - Optimize font loading

**Phase 3:**
- [ ] `assets/css/tailwind.css` - Audit bundle size
- [ ] `_layouts/default.html` - Inline critical CSS

---

## Implementation Timeline

### Day 1: Quick Wins (1 hour)
- [ ] Phase 0: Lazy loading + resource hints
- [ ] Test: Verify LCP drops below 5s

### Day 2: Image Optimization (3 hours)
- [ ] Phase 1.1: Optimize logo
- [ ] Phase 1.2: Download & optimize team images
- [ ] Phase 1.3: Add width/height attributes
- [ ] Test: Verify LCP drops below 3.5s

### Day 3: Font & CSS (3 hours)
- [ ] Phase 2: Font optimization
- [ ] Phase 3.1-3.2: CSS optimization
- [ ] Final testing
- [ ] Test: Verify LCP < 2.5s ✓

**Total Time:** ~7 hours over 3 days

---

## Success Criteria

✅ **Must Have:**
- LCP < 2.5s (currently 6.8s)
- FCP < 1.8s (currently 2.7s)
- Lighthouse Performance score > 90
- No visual regressions on any page

✅ **Nice to Have:**
- LCP < 2.0s
- Lighthouse Performance score > 95
- All Core Web Vitals in "Good" range

---

## Priority Order

1. **CRITICAL:** Phase 0 (Lazy loading + resource hints) - 1 hour
2. **HIGH:** Phase 1 (Image optimization) - 3 hours
3. **MEDIUM:** Phase 2 (Font optimization) - 1 hour
4. **MEDIUM:** Phase 3 (CSS/JS optimization) - 2 hours
5. **LOW:** Phase 4 (Advanced optimizations) - Optional

**Recommendation:** Complete Phase 0 TODAY, then Phase 1 tomorrow. This will get LCP to ~3s and dramatically improve user experience.

---

## Monitoring & Maintenance

After implementation:

1. **Set up monitoring:**
   - Google Search Console Core Web Vitals report
   - PageSpeed Insights weekly checks
   - Real User Monitoring (if budget allows)

2. **Regular audits:**
   - Monthly Lighthouse audits
   - Quarterly image optimization review
   - Annual performance budget review

3. **Performance budget:**
   - LCP: Must stay < 2.5s
   - FCP: Must stay < 1.8s
   - Total page weight: < 1MB
   - Image weight: < 500KB

---

## Notes

- **DO NOT** start mobile responsiveness work until LCP is fixed
- Performance impacts SEO rankings significantly
- 53% of mobile users abandon sites that take >3s to load
- Current 6.8s LCP is costing you conversions
- Team images are likely the culprit - prioritize Phase 1.2
