#!/bin/bash
# Usage: shoot-section.sh <section-id> <WxH> <out.png>
# Extracts one built section from _site/index.html, wraps it with the compiled
# CSS + a simulated 90px fixed header, and screenshots it at the given viewport.
ID="$1"; SIZE="${2:-1440x900}"; OUT="$3"
python3 - "$ID" <<PY > "_site/_shoot_${ID}.html"
import sys
html=open('_site/index.html').read()
sid=sys.argv[1]
i=html.find(f'<section id="{sid}"')
if i<0:
    print("SECTION NOT FOUND"); raise SystemExit
cands=[x for x in [html.find('<section', i+20), html.find('<footer', i+20)] if x>0]
sec=html[i:min(cands)] if cands else html[i:]
hdr='<div style="position:fixed;top:0;left:0;right:0;height:90px;background:rgba(220,0,0,.10);border-bottom:2px dashed rgba(220,0,0,.6);z-index:9999;pointer-events:none;font:11px sans-serif;color:#c00;display:flex;align-items:flex-end;padding:4px 8px">SIMULATED HEADER (90px) — content must clear this and must NOT overflow the bottom of the viewport</div>'
print('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="/assets/css/tailwind.css"><style>body{margin:0}*{transition:none!important;animation:none!important}</style></head><body>'+hdr+sec+'</body></html>')
PY
W="${SIZE%x*}"; H="${SIZE#*x}"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=2000 --window-size=${W},${H} --screenshot="$OUT" "http://127.0.0.1:4000/_shoot_${ID}.html" >/dev/null 2>&1
echo "shot $ID @ ${SIZE} -> $OUT"
