# -*- coding: utf-8 -*-
"""Hexnetz Hochformat-Variante für Mobile (<640px): gleiche Struktur, größere Type."""
import math, pathlib, re, base64
SIMPLE = pathlib.Path('/usr/local/lib/python3.11/dist-packages/material/templates/.icons/simple')
REPO = pathlib.Path('site/assets/images/logos')
MONO = "JetBrains Mono, ui-monospace, monospace"
SANS = "Plus Jakarta Sans, sans-serif"
def si_path(name):
    raw = (SIMPLE/f'{name}.svg').read_text()
    return re.search(r'<path d="([^"]+)"', raw).group(1)
def si_icon(name, x, y, size=20, fill='#e2e8f0', opacity=1.0):
    s = size/24
    return f'<g transform="translate({x-size/2},{y-size/2}) scale({s:.3f})" opacity="{opacity}"><path d="{si_path(name)}" fill="{fill}"/></g>'
def repo_img(name, x, y, size=20):
    p = pathlib.Path(f'{name}.svg') if pathlib.Path(f'{name}.svg').exists() else REPO/f'{name}.svg'
    data = base64.b64encode(p.read_bytes()).decode()
    return f'<image href="data:image/svg+xml;base64,{data}" x="{x-size/2}" y="{y-size/2}" width="{size}" height="{size}"/>'
def hexpath(cx, cy, r):
    pts = []
    for i in range(6):
        a = math.radians(60*i - 30)
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x,y in pts) + " Z"

W, H = 760, 1050
CX, CY = W/2, 470
R_C, R_A, R_S = 92, 68, 50
AP_C, AP_A, AP_S = R_C*0.87, R_A*0.87, R_S*0.87
R1X, R1Y = 205, 235
R2X, R2Y = 322, 412
def pos(deg, rx, ry):
    a = math.radians(deg)
    return CX + rx*math.cos(a), CY + ry*math.sin(a)
def dist(p1, p2): return math.hypot(p2[0]-p1[0], p2[1]-p1[1])
def vis_mid(p1, p2, r1, r2):
    L = dist(p1, p2)
    t = (L + r1 - r2) / (2*L)
    return (p1[0]+(p2[0]-p1[0])*t, p1[1]+(p2[1]-p1[1])*t)

BRAND = {'hubspot':'#ff7a59','snowflake':'#29B5E8'}
anchors = [
    ("Salesforce", 'r', 'salesforce-cloud', 270),
    ("HubSpot", 's', 'hubspot', 330),
    ("Snowflake", 's', 'snowflake', 30),
    ("Stripe", 'badge', 'stripe', 90),
    ("Mulesoft", 'r', 'mulesoft', 150),
    ("Dynamics", 'r', 'microsoft', 210),
]
sats = [
    ("Zendesk",'zendesk', 262, 0), ("Intercom",'intercom', 290, 0), ("n8n",'n8n', 240, 0),
    ("Calendly",'calendly', 312, 1), ("Zapier",'zapier', 348, 1), ("Mixpanel",'mixpanel', 8, 1),
    ("Airbyte",'airbyte', 36, 2), ("Looker",'looker', 62, 2), ("Metabase",'metabase', 84, 2),
    ("Make",'make', 174, 5),
    ("Anthropic",'anthropic', 120, 'C'),
]
apos = [pos(d, R1X, R1Y) for *_, d in anchors]
spos = [pos(d, R2X, R2Y) for _,_,d,_ in sats]

parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{SANS}" role="img" aria-labelledby="hxtm hxdm" text-rendering="geometricPrecision"><title id="hxtm">The APX cross-layer</title><desc id="hxdm">Network diagram: APX at the center, connected to six platforms and their surrounding tools.</desc>']
parts.append('''<defs>
<linearGradient id="hxgm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8E2DE2"/><stop offset="1" stop-color="#4A00E0"/></linearGradient>
<radialGradient id="hglowm" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8E2DE2" stop-opacity="0.28"/><stop offset="1" stop-color="#8E2DE2" stop-opacity="0"/></radialGradient>
</defs>''')
parts.append(f'<ellipse cx="{CX}" cy="{CY}" rx="330" ry="380" fill="url(#hglowm)"/>')
for x,y in apos:
    parts.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="#8E2DE2" stroke-width="2" opacity="0.6"/>')
