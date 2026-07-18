#!/usr/bin/env bash
# shoot.sh — capture mobile + desktop screenshots of a URL with the system
# Chrome (headless, zero-install). Used to verify design from rendered pixels.
#
# Usage:  scripts/shoot.sh <url> <out-prefix> [full-height-px]
#   scripts/shoot.sh http://127.0.0.1:4000/ design/shots/home
#   -> writes design/shots/home.desktop.png and design/shots/home.mobile.png
set -euo pipefail

URL="${1:?usage: shoot.sh <url> <out-prefix> [height]}"
OUT="${2:?usage: shoot.sh <url> <out-prefix> [height]}"
H="${3:-3200}"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Chrome not found at: $CHROME" >&2; exit 1; }

mkdir -p "$(dirname "$OUT")"
# Chrome writes --screenshot only to an ABSOLUTE path (relative silently fails).
OUTDIR="$(cd "$(dirname "$OUT")" && pwd)"
OUT="$OUTDIR/$(basename "$OUT")"

shoot() { # width height outfile
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size="$1,$2" \
    --virtual-time-budget=3000 \
    --screenshot="$3" "$URL" >/dev/null 2>&1 || true
}

shoot 1440 "$H" "${OUT}.desktop.png"
# Desktop Chrome clamps windows to a ~500px minimum width; asking for 390
# renders a 500px layout cropped to 390. Shoot mobile at 500 (same as the
# design/candidates/*.mobile.png references) so the full layout is captured.
shoot 500  "$H" "${OUT}.mobile.png"
echo "wrote ${OUT}.desktop.png  ${OUT}.mobile.png"
