"""Copy the species looks from the PvP page into the Hostile Crew Guide.

The PvP template (src/pvp/template.html) is the source of truth for the looks.
This copies every :root[data-skin="..."] rule that styles the shared LCARS frame
(corner, top bar, rail, section headers, buttons) into crew-guide.html, between
the looks:start / looks:end markers. Rules that style PvP-only parts (crew
panels, roster rows, mode buttons) are left out; the guide's own versions live
in its <style id="looks"> block.

Run from the repo root:  python3 src/looks/sync.py
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / 'src/pvp/template.html'
DST = ROOT / 'crew-guide.html'
PVP_ONLY = re.compile(r'\.(crew|off|ship|credit|modes|chips|pill|ab|rank|tools|p-[A-Z]|tri|shipbtn|alert|face|tabs|pick|dtog|usebtn|needhelp|grpbox)\b')
START, END = '/* looks:start */', '/* looks:end */'

css = SRC.read_text()
css = css[css.index('/* ---- species looks'):]
css = css[:css.index('[hidden]{display:none!important}')]

out, i = [], 0
for m in re.finditer(r'\s*(?:(/\*.*?\*/)|([^{}/]+)\{([^{}]*)\})', css, re.S):
    if m.group(1):
        if 'Shared shape system' not in m.group(1):
            out.append(m.group(1).strip())
        continue
    sels = [s.strip() for s in m.group(2).split(',')]
    keep = [s for s in sels if s.startswith(':root[data-skin=') and not PVP_ONLY.search(s)]
    if keep:
        out.append(','.join(keep) + '{' + m.group(3).strip() + '}')

block = START + '\n' + '\n'.join(out) + '\n' + END
page = DST.read_text()
a, b = page.index(START), page.index(END) + len(END)
DST.write_text(page[:a] + block + page[b:])
print(f'{len(out)} rules/comments copied into {DST.name}')
