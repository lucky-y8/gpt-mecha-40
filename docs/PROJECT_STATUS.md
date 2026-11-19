# Project status

Last updated: 2026-11-19

## Current state

**Phase:** M0 — upstream reference audit, partially complete.  
**Hardware built:** none.  
**Walking validated on GPT-Mecha hardware:** no.  
**Custom armor CAD:** not yet created.  
**Procurement status:** sample-first only; no bulk purchase approved.

## Decisions recorded

- Target scale: approximately 40–42 cm. The user approved reusing the Open Duck Mini V2 motion structure; this does not mean a strict 400 mm final height has been confirmed.
- Visual direction: original slim knight-style mecha; narrow shoulders/waist, long-leg visual language, white/silver + navy armor, cyan lighting.
- Locomotion reference: Open Duck Mini V2.
- Runtime reference: 14 main actuators (five per leg plus four head/neck actuators).
- Gait policy interface: ten leg joints; head/neck actuators are outside the gait action vector.
- First version: biped locomotion, head movement, voice/vision AI. No flight system and no complex hands in V1.
- Preserve upstream skeleton, joint axes and actuator interfaces until the baseline build is validated.
- China/Taobao-first procurement; prioritize sample testing and low-cost compatible components.

## Audit completed

- [x] Pin mechanical, runtime and simulation revisions.
- [x] Record motor IDs, joint names and simulated joint ranges.
- [x] Separate runtime actuator order from gait-policy action order.
- [x] Count upstream print guide: 36 STL designs / 51 pieces.
- [x] Identify upstream assembly TODOs and power-system topology.
- [x] Record known licensing gaps and attribution requirements.
- [x] Document the community body-cover mod and its policy-stability warning.
- [x] Find candidate low-cost China-side STS3215, bus adapter and BNO055 listings.
- [x] Identify 2S battery / 7.4V STS3215 maximum-voltage conflict.

See:
- [Open Duck Mini V2 audit](audit/OPEN_DUCK_MINI_V2_AUDIT.md)
- [China / Taobao sourcing plan](../bom/CHINA_TAOBAO_SOURCING.md)
- [Procurement gates](audit/PROCUREMENT_GATES.md)
- [Policy interface](simulation/policy-interface.md)
- [Armor integration](mechanical/armor-integration.md)

## M0 exit criteria still open

- [ ] Export and inspect exact Onshape CAD revision and record document/version IDs.
- [ ] Match every actuator in CAD, BOM, runtime joint order and motor ID.
- [ ] Verify exact servo model suffix, voltage range, bus interface and controller.
- [ ] Bench-test one servo with the candidate bus adapter.
- [ ] Design and verify regulated servo power rail; do not directly connect a full 2S pack to a 7.4V-max servo without manufacturer approval.
- [ ] Reconcile BOM, bearings, M3 inserts and screw lengths against CAD.
- [ ] Measure baseline physical mass, center of mass and joint loading.
- [ ] Define armor mass budget and joint keep-out volumes.
- [ ] Produce one joint and foot fit-check before full printing.
- [ ] Confirm licenses for every upstream file before copying it.

## Known uncertainties

- Upstream README describes approximately 42 cm with legs extended. This is not a guaranteed final height after armor.
- MuJoCo inertial mass entries sum to approximately 2.1071 kg, but this is simulation data, not a measured physical robot weight.
- Upstream assembly guide is incomplete; exact M3 screw count and servo-driver-board mounting instructions are unresolved.
- Upstream runtime's prebuilt image is documented primarily for Raspberry Pi Zero 2 W. A more powerful AI computer must be evaluated separately for mass, power and thermal impact.
- Historical BOM values and Taobao listing prices are references, not current supplier quotations.
- The cheapest ¥60 ST3215 listing has not yet been confirmed to be the exact STS3215-C001 7.4V variant.
- The original 2S battery topology reaches 8.4V when fully charged; the FEETECH C001 documentation lists 7.4V maximum. A regulated servo rail or written manufacturer confirmation is required before power-up.

## Change control

Any change to link lengths, joint axes, actuator model, foot geometry, battery placement or armor mass requires updating the simulation model and rechecking the locomotion policy before free-standing tests.
