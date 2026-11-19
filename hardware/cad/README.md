# CAD workspace

This directory is reserved for original GPT-Mecha CAD and the read-only reference assembly.

## Layout

- `reference/`: upstream STEP export and source manifest. Do not alter the original export.
- `skeleton/`: any GPT-Mecha-owned adapters or skeleton modifications, only after the reference is validated.
- `armor/`: original helmet, chest, shoulder, waist, leg and backpack panels.
- `fit_checks/`: single-joint, knee-cover, ankle-cover and foot fit-check parts.

## File policy

- Keep native editable CAD sources whenever possible.
- Export STEP for neutral assembly exchange.
- Export STL/3MF only for printing.
- Use millimeters and record units in every drawing.
- Keep upstream files separate and preserve their original licenses.
- Do not commit a binary CAD file until its source, revision, license and checksum are recorded.

No manufacturing-ready CAD is present yet. See [Onshape export procedure](../../docs/cad/ONSHAPE_EXPORT_AND_REFERENCE_BASELINE.md).
