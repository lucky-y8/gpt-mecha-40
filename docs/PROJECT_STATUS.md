# Project status

Last updated: 2026-11-19

## Current state

**Phase:** M0 — upstream reference audit.  
**Hardware built:** none.  
**Walking validated on GPT-Mecha hardware:** no.  
**Custom armor CAD:** not yet created.  
**Procurement status:** no bulk purchase approved.

## Decisions recorded

- Project target: approximately 40–42 cm class.
- Visual direction: original slim knight-style mecha; narrow shoulders/waist, long-leg visual language, white/silver + navy armor, cyan lighting.
- Locomotion reference: Open Duck Mini V2.
- Initial reference actuator layout: 5 actuated joints per leg plus 4 head/neck actuators (14 total), subject to verification against the selected CAD/BOM/runtime revision.
- First version: biped locomotion, head movement, voice/vision AI. No flight system and no complex hands in V1.
- Keep upstream skeleton and actuator interfaces unchanged until a baseline build has been validated.

## M0 exit criteria

- [ ] Record exact upstream CAD document revision and export archive.
- [ ] Match every actuator in CAD, BOM, runtime joint order and motor ID.
- [ ] Verify voltage variant, communication bus, controller and power requirements.
- [ ] Reconcile print quantities, fasteners, bearings, inserts and assembly steps.
- [ ] Calculate baseline mass, center of mass and joint loading.
- [ ] Define armor keep-out volumes and allowable added mass.
- [ ] Produce a single-joint and foot fit-check before full printing.
- [ ] Review licenses for each upstream component before copying files.

## Known uncertainties

The upstream README describes approximately 42 cm height with legs extended. This is not a guaranteed finished height after armor. Upstream documentation says the assembly guide is incomplete and contains unresolved details. Do not treat previous conversational cost estimates as supplier quotes or validated BOM totals.

## Change control

Any change to link lengths, joint axes, actuator model, foot geometry, battery placement or armor mass requires updating the simulation model and rechecking the locomotion policy before free-standing tests.
