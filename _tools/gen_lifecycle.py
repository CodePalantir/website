#!/usr/bin/env python3
"""Generates _includes/sections/lifecycle-mobius.html (the Revenue Lifecycle section).

The ribbon is a distorted Gerono lemniscate rendered as ~200 shaded quads so the
strip has a light front face and a dark back face that exchange at the crossover:
that shading is what makes the Mobius twist legible. Nodes are small on-ribbon
dots (numbers live in the labels), the arrow docks at each node (travel > dwell
> depart, pause on hover), and the ribbon draws itself in on first view.

Run from repo root:  python3 _tools/gen_lifecycle.py
"""
import math, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_includes", "sections", "lifecycle-mobius.html")

# ---------------- geometry ----------------
cx, cy = 210, 292
RX, RY = 150, 222
N = 600
TSTART = math.pi / 2          # path starts at the crossover so the seam hides there

def P(t):
    c = -math.cos(t)                      # +1 at top, -1 at bottom
    w = 1 + 0.20 * c + 0.10 * c * abs(c)  # top lobe ~+30% wide, bottom tucked (smooth)
    h = 1 + 0.07 * c
    sk = 10 * math.sin(t)                 # gentle organic skew
    return (cx + RX * math.sin(2 * t) * w + sk, cy + RY * math.cos(t) * h)

def basehalf(t):
    return 30 * (0.30 + 0.70 * abs(math.cos(t)))

ts = [TSTART + 2 * math.pi * i / N for i in range(N + 1)]
pts = [P(t) for t in ts]
Le, Re = [], []
for i, t in enumerate(ts):
    a = pts[(i + 1) % (N + 1)]; b = pts[(i - 1) % (N + 1)]
    tx, ty = a[0] - b[0], a[1] - b[1]; l = math.hypot(tx, ty) or 1
    nx, ny = -ty / l, tx / l
    # clamp half-width by local circumradius so the inner edge can't fold
    ax, ay = b; bx, by = pts[i]; ccx, ccy = a
    dd = 2 * (ax * (by - ccy) + bx * (ccy - ay) + ccx * (ay - by))
    if abs(dd) < 1e-6:
        Rc = 1e9
    else:
        ux = ((ax*ax+ay*ay)*(by-ccy)+(bx*bx+by*by)*(ccy-ay)+(ccx*ccx+ccy*ccy)*(ay-by))/dd
        uy = ((ax*ax+ay*ay)*(ccx-bx)+(bx*bx+by*by)*(ax-ccx)+(ccx*ccx+ccy*ccy)*(bx-ax))/dd
        Rc = math.hypot(ux - bx, uy - by)
    hh = min(basehalf(t), 0.80 * Rc)
    Le.append((pts[i][0] + nx * hh, pts[i][1] + ny * hh))
    Re.append((pts[i][0] - nx * hh, pts[i][1] - ny * hh))

seg = [0.0]
for i in range(1, len(pts)):
    seg.append(seg[-1] + math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]))
Ltot = seg[-1]
uu = [s / Ltot for s in seg]

def u_at_t(t):
    x = ((t - TSTART) % (2*math.pi)) / (2*math.pi) * N; i = int(x); f = x - i
    return (seg[i] + (seg[min(i+1, N)] - seg[i]) * f) / Ltot

def idx_at_u(u):
    u = ((u % 1) + 1) % 1
    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi) // 2
        if uu[mid] < u: lo = mid + 1
        else: hi = mid
    return lo

# ---------------- shading ----------------
TOP = (0xB4, 0x66, 0xF2)   # light violet
BOT = (0x4A, 0x00, 0xE0)   # deep indigo
GREY = (0x3A, 0x2F, 0x52)  # desaturation target for the back face

ys = [p[1] for p in pts]
ymin, ymax = min(ys), max(ys)

