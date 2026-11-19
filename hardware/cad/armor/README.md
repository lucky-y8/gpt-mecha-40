# Original slim-knight armor CAD

This directory will contain GPT-Mecha-owned armor parts. It must not contain unmodified upstream cover files presented as original work.

## First design modules

1. Helmet / visor
2. Chest front and rear
3. Left / right shoulder shells
4. Abdomen and waist / side skirts
5. Left / right thigh shells
6. Knee guards
7. Left / right shin shells
8. Foot cosmetic covers
9. Removable backpack shell

## CAD constraints

- Reference skeleton is the load-bearing structure.
- Armor is non-structural in V1.
- Define joint swept-volume keep-out regions before modeling each panel.
- Preserve service access to servo cases, output horns, connectors and screws.
- Keep camera field of view, microphone openings, speaker ports and ventilation clear.
- Do not cover foot-contact switches or change the support polygon.
- Assign material and density to each panel and export a mass-properties report.
- Recheck the MuJoCo model and policy after each mass-distribution change.

## First printable fit-checks

Do not print the full armor set first. Start with:
- one knee guard,
- one shin side panel,
- one ankle / foot cover,
- one chest access panel.

These are fit checks only until the reference STEP is available and joint interference is measured.
