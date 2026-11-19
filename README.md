# GPT-Mecha 40

**An open-source, 40–42 cm class bipedal AI mecha companion.**  
**中文：** 一台约 40–42 cm、采用原创轻骑士机甲外观的双足 AI 伙伴机器人。

> Project status: **M0 reference audit in progress**. This repository contains project specifications and engineering plans; it is not yet a verified build kit. Do not bulk-purchase parts or attempt untethered walking based only on these documents.

## Vision

GPT-Mecha 40 combines a compact biped platform with an original, slim knight-style mecha shell:

- Narrow shoulders and waist, long-leg visual proportions, layered white/silver and navy armor.
- Cyan status lighting and expressive head display.
- Biped locomotion based on a separately validated open-source reference platform.
- Voice, vision and conversational AI as higher-level capabilities.
- Modular, removable armor and serviceable electronics.

The aesthetic is an original interpretation of a light-knight mecha direction. It does not reproduce an existing anime character or proprietary design.

## Engineering baseline

Current reference candidate: [Open Duck Mini V2](https://github.com/apirrone/Open_Duck_Mini/tree/v2). We are reusing its mechanical and locomotion baseline; we are **not** assuming that armor can be added without changing balance.

The upstream project describes approximately 42 cm with legs extended and provides Onshape CAD, printed parts, assembly notes, a runtime and a MuJoCo playground. Its assembly guide is incomplete, so this is a reference platform requiring validation, not a turnkey kit.

### Pinned references

| Component | Upstream | Audited revision |
|---|---|---|
| Mechanical design / print files | [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini/tree/v2) | `b23317a485b3cec7d8417f352478778b3475173c` |
| On-robot runtime | [Open Duck Mini Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime/tree/v2) | `376de65435c93486347cd601a31aa96951799896` |
| Simulation / training | [Open Duck Playground](https://github.com/apirrone/Open_Duck_Playground) | `b9be205ac64488c23504ca42e5ec790337adeec3` |

### Key audit findings

- Runtime reference: **14 main actuators** — five per leg plus four head/neck actuators.
- Gait policy action interface: **10 leg joints only**. The head/neck actuators are not part of the gait action vector.
- Runtime servo IDs and policy joint order differ in layout; use explicit joint-name mapping.
- The pinned print guide lists **36 STL designs / 51 printed pieces**, before any GPT-Mecha armor.
- The upstream assembly guide leaves the M3 fastener count and servo-driver-board mounting instructions unfinished.
- The upstream wiring diagram shows a 2S 18650 battery system, BMS, USB-C charging, a 7.4V motor-controller path and a 5V compute rail. Exact servo voltage tolerance must be verified against the matching datasheet.

Full details: [Open Duck Mini V2 audit](docs/audit/OPEN_DUCK_MINI_V2_AUDIT.md).

## Architecture principles

1. **Reuse before redesign.** Preserve reference link lengths, joint axes, actuator interfaces and locomotion assumptions initially.
2. **Armor is non-structural in V1.** The original frame and actuator mounts carry loads. Armor must be removable, light and clear of joint travel.
3. **Separate real-time control from AI.** A local controller handles actuator timing, limits, balance and emergency stop. GPT is a high-level planner/interface and never closes motor-control loops.
4. **Measure mass and inertia.** Armor, camera, battery and computer additions change center of mass and inertia. Revalidate simulation and hardware after each change.
5. **Safety before free walking.** Use a support gantry, soft landing area, current limits and a physical emergency stop during early tests.

## Planned subsystems

- **Mechanical:** reference biped skeleton + original knight-style armor panels.
- **Locomotion:** upstream runtime and policy, followed by measured sim-to-real adaptation.
- **Embedded I/O:** actuator bus, IMU, foot contact, LEDs and auxiliary sensors.
- **AI companion:** camera, microphone, speaker, speech pipeline, vision and GPT API.
- **Power:** separate regulated rails for actuators and compute, battery protection, fusing and hard stop.
- **Future expansion:** arms, hands and a detachable flight-module research interface. Flight is **not part of V1**.

## Repository map

- `docs/audit/`: upstream engineering audit and procurement gates.
- `docs/design/`: appearance and concept brief.
- `docs/mechanical/`: skeleton adaptation and armor integration.
- `docs/electronics/`: power and control architecture.
- `docs/simulation/`: policy joint mapping and simulation notes.
- `docs/bom/`: reference and verified bills of materials.
- `hardware/cad/`: original CAD and armor parts, to be added after validation.
- `hardware/electronics/`: schematics and PCB design, to be added.
- `software/`: locomotion, embedded I/O and AI modules, to be added.
- `third_party/`: upstream references and provenance notes.

## Current milestone: M0 — reference audit

Completed:
- [x] Pin upstream mechanical, runtime and simulation revisions.
- [x] Record the 14-actuator runtime map and 10-joint gait-policy interface.
- [x] Count the upstream print package.
- [x] Identify key assembly, power and documentation gaps.
- [x] Record third-party provenance and license checks.

Still open:
- [ ] Export and inspect the exact Onshape CAD revision.
- [ ] Verify exact servo SKU, voltage range, connectors and supplier datasheet.
- [ ] Reconcile every BOM item, fastener, bearing and insert against CAD.
- [ ] Measure baseline physical mass and center of mass.
- [ ] Define an armor mass budget and joint keep-out volumes.
- [ ] Print one joint/foot fit-check before a full print batch.

See [Project status](docs/PROJECT_STATUS.md), [mechanical adaptation](docs/mechanical/reference-adaptation.md), [armor integration](docs/mechanical/armor-integration.md), [policy interface](docs/simulation/policy-interface.md), [BOM](docs/bom/README.md) and [procurement gates](docs/audit/PROCUREMENT_GATES.md).

## Upstream acknowledgement

This project builds on research and design work by the authors and contributors of [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini), [Open Duck Mini Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime) and [Open Duck Playground](https://github.com/apirrone/Open_Duck_Playground). Their files and documentation remain their authors' work and retain their original licenses and notices. See [third-party provenance](third_party/UPSTREAMS.md).

## Contributing

Early contributions welcome: mechanical review, CAD fit checks, BOM verification, simulation, electronics, documentation and safety review. Read [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

This is an experimental hobby robotics project, not a certified consumer robot. A small biped can fall, pinch, overheat or damage property. Never test walking near people, pets, stairs, glass or fragile objects. Do not operate a flight module based on this repository; any future aerial module requires a separate flight controller, independent failsafes and local regulatory review.