for (label, icon, deg, tgt), (x,y) in zip(sats, spos):
    if tgt == 'C':
        parts.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="#a78bfa" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.9"/>')
    else:
        tx, ty = apos[tgt]
        parts.append(f'<line x1="{tx:.1f}" y1="{ty:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="#4A00E0" stroke-width="1.5" opacity="0.5"/>')
for i in range(6):
    mx,my = vis_mid((CX,CY), apos[i], AP_C, AP_A)
    parts.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="4.2" fill="#34d399"/><circle cx="{mx:.1f}" cy="{my:.1f}" r="8" fill="#34d399" opacity="0.25"/>')
ring_pts = [
    vis_mid(apos[0], spos[1], AP_A, AP_S),
    vis_mid(apos[1], spos[3], AP_A, AP_S),
    vis_mid(apos[2], spos[7], AP_A, AP_S),
]
for mx,my in ring_pts:
    parts.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="5.2" fill="#0f172a" stroke="#fb7185" stroke-width="2.5"/>')
for (label, icon, deg, tgt), (x,y) in zip(sats, spos):
    parts.append(f'<path d="{hexpath(x, y, R_S)}" fill="#141d33" stroke="rgba(255,255,255,0.13)" stroke-width="1.2"/>')
    parts.append(si_icon(icon, x, y-11, 23, '#ffffff', 0.72))
    parts.append(f'<text x="{x:.1f}" y="{y+23:.1f}" text-anchor="middle" font-size="14.5" font-weight="600" fill="#94a3b8">{label}</text>')
for (label, kind, name, deg), (x,y) in zip(anchors, apos):
    parts.append(f'<path d="{hexpath(x, y, R_A)}" fill="#1c2740" stroke="url(#hxgm)" stroke-width="2.2"/>')
    if kind == 's':
        parts.append(si_icon(name, x, y-14, 28, BRAND.get(name, '#e2e8f0')))
    elif kind == 'badge':
        parts.append(f'<rect x="{x-15:.1f}" y="{y-29:.1f}" width="30" height="30" rx="7" fill="#635BFF"/>')
        parts.append(si_icon(name, x, y-14, 19, '#ffffff'))
    else:
        parts.append(repo_img(name, x, y-14, 34 if 'salesforce' in name else 28))
    parts.append(f'<text x="{x:.1f}" y="{y+28:.1f}" text-anchor="middle" font-size="16" font-weight="700" fill="#e2e8f0">{label}</text>')
parts.append(f'<path d="{hexpath(CX, CY, R_C)}" fill="url(#hxgm)" stroke="#ffffff" stroke-width="2"/>')
parts.append(f'<text x="{CX}" y="{CY+11}" text-anchor="middle" font-size="36" font-weight="800" letter-spacing="-0.5" fill="#ffffff">APX.</text>')
parts.append(f'<text x="{CX}" y="{H-58}" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#94a3b8"><tspan fill="#34d399">●</tspan> monitored platform&#160;&#160;<tspan fill="#fb7185">○</tspan> found in a typical audit</text>')
parts.append(f'<text x="{CX}" y="{H-30}" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#94a3b8"><tspan fill="#a78bfa" font-weight="700">╌╌</tspan> custom AI workflows</text>')
parts.append('</svg>')
pathlib.Path('hexnet-mobile.svg').write_text("\n".join(parts))

# Geometrie-Checks
nodes = [(x,y,R_S) for x,y in spos] + [(x,y,R_A) for x,y in apos] + [(CX,CY,R_C)]
worst = 1e9; pair = None
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        g = dist(nodes[i][:2], nodes[j][:2]) - nodes[i][2] - nodes[j][2]
        if g < worst: worst, pair = g, (i,j)
print("min gap:", round(worst,1), pair)
xs = [x for x,y in spos]; ys = [y for x,y in spos]
print("bounds x:", round(min(xs)-R_S,1), round(max(xs)+R_S,1), "y:", round(min(ys)-R_S,1), round(max(ys)+R_S,1), f"(canvas {W}x{H})")
print("hexnet-mobile geschrieben")
