# Example Notes From This Conversation: PE250x400 Jaw Crusher

Use these notes only as an example pattern, not as universal values.

## Extracted source values

- feed opening: 250 x 400 mm
- discharge opening adjustment range: 20 to 80 mm
- target capacity: 5 to 20 t/h
- jaw plate working size: 400 x 600 mm
- effective cavity height calculation: about 549.5 mm from B=250 mm, e=50 mm, alpha=20 degrees
- selected jaw plate height: 600 mm with tooth/wear allowance
- lower jaw horizontal stroke: 12 mm
- eccentricity: 15 mm
- maximum crushing force: 156 kN
- motor: y160l-6, 15 kw, 970 r/min
- main shaft speed: 300 r/min
- v-belt: c type, 6 belts
- small pulley: 180 mm
- large pulley: 580 mm
- belt center distance: 1000 mm
- main journal: 110 mm
- eccentric journal: 130 mm
- flywheel outer diameter: 600 mm
- frame side plate thickness: 16 mm
- toggle plate section: 350 x 30 mm
- pin diameter: 60 mm

## Example modeling supplements

- frame inner width: jaw width + clearance, e.g. 440 mm for a 400 mm jaw plate
- bearing seat and outer bearing dimensions need supplementing if not present in source
- toggle plate hole center distance is not necessarily the same as source section size
- pulley width must be supplemented to fit all belt grooves
- motor outline dimensions may be simplified unless manufacturing-level detail is required

## Example conflict findings

- 600 mm jaw plate total height, 20 degree angle, 250 mm feed opening, and 50 mm average discharge opening are not all simultaneously effective-cavity constraints. Treat about 550 mm as effective crushing height and 600 mm as total plate height with installation/wear margin.
- Minimum discharge opening should be treated as closed-side setting. If the initial model is set to 20 mm and then the moving jaw closes by 12 mm, interference can occur.
- Frame inner width should not equal jaw plate width; add side clearance.
- Use final shaft dimensions from the strength section rather than preliminary torsion-only estimates.