def shade(u, ymid):
    # compress the y-ramp so the face shading (the twist cue) carries the contrast
    yn = 0.28 + 0.44 * (ymid - ymin) / (ymax - ymin)
    base = [TOP[i] + (BOT[i] - TOP[i]) * yn for i in range(3)]
    f = 0.70 + 0.52 * (0.5 - 0.5 * math.cos(2 * math.pi * u))  # light at u=.5 (over arm), dark at u=0/1
    out = []
    for i in range(3):
        v = base[i] * f
        if f < 1:  # pull the back face slightly toward grey so it recedes
            mix = (1 - f) * 0.5
            v = v * (1 - mix) + GREY[i] * mix
        out.append(max(0, min(255, round(v))))
    return "#%02X%02X%02X" % tuple(out)

STEP = 3
quads = []          # (u_mid, path_d, fill)
for i in range(0, N, STEP):
    j = min(i + STEP, N)
    d = (f"M {Le[i][0]:.1f} {Le[i][1]:.1f} L {Le[j][0]:.1f} {Le[j][1]:.1f} "
         f"L {Re[j][0]:.1f} {Re[j][1]:.1f} L {Re[i][0]:.1f} {Re[i][1]:.1f} Z")
    umid = (uu[i] + uu[j]) / 2
    ymid = (pts[i][1] + pts[j][1]) / 2
    quads.append((umid, d, shade(umid, ymid)))

def quad_svg(q):
    return f'<path d="{q[1]}" fill="{q[2]}" stroke="{q[2]}" stroke-width="0.7" stroke-linejoin="round"></path>'

OVER_W = 0.085
base_quads = "\n".join(quad_svg(q) for q in quads)
over_quads = "\n".join(quad_svg(q) for q in quads if 0.5 - OVER_W <= q[0] <= 0.5 + OVER_W)

# underpass shadow: rotated ellipse aligned with the UNDER arm, so the visible
# spill lands on the under-arm surface either side of the over arm (contact shadow)
i0, i5 = idx_at_u(0.0), idx_at_u(0.5)
shx = (pts[i0][0] + pts[i5][0]) / 2
shy = (pts[i0][1] + pts[i5][1]) / 2
a1 = pts[min(i0+4, N)]; b1 = pts[max(i0-4, 0)]
sh_ang = math.degrees(math.atan2(a1[1]-b1[1], a1[0]-b1[0]))
# clip the shadow to the under-arm surface so nothing spills onto the page ground
under_clip = "".join(f'<path d="{q[1]}"></path>' for q in quads if q[0] < 0.07 or q[0] > 0.93)
shadow = (f'<clipPath id="lc-und">{under_clip}</clipPath>'
          f'<g clip-path="url(#lc-und)"><ellipse transform="translate({shx:.1f},{shy:.1f}) rotate({sh_ang:.1f})" '
          f'rx="52" ry="22" fill="url(#lc-sh)" opacity="0.5"></ellipse></g>')

# crisp hairline edges on the over arm where it crosses the dark under arm
def edge_slice(edge, lo, hi):
    pp = edge[lo:hi + 1]
    return ('<path d="' + "M " + " L ".join(f"{p[0]:.1f} {p[1]:.1f}" for p in pp) +
            '" fill="none" stroke="#FFFFFF" stroke-width="1" opacity="0.35"></path>')
ov_lo, ov_hi = idx_at_u(0.5 - OVER_W), idx_at_u(0.5 + OVER_W)
highlight = edge_slice(Le, ov_lo, ov_hi) + "\n" + edge_slice(Re, ov_lo, ov_hi)

# ---------------- nodes ----------------
SHORT = ["Attract &|Demand Gen", "Prospecting|& Outbound", "Lead|Management",
         "Selling &|Pipeline", "Quote-to-Cash", "Onboarding|& Success", "Renewal &|Expansion"]

nodes = []
for k in range(7):
    t = math.pi + 2 * math.pi * k / 7
    x, y = P(t)
    nodes.append({"n": k + 1, "u": round(u_at_t(t), 4), "x": round(x, 1), "y": round(y, 1)})

# direction chevrons at inter-node midpoints, away from crossover and nodes
sorted_u = sorted(nd["u"] for nd in nodes)
mids = []
for k in range(len(sorted_u)):
    a, b = sorted_u[k], sorted_u[(k + 1) % len(sorted_u)]
    m = (a + (((b - a) % 1) / 2)) % 1
    near_node = min(min(abs(m - nu), 1 - abs(m - nu)) for nu in sorted_u)
    if abs(m - 0.5) > 0.11 and 0.05 < m < 0.95 and near_node > 0.055:
        mids.append(m)
