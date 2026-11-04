"""Builds map/index.html for fleetacademy.ai/map from the v3 sources: head, body, legend, app and data, wrapped as a full page."""
import re, sys
from pathlib import Path
H = Path(__file__).resolve().parent / "src"
body = (H / "body.html").read_text()
legend = (H / "legend.html").read_text()
body = re.sub(r'<div class="legend">.*?</p>', legend, body, flags=re.S)
body = body.replace("Pick a role to see its path, and how much of that job agents can be trusted with today.", "Roles sit on the rim. Pick one to light its path, and see how much of that job agents can be trusted with today.")
body = body.replace("Search 923 jobs: sales, accountant, nurse, developer…", "Search roles and 923 jobs: account executive, accountant, nurse…")
body = body.replace("      <h1>Every Job on the Map</h1>", '      <a class="home" href="/">Fleet Academy</a>\n      <h1>Every Job on the Map</h1>', 1)
head = (H / "head.html").read_text().replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = head.replace(".src a { color: var(--ink-muted); }\n", ".src a { color: var(--ink-muted); }\n.home { display: inline-block; margin-bottom: 6px; font: 600 13px/1.4 var(--sans); color: var(--green-hi); text-decoration: none; letter-spacing: .02em; }\n.home:hover, .home:focus-visible { text-decoration: underline; }\n", 1)
js = (H / "app.js").read_text().replace("__DATA__", (H / "map.json").read_text())
top = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       '<meta name="description" content="Every requirement of every job, from O*NET, as one map, with the Fleet Academy skills that cover it.">\n')
out = Path(sys.argv[1]) if len(sys.argv) > 1 else H.parent / "index.html"
out.write_text(top + head + body + "<script>\n" + js + "\n</script>\n</html>\n")
print(out, out.stat().st_size)
