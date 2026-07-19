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

W, H = 1120, 700
CX, CY = W/2, 344
R_C, R_A, R_S = 76, 55, 38            # three hard size tiers
AP_C, AP_A, AP_S = R_C*0.87, R_A*0.87, R_S*0.87   # hex apothems (visible edge radius)
R1X, R1Y = 218, 172                    # anchor ellipse
R2X, R2Y = 420, 280                    # satellite ellipse
def pos(deg, rx, ry):
    a = math.radians(deg)
    return CX + rx*math.cos(a), CY + ry*math.sin(a)
def dist(p1, p2): return math.hypot(p2[0]-p1[0], p2[1]-p1[1])
def vis_mid(p1, p2, r1, r2):
    """midpoint of the VISIBLE segment between two hex nodes (edges hidden under hexes)"""
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
    ("Dynamics 365", 'r', 'microsoft', 210),
]
# satellites: (label, icon, angle, target_anchor_index or 'C')
sats = [
    ("Zendesk",'zendesk', 262, 0), ("Intercom",'intercom', 290, 0), ("n8n",'n8n', 240, 0),
    ("Calendly",'calendly', 312, 1), ("Zapier",'zapier', 342, 1), ("Mixpanel",'mixpanel', 8, 1),
    ("Airbyte",'airbyte', 36, 2), ("Looker",'looker', 62, 2), ("Metabase",'metabase', 84, 2),
    ("Make",'make', 174, 5),
    ("Anthropic",'anthropic', 120, 'C'),
]
apos = [pos(d, R1X, R1Y) for *_, d in anchors]
spos = [pos(d, R2X, R2Y) for _,_,d,_ in sats]

parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{SANS}" role="img" aria-labelledby="hxt hxd" text-rendering="geometricPrecision"><title id="hxt">The APX cross-layer</title><desc id="hxd">Network diagram: APX at the center, connected to six platforms (Salesforce, HubSpot, Dynamics 365, Snowflake, Stripe, Mulesoft) and their surrounding tools. Markers show monitored platforms and typical audit findings.</desc>']
parts.append('''<defs>
<linearGradient id="hxg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8E2DE2"/><stop offset="1" stop-color="#4A00E0"/></linearGradient>
<radialGradient id="hglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8E2DE2" stop-opacity="0.28"/><stop offset="1" stop-color="#8E2DE2" stop-opacity="0"/></radialGradient>
<pattern id="dotgrid" x="5" y="1" width="46" height="46" patternUnits="userSpaceOnUse"><circle cx="23" cy="23" r="1" fill="#334155" opacity="0.3"/></pattern>
</defs>''')
parts.append('<rect x="0" y="0" width="%d" height="%d" fill="url(#dotgrid)"/>' % (W, H-40))
parts.append(f'<ellipse cx="{CX}" cy="{CY}" rx="320" ry="240" fill="url(#hglow)"/>')

# spokes center->anchors (all six)
for x,y in apos:
    parts.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="#8E2DE2" stroke-width="1.5" opacity="0.6"/>')
# satellite edges (explicit targets); Anthropic->center one step brighter
for (label, icon, deg, tgt), (x,y) in zip(sats, spos):
    if tgt == 'C':
        parts.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="#a78bfa" stroke-width="1.4" stroke-dasharray="7 5" opacity="0.9"/>')
    else:
        tx, ty = apos[tgt]
        parts.append(f'<line x1="{tx:.1f}" y1="{ty:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="#4A00E0" stroke-width="1.1" opacity="0.5"/>')

# green sync dots at visible-segment midpoint of five anchor spokes
for i in range(6):
    mx,my = vis_mid((CX,CY), apos[i], AP_C, AP_A)
    parts.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="3.2" fill="#34d399"/><circle cx="{mx:.1f}" cy="{my:.1f}" r="6.2" fill="#34d399" opacity="0.25"/>')
# audit rings, all hard on visible-segment midpoints:
# Stripe spoke (payment status back to CRM), HubSpot->Calendly, Snowflake->Looker
ring_pts = [
    vis_mid(apos[0], spos[1], AP_A, AP_S),
    vis_mid(apos[1], spos[3], AP_A, AP_S),
    vis_mid(apos[2], spos[7], AP_A, AP_S),
]
for mx,my in ring_pts:
    parts.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="4" fill="#0f172a" stroke="#fb7185" stroke-width="2"/>')