chev_us = mids[::2][:3] if len(mids) >= 3 else mids
chevrons = ""
for m in chev_us:
    i = idx_at_u(m)
    p = pts[i]; a1 = pts[min(i+3, N)]; b1 = pts[max(i-3, 0)]
    ang = math.degrees(math.atan2(a1[1]-b1[1], a1[0]-b1[0]))
    chevrons += (f'<path transform="translate({p[0]:.1f},{p[1]:.1f}) rotate({ang:.1f})" '
                 f'd="M -3 -5.5 L 4.5 0 L -3 5.5" fill="none" stroke="#FFFFFF" stroke-width="2" '
                 f'stroke-linecap="round" opacity="0.18"></path>\n')

PAD = 52
def esc(s): return s.replace("&", "&amp;")

label_boxes = []
node_svg = ""
for nd in nodes:
    x, y = nd["x"], nd["y"]; k = nd["n"] - 1
    name_lines = SHORT[k].split("|")
    dx, dy = x - cx, y - cy; d = math.hypot(dx, dy) or 1
    if abs(dy) < 72:                       # near crossover height: push horizontally out
        lx = 48 if dx > 0 else -48; ly = 0
    else:
        lx = round(dx / d * PAD); ly = round(dy / d * PAD)
    anchor = "start" if lx > 12 else "end" if lx < -12 else "middle"
    lines = [f"{nd['n']:02d}"] + name_lines
    n_l = len(lines)
    first_y = ly - (n_l - 1) * 9
    tsp = ""
    for li, line in enumerate(lines):
        yy = first_y + li * 18
        cls = "lc-lnum" if li == 0 else "lc-lname"
        tsp += f'<tspan class="{cls}" x="{lx}" y="{yy}">{esc(line)}</tspan>'
    label = f'<text class="lc-label" text-anchor="{anchor}">{tsp}</text>'
    node_svg += f'''      <g class="lc-node" data-i="{nd['n']}" role="button" tabindex="0" aria-label="Phase {nd['n']} of 7: {esc(SHORT[k].replace('|', ' '))}" transform="translate({x},{y})">
        <circle class="lc-hit" r="24" fill="transparent"></circle>
        <circle class="lc-halo" r="22" fill="#8E2DE2"></circle>
        <circle class="lc-dot" r="6" fill="#FFFFFF" stroke="#8E2DE2" stroke-width="2"></circle>
        {label}
      </g>\n'''
    # label bbox estimate for viewBox fitting + collision warnings
    def est_w(line, fs, mono=False): return len(line) * fs * 0.66
    lw = max(est_w(l, 11 if li == 0 else 13.5) for li, l in enumerate(lines))
    if anchor == "start": bx0, bx1 = lx, lx + lw
    elif anchor == "end": bx0, bx1 = lx - lw, lx
    else: bx0, bx1 = lx - lw/2, lx + lw/2
    by0, by1 = first_y - 12, first_y + (n_l - 1) * 18 + 4
    label_boxes.append((x + bx0, y + by0, x + bx1, y + by1, nd["n"]))

# collision warnings: label boxes vs ribbon centerline
warn = 0
for (bx0, by0, bx1, by1, n) in label_boxes:
    corners = [(bx0,by0),(bx1,by0),(bx0,by1),(bx1,by1),((bx0+bx1)/2,(by0+by1)/2)]
    md = min(math.hypot(px-qx, py-qy) for (px,py) in corners for (qx,qy) in pts[::8])
    if md < 16:   # ribbon half-width tops out ~12px near the crossover-height nodes
        print(f"WARN: label {n:02d} within {md:.0f}px of ribbon centerline"); warn += 1

# ---------------- viewBox autofit ----------------
xs_all = [p[0] for p in Le+Re] + [b[0] for b in label_boxes] + [b[2] for b in label_boxes]
ys_all = [p[1] for p in Le+Re] + [b[1] for b in label_boxes] + [b[3] for b in label_boxes]
for nd in nodes:
    xs_all += [nd["x"]-24, nd["x"]+24]; ys_all += [nd["y"]-24, nd["y"]+24]
