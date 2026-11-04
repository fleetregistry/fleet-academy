# Every Job on the Map

`index.html` is the public map served at https://fleetacademy.ai/map.

- **Requirements:** O*NET 31.0, US Department of Labor, Employment and Training Administration, licensed CC BY 4.0.
- **Skills and provings:** this repo. Each skill's state (built, held, Hallmarked, Hallmarked for small engines) comes from its newest results file.
- **Placement:** each skill is placed on the requirements it covers by hand. That placement is a first pass.

**To change the map,** edit the files in `src/` and run `python3 map/build.py`, which writes `index.html`.

**Getting around:** drag to move; scroll, pinch or double-tap to zoom (shift and double-click zooms out); the minimap shows where you are once you zoom in. Keys, when the map has focus: + and − zoom, 0 shows the whole map, the arrows move, F goes full screen, I shows or hides the card in full screen, Esc leaves.

fleetacademy.ai reads this file from the `main` branch, so a change merged here shows on the site within a few minutes.
