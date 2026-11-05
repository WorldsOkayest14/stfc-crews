"""Rebuild incursion-pvp.html from src/pvp/template.html + src/pvp/data.json.

Run from the repository root:  python3 src/pvp/build.py
Adds the GitHub-only pieces (document skeleton, Home button, Red Alert switch).
data.json was produced by the original data pipeline (M92 Cheat Sheet, M87 crews,
Blue's Crews, stfc.phd ship/tech/officer data); edit it directly for small changes.
"""
import pathlib
root = pathlib.Path(__file__).resolve().parents[2]
src = root / 'src' / 'pvp'
page = (src / 'template.html').read_text().replace('/*DATA*/', (src / 'data.json').read_text(), 1)
switch = ('<a class="homelink" href="./" aria-label="Home">◂<span class="hl"> Home</span></a>\n      '
          '<a class="ra" href="crew-guide.html" title="Red alert is on. Tap to go back to the everyday guide." '
          'aria-label="Red alert is on. Go back to the everyday guide."><span class="knob" aria-hidden="true"></span>'
          '<span id="alertTag">Red alert</span></a>')
site = page.replace('<span class="alert" id="alertTag">Red alert</span>', switch, 1)
assert site != page, 'header marker not found'
marker = '<div class="chips" id="fixF"'
assert marker in site, 'fix tab marker not found'
site = site.replace(marker, '<p class="lead">Lost a specific fight? <a href="lose.html">Upload its combat log</a> and get the answer for that fight.</p>\n      ' + marker, 1)
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>\n')
i = site.index('<div class="lc">')
(root / 'incursion-pvp.html').write_text(head + site[:i] + '</head>\n<body>\n' + site[i:] + '\n</body>\n</html>\n')
print('built incursion-pvp.html')