M = 16
vx, vy = math.floor(min(xs_all))-M, math.floor(min(ys_all))-M
vw, vh = math.ceil(max(xs_all))+M - vx, math.ceil(max(ys_all))+M - vy
AR = f"{vw}/{vh}"

track_d = "M " + " L ".join(f"{p[0]:.1f} {p[1]:.1f}" for p in pts)
DASH = round(Ltot) + 4

# ---------------- copy ----------------
phases = [
 ("Attract & Demand Gen", "Turn attention into intent.",
  "Campaigns, forms and your website wired into one place, with every signal cleanly attributed from first click to closed deal. You see exactly which channels drive pipeline and which just make noise, so budget follows evidence instead of opinion. Nothing slips between marketing and the CRM, and no lead arrives without its history attached."),
 ("Prospecting & Outbound", "The right accounts, reached with a system.",
  "Target lists are built from real fit signals, enriched, deduped and fed into sequences your reps can actually keep up with. Every touch is logged, every reply is routed to the right owner, and nothing gets dropped between tools. Outbound stops being a pile of disconnected tasks and becomes a measurable motion you can tune week over week."),
 ("Lead Management", "No lead waits, and none get lost.",
  "Every lead is routed, scored and assigned the moment it arrives, with SLAs you can actually enforce and escalations that fire on their own. The right rep gets the right lead in minutes, full context already attached, whether it came from a form, a referral or a cold reply. Follow-up stops depending on who remembered to check a queue."),
 ("Selling & Pipeline", "A pipeline your forecast can stand on.",
  "Stages that reflect how buyers really move, a CRM that captures the truth without punishing reps with admin, and forecasts built on clean data instead of gut feel. Deals carry their whole story with them, risk shows up early enough to act on, and leaders walk into the board meeting with numbers they can actually defend."),
 ("Quote-to-Cash", "From yes to paid, without the friction.",
  "Quoting, approvals, billing and revenue recognition are connected end to end, so a closed deal flows straight through to cash without being rekeyed three times. Discounts stay inside guardrails, invoices go out right the first time, and month-end close stops producing surprises. Finance and revenue finally read from one source of truth."),
 ("Onboarding & Success", "Start strong, and stay longer.",
  "New customers land in structured onboarding instead of an inbox, health signals surface risk while there is still time to act, and success playbooks fire before accounts go quiet. The handoff from sales is clean, the data follows the customer through every stage, and your best logos turn into references instead of quiet churn."),
 ("Renewal & Expansion", "Grow the accounts you already have.",
  "Renewals are tracked and forecast long before they land on the calendar, expansion signals surface while the timing is still right, and churn risk is caught early enough to do something about it. Retention becomes a number you can plan around instead of a fire drill, and the loop feeds straight back into new demand."),
]

items = ""
for i, (title, sub, body) in enumerate(phases):
    items += f'''        <article class="lc-item" data-i="{i+1}">
          <h3 class="lc-item-title" style="text-wrap:balance">{title}</h3>
          <p class="lc-item-sub">{sub}</p>
          <p class="lc-item-body">{body}</p>
        </article>\n'''

nodes_js = json.dumps([{"i": nd["n"], "u": nd["u"]} for nd in nodes])