# satellites (monochrome, 72%)
for (label, icon, deg, tgt), (x,y) in zip(sats, spos):
    parts.append(f'<path d="{hexpath(x, y, R_S)}" fill="#141d33" stroke="rgba(255,255,255,0.13)" stroke-width="1"/>')
    parts.append(si_icon(icon, x, y-8, 17, '#ffffff', 0.72))
    parts.append(f'<text x="{x:.1f}" y="{y+17:.1f}" text-anchor="middle" font-size="10" font-weight="600" fill="#94a3b8" opacity="0.85">{label}</text>')
# anchors (brand treatment)
for (label, kind, name, deg), (x,y) in zip(anchors, apos):
    parts.append(f'<path d="{hexpath(x, y, R_A)}" fill="#1c2740" stroke="url(#hxg)" stroke-width="1.75"/>')
    if kind == 's':
        parts.append(si_icon(name, x, y-11, 22, BRAND.get(name, '#e2e8f0')))
    elif kind == 'badge':
        # Stripe: app-icon badge so the S reads as brand mark, not set type
        parts.append(f'<rect x="{x-12:.1f}" y="{y-23:.1f}" width="24" height="24" rx="5.5" fill="#635BFF"/>')
        parts.append(si_icon(name, x, y-11, 15, '#ffffff'))
    else:
        parts.append(repo_img(name, x, y-11, 27 if 'salesforce' in name else 22))
    fs = 11 if len(label) > 10 else 11.5
    parts.append(f'<text x="{x:.1f}" y="{y+22:.1f}" text-anchor="middle" font-size="{fs}" font-weight="700" fill="#e2e8f0">{label}</text>')
# center
parts.append(f'<path d="{hexpath(CX, CY, R_C)}" fill="url(#hxg)" stroke="#ffffff" stroke-width="2.5"/>')
parts.append(f'<text x="{CX}" y="{CY+9}" text-anchor="middle" font-size="30" font-weight="800" letter-spacing="-0.5" fill="#ffffff">APX.</text>')
# legend: centered, tight under graphic
parts.append(f'<text x="{CX}" y="{H-14}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#94a3b8"><tspan fill="#34d399">●</tspan> monitored platform&#160;&#160;&#160;<tspan fill="#fb7185">○</tspan> found in a typical audit&#160;&#160;&#160;<tspan fill="#a78bfa" font-weight="700">╌╌</tspan> custom AI workflows</text>')
parts.append('</svg>')
pathlib.Path('hexnet.svg').write_text("\n".join(parts))

# geometry self-checks
def pt_line_dist(p, a, b):
    ax,ay = a; bx,by = b; px,py = p
    dx,dy = bx-ax, by-ay
    t = max(0, min(1, ((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
    return math.hypot(px-(ax+t*dx), py-(ay+t*dy))
anth = spos[10]
print("anthropic line clearance mulesoft:", round(pt_line_dist(apos[4], anth, (CX,CY)) - R_A, 1))
print("anthropic line clearance stripe:", round(pt_line_dist(apos[3], anth, (CX,CY)) - R_A, 1))
print("metabase edge clearance stripe:", round(pt_line_dist(apos[3], apos[2], spos[8]) - R_A, 1))
print("n8n edge clearance dynamics:", round(pt_line_dist(apos[5], apos[0], spos[2]) - R_A, 1))
print("make edge clearance mulesoft:", round(pt_line_dist(apos[4], apos[5], spos[9]) - R_A, 1))
print("mixpanel edge clearance snowflake:", round(pt_line_dist(apos[2], apos[1], spos[5]) - R_A, 1))
# min node separation
nodes = [(x,y,R_S) for x,y in spos] + [(x,y,R_A) for x,y in apos] + [(CX,CY,R_C)]
worst = 1e9
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        gap = dist(nodes[i][:2], nodes[j][:2]) - nodes[i][2] - nodes[j][2]
        worst = min(worst, gap)
print("min hex-to-hex gap:", round(worst,1))
# canvas bounds
ymin = min(y-R_S for x,y in spos); ymax = max(y+R_S for x,y in spos)
print("sat y range:", round(ymin,1), round(ymax,1), "(canvas 0..", H, ")")
print("hexnet v4 written")
