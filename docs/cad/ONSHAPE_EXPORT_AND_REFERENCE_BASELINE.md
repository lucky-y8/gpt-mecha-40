# Exporting the Open Duck Mini V2 reference CAD

## Why this step is required

The GitHub print guide gives STL names and quantities, while the MuJoCo XML gives joint names, ranges and inertial data. Neither replaces the native mechanical assembly for checking actuator mounting interfaces, bearing sizes, joint axes, fasteners, clearances and armor fit.

The Onshape source linked by the upstream project is:

- Document: https://cad.onshape.com/documents/64074dfcfa379b37d8a47762
- Workspace: 3650ab4221e215a4f65eb7fe
- Element: 0505c262d882183a25049d05

The Onshape page is not currently accessible through the connected GitHub integration, so the exact STEP export and revision still need to be supplied by a project maintainer.

## Export procedure

1. Open the upstream Onshape document using the link above.
2. Do not edit the upstream document. Record the visible document version / workspace / element identifiers and export date.
3. Select the top-level robot assembly (not an individual part).
4. Use the assembly export command and select STEP AP242 or AP214.
5. Set units to millimeters and preserve assembly structure / part names.
6. Export the complete assembly as a STEP file.
7. Also export a parts list or BOM from the same exact revision if available.
8. Save screenshots of the assembly tree and export settings.
9. Record the source revision and file checksum in the CAD manifest.
10. If the STEP file is too large for a normal GitHub upload, use Git LFS or attach it to the project issue/release. Do not compress or mesh-decimate the only editable source copy.

## Required handoff

Preferred handoff to GPT-Mecha maintainers:
- `open_duck_mini_v2_reference.step`
- `source_manifest.json` containing document ID, workspace/version ID, element ID, export date, units, export format and SHA-256
- assembly tree screenshot
- original print list and any Onshape BOM export

Place the STEP under `hardware/cad/reference/` only after confirming its upstream license and retaining all notices. Until then, keep a link and manifest template rather than copying the model.

## After import

1. Open the STEP in FreeCAD or Onshape.
2. Confirm units and overall height.
3. Identify each of the 14 actuator envelopes and joint axes.
4. Measure the actual foot support polygon and joint-to-joint link lengths.
5. Verify bearing, horn, fastener and heat-set insert interfaces.
6. Export a neutral skeleton-only assembly for the armor design workflow.
7. Record baseline mass properties where the CAD materials are reliable; compare against the simulation model.
8. Create armor as separate components and run motion-interference checks.

Do not scale the entire robot to force a 400 mm height. Servos and hardware interfaces do not scale.