# ---------------- SVG ----------------
svg = f'''<svg class="lc-svg" viewBox="{vx} {vy} {vw} {vh}" role="img" aria-label="The revenue lifecycle as one continuous Mobius loop of seven phases.">
      <defs>
        <radialGradient id="lc-sh" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#1C0940" stop-opacity="0.55"></stop><stop offset="1" stop-color="#1C0940" stop-opacity="0"></stop></radialGradient>
        <linearGradient id="lc-tail" x1="-38" y1="0" x2="-6" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"></stop><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.55"></stop></linearGradient>
        <filter id="lc-aglow" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#2A0A5E" flood-opacity="0.35"></feDropShadow></filter>
        <mask id="lc-rvl" maskUnits="userSpaceOnUse" x="{vx}" y="{vy}" width="{vw}" height="{vh}">
          <path class="lc-msk-stroke" d="{track_d}" fill="none" stroke="#FFFFFF" stroke-width="84" stroke-linecap="round" stroke-dasharray="{DASH}" stroke-dashoffset="0"></path>
        </mask>
      </defs>
      <g mask="url(#lc-rvl)">
{base_quads}
{shadow}
{over_quads}
{highlight}
<path class="lc-stream" d="{track_d}" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" stroke-dasharray="3 22" opacity="0.18"></path>
<g class="lc-chevs">
{chevrons}</g>
      </g>
      <path id="lc-track" d="{track_d}" fill="none" stroke="none"></path>
      <g class="lc-nodes">
{node_svg}      </g>
      <g id="lc-arrow" aria-hidden="true">
        <path d="M -38 0 L -7 4.6 L -7 -4.6 Z" fill="url(#lc-tail)"></path>
        <path d="M 12 0 L -8 9 L -3.5 0 L -8 -9 Z" fill="#FFFFFF" filter="url(#lc-aglow)"></path>
      </g>
    </svg>'''

# ---------------- CSS / JS (plain strings, token substitution) ----------------
css = '''
  .lc-stage { display:flex; align-items:flex-start; justify-content:center; }
  .lc-svg { width:100%; height:auto; aspect-ratio:__AR__; max-height:min(62vh,560px); display:block; margin-inline:auto; overflow:visible; }
  @media (max-width:1023px) { .lc-svg { max-height:min(52vh,460px); } }
  /* on small screens the scaled-down names would render ~8px; numbers carry the
     mapping (the reader below shows number + name) */
  @media (max-width:639px) {
    .lc-lname { display:none; }
    .lc-lnum { font-size:17px; }
  }

  .lc-node { cursor:pointer; outline:none; }
  .lc-dot { transition:r .35s cubic-bezier(.2,.8,.2,1), stroke-width .3s ease; }
  .lc-node.is-active .lc-dot { r:9px; stroke-width:2.5; }
  .lc-node:hover .lc-dot, .lc-node:focus-visible .lc-dot { stroke-width:3.25; }
  .lc-halo { opacity:0; transform-box:fill-box; transform-origin:center; transform:scale(.5); transition:opacity .45s ease, transform .45s ease; }
  .lc-node.is-active .lc-halo { opacity:.14; transform:scale(1); }
  .lc-node:focus-visible .lc-halo { opacity:.2; transform:scale(1); }
  .lc-lnum { font-family:ui-monospace,monospace; font-weight:700; font-size:11px; letter-spacing:.08em; fill:#8E2DE2; }
  .lc-lname { font-weight:600; font-size:13.5px; fill:var(--color-muted); }
  .lc-label tspan { transition:fill .35s ease, opacity .35s ease, font-size .35s ease; }
  .lc-node:not(.is-active) .lc-lnum { opacity:.55; }
  .lc-node:not(.is-active) .lc-lname { opacity:.6; }
  .lc-node:hover .lc-lname, .lc-node:focus-visible .lc-lname { opacity:.95; }
  .lc-node.is-active .lc-lname { fill:var(--color-ink); opacity:1; font-size:14.5px; }
  .lc-node.is-active .lc-lnum { opacity:1; }

  /* one-time draw-on entrance (JS adds .lc-on on first view; no-JS shows everything) */
  .lc-msk-stroke { transition:stroke-dashoffset 1.35s cubic-bezier(.6,.05,.3,.95); }
  html.js #lifecycle:not(.lc-on) .lc-msk-stroke { stroke-dashoffset:__DASH__; }
  .lc-nodes, #lc-arrow { transition:opacity .6s ease; }
  html.js #lifecycle:not(.lc-on) .lc-nodes, html.js #lifecycle:not(.lc-on) #lc-arrow { opacity:0; }
  #lifecycle.lc-on .lc-nodes { transition-delay:.85s; }
  #lifecycle.lc-on #lc-arrow { transition-delay:1.05s; }

  /* phase reader (subordinate to the section H2 above) */
  .lc-stack { display:grid; }
  .lc-item { grid-area:1/1; opacity:0; visibility:hidden; transform:translateY(14px); transition:opacity .55s ease, transform .55s ease; pointer-events:none; }
  .lc-item.is-active { opacity:1; visibility:visible; transform:none; pointer-events:auto; }
  .lc-item-title { font-weight:700; color:var(--color-ink); letter-spacing:-.015em; line-height:1.15; font-size:clamp(1.5rem,2.2vw,2.1rem); }
  .lc-item-sub { margin-top:.75rem; max-width:46ch; font-weight:600; color:var(--color-ink); font-size:1.125rem; line-height:1.45; }
  .lc-item-body { margin-top:.9rem; max-width:54ch; font-size:1.125rem; line-height:1.7; color:var(--color-muted); }

  /* the band flows forward: white ticks drifting along the centerline */
  .lc-stream { animation:lc-flow 1.1s linear infinite; }
  @keyframes lc-flow { to { stroke-dashoffset:-25; } }
  .lc-chevs { display:none; }

  @media (prefers-reduced-motion: reduce) {
    .lc-msk-stroke, .lc-nodes, #lc-arrow, .lc-dot, .lc-halo, .lc-label tspan, .lc-item { transition:none; }
    .lc-stream { animation:none; display:none; }
    .lc-chevs { display:block; }
  }
'''.replace("__AR__", AR).replace("__DASH__", str(DASH))

