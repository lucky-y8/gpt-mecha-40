# Mechanical reference adaptation

## Goal

Use Open Duck Mini V2 as a reference skeleton and locomotion baseline while designing an original, removable knight-style armor shell.

## Non-negotiable rule

Do not scale the complete robot STL to force a 40 cm height. Servos, bearings, fasteners and joint clearances do not scale. The upstream project describes approximately 42 cm with legs extended; accept the reference scale initially and measure the actual CAD envelope.

## Reference joints

The upstream assembly guide and runtime must be reconciled before procurement. The reference assembly describes:
- Left leg: hip yaw, hip roll, hip pitch, knee and ankle (5 actuators).
- Right leg: same (5 actuators).
- Head/neck mechanism: 4 actuators.
- Reference total: 14 actuators.

Do not assume a 12-DOF leg layout. Do not add ankle roll or extra leg joints without redoing kinematics, simulation and policy validation.

## Armor design rules

1. Armor is cosmetic and non-load-bearing in V1.
2. Keep actuator cases, output shafts, horn screws and service connectors accessible.
3. Define joint swept-volume keep-out regions from CAD motion studies.
4. Avoid hard edges near moving joints and cable paths.
5. Use removable fasteners; avoid permanently bonding armor to the skeleton.
6. Keep head, shoulder and backpack additions light and close to the body.
7. Add armor mass only after measuring the baseline robot mass and center of mass.
8. Rebuild the simulation model with measured printed-part masses and inertias.

## Proposed armor modules

- head helmet and faceplate
- chest front / chest rear
- left and right shoulder armor
- abdomen cover
- waist / side skirts
- left and right thigh shells
- knee guards
- left and right shin shells
- foot armor
- removable backpack shell

## CAD workflow

1. Obtain the native upstream Onshape design and record its document/version identifiers.
2. Export a read-only reference STEP assembly and original print STLs.
3. Create a separate original CAD project; do not overwrite upstream geometry.
4. Add armor as separate components around the reference skeleton.
5. Check joint motion at minimum, nominal and maximum positions.
6. Check access to all screws, motor cables, IMU and battery.
7. Export armor-only STEP and STL files.
8. Print one representative joint cover and one foot/ankle fit-check.
9. Measure fit and revise before printing a full set.

## Required deliverables

- native editable CAD source
- skeleton reference STEP
- armor STEP assembly
- individual armor STLs
- front / side / rear drawings
- exploded assembly drawing
- joint keep-out and cable routing drawings
- mass properties report
- print orientation and material notes

No dimensions in this document are manufacturing-ready. Derive final dimensions from the actual CAD and physical components.
