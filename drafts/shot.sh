#!/bin/bash
for d in "$@"; do google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1440,2400 --virtual-time-budget=3000 --screenshot="$PWD/$d/screenshot.png" "file://$PWD/$d/index.html" 2>/dev/null; done