js = '''
(function(){
  var section=document.getElementById('lifecycle'); if(!section) return;
  var track=section.querySelector('#lc-track');
  var arrow=section.querySelector('#lc-arrow');
  var nodeEls=[].slice.call(section.querySelectorAll('.lc-node'));
  var items=[].slice.call(section.querySelectorAll('.lc-item'));
  var NODES=__NODES__;
  var L=track.getTotalLength();
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover=window.matchMedia&&window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var DWELL=11000, LOOP=56000;   // reduce-mode step interval / full-lap duration
  function ptAt(u){ return track.getPointAtLength((((u%1)+1)%1)*L); }
  function fwd(a,b){ var d=b-a; if(d<0)d+=1; return d; }
  var arrowU=NODES[0].u;
  function placeArrow(u){
    arrowU=((u%1)+1)%1;
    var p=ptAt(arrowU), a=ptAt(arrowU+0.004), b=ptAt(arrowU-0.004);
    var ang=Math.atan2(a.y-b.y,a.x-b.x)*180/Math.PI;
    arrow.setAttribute('transform','translate('+p.x.toFixed(2)+','+p.y.toFixed(2)+') rotate('+ang.toFixed(1)+')');
  }
  var cur=0;
  function activate(k){
    cur=k;
    nodeEls.forEach(function(el){ var on=+el.dataset.i===NODES[k].i; el.classList.toggle('is-active',on); el.setAttribute('aria-current',on?'true':'false'); });
    items.forEach(function(el){ el.classList.toggle('is-active', +el.dataset.i===NODES[k].i); });
  }
  // the phase whose node the arrow passed most recently
  function phaseOf(u){ var bi=0,bd=9; for(var i=0;i<NODES.length;i++){ var d=fwd(NODES[i].u,u); if(d<bd){bd=d;bi=i;} } return bi; }
  activate(0); placeArrow(NODES[0].u);
  var raf=null, running=false, last=null, paused=false;
  var dwellT=0, seek=null;
  function frame(ts){
    if(!running){ raf=null; return; }
    if(last===null) last=ts;
    var dt=Math.min(ts-last,80); last=ts;
    if(seek){
      if(seek.start===null) seek.start=ts;
      var f=Math.min((ts-seek.start)/seek.dur,1);
      var ef=f<.5?2*f*f:1-Math.pow(-2*f+2,2)/2;
      placeArrow(seek.from+fwd(seek.from,seek.to)*ef);
      if(f>=1){ var kk=seek.k; seek=null; activate(kk); }
    } else if(reduce){
      dwellT+=dt;
      if(dwellT>=DWELL){ dwellT=0; var nk=(cur+1)%NODES.length; activate(nk); placeArrow(NODES[nk].u); }
    } else {
      // continuous forward drift; hovering the reader slows it, never stops it
      placeArrow(arrowU + dt/LOOP*(paused?0.25:1));
      var k=phaseOf(arrowU); if(k!==cur) activate(k);
    }
    raf=requestAnimationFrame(frame);
  }
  function start(){ if(running) return; running=true; last=null; if(!raf) raf=requestAnimationFrame(frame); }
  function stop(){ running=false; if(raf){ cancelAnimationFrame(raf); raf=null; } }
  function goTo(nodeI){
    var k=-1; for(var j=0;j<NODES.length;j++) if(NODES[j].i===nodeI) k=j;
    if(k<0) return;
    if(reduce){ activate(k); placeArrow(NODES[k].u); dwellT=0; return; }
    var dist=fwd(arrowU,NODES[k].u);
    seek={from:arrowU,to:NODES[k].u,k:k,dur:Math.max(600,Math.min(2200,dist*L*2.6)),start:null};
    start();
  }
  nodeEls.forEach(function(el){
    el.addEventListener('click',function(){ goTo(+el.dataset.i); });
    el.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); goTo(+el.dataset.i); } });
  });
  var panel=section.querySelector('.lc-panel');
  if(canHover&&panel){
    panel.addEventListener('pointerenter',function(){ paused=true; });
    panel.addEventListener('pointerleave',function(){ paused=false; });
  }
  var seen=false;
  function reveal(){ if(!seen){ seen=true; section.classList.add('lc-on'); } }
  if(reduce) reveal();
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(es){ es.forEach(function(en){
      if(en.isIntersecting){ reveal(); start(); } else stop();
    }); },{threshold:.25}).observe(section);
  } else { reveal(); start(); }
})();
'''.replace("__NODES__", nodes_js)

