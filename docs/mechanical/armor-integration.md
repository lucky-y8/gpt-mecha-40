# Slim-knight armor integration plan

## Visual direction

GPT-Mecha 40 uses the selected **C — slim knight** silhouette:
- narrow shoulders and waist
- long-leg visual language
- sharp, layered armor edges
- white/silver primary armor, navy secondary armor and cyan accents
- original helmet, visor and chest-core design
- removable, serviceable armor modules

This is an original design direction. Do not reproduce an existing anime character's exact head, crest, emblems, silhouette or proprietary model.

## Structural rule

The Open Duck Mini V2 reference skeleton remains the load-bearing structure for the first adaptation. Armor is non-structural and must not carry actuator loads or replace servo mounts.

Do not alter the reference link lengths, joint axes, horn offsets, actuator mounts or foot support geometry in the first armor iteration.

## Armor module plan

| Module | Design intent | Integration constraint |
|---|---|---|
| Helmet / visor | Knight helmet, cyan eyes, camera aperture | Preserve four-axis head mechanism travel and camera FOV |
| Chest front | Narrow V-shaped chest armor, cyan core | Removable; preserve speaker openings, compute access and ventilation |
| Chest rear | Slim back shell | Preserve USB, power and service access |
| Shoulders | Narrow layered pauldrons | Must clear neck and arm/antenna motion; keep mass close to torso |
| Waist / side skirts | Narrow waist and light side armor | Must clear hip yaw/roll sweep |
| Thigh shells | Long-leg visual proportion | Must clear hip pitch and knee movement |
| Knee guards | Small sharp knight-style guards | Must not collide at maximum flexion |
| Shin shells | Layered tapered shin armor | Must clear knee/ankle and foot-contact switches |
| Foot armor | Knight-style toe/heel covers | Must not reduce support polygon, alter sole friction or block switches |
| Backpack | Slim removable expansion shell | V1 decorative only; no flight hardware |

## Design workflow

1. Import the pinned upstream Onshape design as a read-only reference.
2. Record the exact document/version and export a STEP assembly.
3. Create a separate original CAD assembly for GPT-Mecha armor.
4. Define joint swept volumes using the reference axes and simulated limits.
5. Place armor outside all keep-out volumes.
6. Keep screws, connectors, servo cases and cable paths accessible.
7. Assign material and density to each panel.
8. Export a mass-properties report for every panel and the complete armored robot.
9. Add those masses and inertias to the MuJoCo model.
10. Print one representative knee/shin cover and one chest access panel before a full print batch.

## Materials and mass

Candidate materials:
- PETG for first armor prototypes.
- PLA for low-load cosmetic mockups.
- TPU only for compliant bumpers or sole interfaces where appropriate.
- Metal or reinforced engineering material only where the mechanical engineer verifies a structural need.

Armor mass budget is **not yet set**. First measure the unarmored reference robot. Then define a mass allowance by body segment, with particular caution for head, upper torso and backpack because added mass there changes balance and joint torque.

## Required CAD deliverables

- editable native CAD source
- armor-only STEP assembly
- individual STL files
- front, side, rear and isometric views
- exploded armor view
- joint swept-volume / keep-out overlays
- cable-routing and service-access drawings
- material, print orientation and slicer mass report
- updated MJCF with measured mass/inertia

## Existing community reference

Open Duck Mini V2 contains a community body-cover mod by Jaime Machuca under `print/mods/v2_Jaimes_Mods`. It demonstrates body/leg covers and cable guides. Its README warns that changed mass distribution may reduce stability with the original policy. Treat it as an integration reference only; retain attribution if any of its files are reused. It is not the GPT-Mecha armor design.
