# -*- coding: utf-8 -*-
"""Möbius Engineering-Restyle: Hex-Nodes, Mono-Labels, Blueprint-Leader, gestreckte Chevrons.
Danach Mobile-Band-Variante neu ableiten."""
import re, math, pathlib
p = pathlib.Path('apx-root-v9-body.html')
b = p.read_text()
i0 = b.find('viewBox="0 56 1180 324"')
i0 = b.rfind('<svg', 0, i0)
i1 = b.find('</svg>', i0) + 6
svg = b[i0:i1]

def hexpath(cx, cy, r):
    pts = []
    for k in range(6):
        a = math.radians(60*k - 30)
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"

# ---- 1. Node-Kreise -> Hex-Chips (Klasse node fürs Mobile-Stripping) ----
def circle_to_hex(m):
    cx, cy, r, fill, stroke, sw = m.groups()
    cx, cy = float(cx), float(cy)
    if fill == '#8E2DE2':   # START-Node gefüllt
        return f'<path class="node" d="{hexpath(cx, cy, 19)}" fill="#8E2DE2" stroke="#ffffff" stroke-width="2.5"/>'
    return f'<path class="node" d="{hexpath(cx, cy, 18)}" fill="#ffffff" stroke="#8E2DE2" stroke-width="1.75"/>'
svg, n = re.subn(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="(1[78])" fill="(#8E2DE2|#ffffff)" stroke="(#ffffff|#8E2DE2)" stroke-width="(2\.?5?)"/>', circle_to_hex, svg)
assert n == 7, f"nur {n} Nodes konvertiert"

# ---- 2. Leader-Lines -> gestrichelte Hairlines mit Quadrat-Terminal am Band ----
def leader(m):
    x1, y1, x2, y2 = map(float, m.groups())
    return (f'<line class="leader" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>'
            f'<rect class="leader" x="{x1-2.2:.1f}" y="{y1-2.2:.1f}" width="4.4" height="4.4" fill="#94a3b8"/>')
svg, n = re.subn(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)" stroke="#cbd5e1" stroke-width="1.2"/>', leader, svg)
assert n == 7, f"nur {n} Leader konvertiert"

# ---- 3. Sans-Labels -> Mono (12px, slate-700), Klasse nlabel ----
def label(m):
    x, y, anchor, txt = m.groups()
    return f'<text class="nlabel" x="{x}" y="{y}" text-anchor="{anchor}" font-family="JetBrains Mono, ui-monospace, monospace" font-size="12" font-weight="700" fill="#334155">{txt}</text>'
svg, n = re.subn(r'<text x="([\d.]+)" y="([\d.]+)" text-anchor="(middle|end|start)" font-size="13" font-weight="700" fill="#0f172a">([^<]+)</text>', label, svg)
assert n == 13, f"nur {n} Labels konvertiert (erwartet 13)"

# ---- 4. Chevrons strecken (Basis zurückziehen, schmaler machen) ----
def stretch(m):
    d = m.group(1)
    pts = [(float(x), float(y)) for x, y in re.findall(r'([\d.]+) ([\d.]+)', d)]
    A, B, C = pts
    dAB = math.dist(A, B); dAC = math.dist(A, C); dBC = math.dist(B, C)
    # Tip = Ecke gegenüber der kürzesten Seite
    if dBC <= dAB and dBC <= dAC: tip, b1, b2 = A, B, C
    elif dAC <= dAB and dAC <= dBC: tip, b1, b2 = B, A, C
    else: tip, b1, b2 = C, A, B
    M = ((b1[0]+b2[0])/2, (b1[1]+b2[1])/2)
    Mn = (tip[0] + (M[0]-tip[0])*1.45, tip[1] + (M[1]-tip[1])*1.45)
    nb1 = (Mn[0] + (b1[0]-M[0])*0.58, Mn[1] + (b1[1]-M[1])*0.58)
    nb2 = (Mn[0] + (b2[0]-M[0])*0.58, Mn[1] + (b2[1]-M[1])*0.58)
    nd = f"M {tip[0]:.1f} {tip[1]:.1f} L {nb1[0]:.1f} {nb1[1]:.1f} L {nb2[0]:.1f} {nb2[1]:.1f} Z"
    return m.group(0).replace(d, nd)
count = 0
for pat in [r'<path d="(M [\d. L]+Z)" fill="#ffffff" fill-opacity="0\.6"[^>]*/>',
            r'<path d="(M [\d. L]+Z)" fill="#4A00E0" fill-opacity="0\.7"[^>]*/>']:
    svg, n = re.subn(pat, stretch, svg)
    count += n
assert count == 7, f"nur {count} Chevrons gestreckt"

# ---- 5. SVG-a11y ----
svg = svg.replace('<svg viewBox="0 56 1180 324" xmlns="http://www.w3.org/2000/svg" font-family="Plus Jakarta Sans, sans-serif">',
    '<svg viewBox="0 56 1180 324" xmlns="http://www.w3.org/2000/svg" font-family="Plus Jakarta Sans, sans-serif" role="img" aria-labelledby="mbt mbd" text-rendering="geometricPrecision"><title id="mbt">The RevOps lifecycle</title><desc id="mbd">A Möbius band with seven numbered phases: Attract and Demand Gen, Prospecting and Outbound, Lead Management, Selling and Pipeline, Quote-to-Cash, Onboarding and Success, Renewal and Expansion. One continuous loop.</desc>', 1)

b = b[:i0] + svg + b[i1:]

# ---- 6. Mobile-Band neu ableiten (ohne Labels/Leader, MIT Nodes + Nummern) ----
m_svg = svg
m_svg = re.sub(r'<text class="nlabel"[^>]*>[^<]*</text>', '', m_svg)
m_svg = re.sub(r'<(line|rect) class="leader"[^/]*/>', '', m_svg)
m_svg = re.sub(r'<title[^>]*>[^<]*</title><desc[^>]*>[^<]*</desc>', '<title id="mbt">The RevOps lifecycle</title><desc id="mbd">Möbius band, seven numbered phases, listed below.</desc>', m_svg)
m_svg = m_svg.replace('viewBox="0 56 1180 324"', 'viewBox="60 110 1060 260"')
# START-Text behalten? Mobil zu klein -> raus, Nummern bleiben
m_svg = re.sub(r'<text x="[\d.]+" y="[\d.]+" text-anchor="middle" font-family="JetBrains Mono[^"]*" font-size="10" font-weight="700" letter-spacing="2" fill="#8E2DE2">START</text>', '', m_svg)
old_mobile = re.search(r'<div class="sm:hidden mb-6"><svg.*?</svg></div>', b, re.S)
assert old_mobile, "mobiles Möbius-Band nicht gefunden"
b = b[:old_mobile.start()] + f'<div class="sm:hidden mb-6" aria-hidden="true">{m_svg}</div>' + b[old_mobile.end():]

p.write_text(b)
print("Möbius restyled, Mobile-Band abgeleitet")
EOF_MARKER_NOT_NEEDED = None