html = f'''{{%- comment -%}}
  The revenue lifecycle. A distorted vertical Mobius ribbon (procedural,
  regenerate with: python3 _tools/gen_lifecycle.py). Segmented shading gives the
  strip a light front face and a dark back face so the twist actually reads.
  Nodes are on-ribbon dots; the arrow drifts around the loop continuously and
  a phase activates the moment the arrow passes its node. Clicking a node or
  label glides the arrow there. Hovering the reader slows the drift. Ribbon
  draws itself in on first view. Keyboard and reduced-motion safe.
{{%- endcomment -%}}
<section id="lifecycle" class="lc-section apx-section px-6 bg-surface overflow-hidden scroll-mt-24">
  <div class="max-w-wide mx-auto w-full">

    <div class="max-w-[720px] mx-auto text-center rv">
      <span class="apx-eyebrow">The revenue lifecycle</span>
      <h2 class="mt-4 font-bold text-ink tracking-[-0.02em] leading-[1.12] text-[clamp(2rem,3.6vw,3rem)]" style="text-wrap:balance">One loop, from first touch to renewal.</h2>
      <p class="mt-4 mx-auto max-w-[560px] text-lg leading-relaxed text-muted">Revenue is not a funnel that ends at closed won. Every phase feeds the next, and we engineer all seven. Click any phase to explore it.</p>
    </div>

    <div class="lc-grid mt-10 md:mt-14 grid lg:grid-cols-[0.95fr_1.05fr] gap-[clamp(2rem,4vw,4rem)] lg:items-center">

      <div class="lc-panel rv order-2 lg:order-1">
        <div class="lc-stack" aria-live="polite">
{items}        </div>
      </div>

      <div class="lc-stage rv order-1 lg:order-2">
    {svg}
      </div>

    </div>
  </div>
</section>

<style>{css}</style>

<script>{js}</script>
'''

with open(OUT, "w") as fh:
    fh.write(html)
print(f"wrote {OUT}")
print(f"viewBox {vx} {vy} {vw} {vh}  |  track length {Ltot:.0f}px  |  {len(quads)} quads  |  warnings {warn}")
for nd in nodes:
    print(f"  node {nd['n']}  ({nd['x']:.0f},{nd['y']:.0f})  u={nd['u']:.3f}")
