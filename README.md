# GPT-Mecha 40

**An open-source, 40–42 cm class bipedal AI mecha companion.**  
**中文：** 一台约 40–42 cm、采用原创轻骑士机甲外观的双足 AI 伙伴机器人。

> Project status: **Planning / reference validation**. This repository currently contains project specifications and engineering plans. It is **not a verified build kit**. Do not purchase a complete parts set or attempt untethered walking based only on these documents.

## Vision

GPT-Mecha 40 combines a compact biped platform with an original, slim knight-style mecha shell:

- Narrow shoulders and waist, long-leg visual proportions, layered white/silver and navy armor.
- Cyan status lighting and expressive head display.
- Biped locomotion based on a separately validated open-source reference platform.
- Voice, vision and conversational AI as higher-level capabilities.
- Modular armor and serviceable electronics.

The aesthetic is inspired by the light-knight mecha direction discussed by the project owner. The design is intended to be original; it does not reproduce any existing anime character or proprietary design.

## Current engineering baseline

The current reference candidate is [Open Duck Mini V2](https://github.com/apirrone/Open_Duck_Mini/tree/v2), not a claim that its parts can be directly covered with armor and still walk.

Why it is a useful starting point:

- The upstream project describes a robot approximately 42 cm tall with its legs extended.
- It provides an Onshape CAD document, printed-part files, a print guide, an assembly guide, a runtime repository and a MuJoCo-based training/playground repository.
- Its published assembly documentation describes five actuated joints per leg and a four-actuator head/neck assembly. This gives a **14-actuator reference configuration**; verify the exact BOM, motor IDs, CAD revision and runtime mapping before ordering parts.
- The upstream README says its assembly guide is incomplete. Its assembly guide still has an unresolved M3 screw count and a TODO around the servo-driver-board mounting. Treat the upstream build as a reference that requires validation, not a turnkey kit.

Pinned reference revisions (review before updating):

| Component | Upstream | Reference revision |
|---|---|---|
| Mechanical design / print files | [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini/tree/v2) | b23317a485b3cec7d8417f352478778b3475173c |
| Runtime | [Open Duck Mini Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime/tree/v2) | 376de65435c93486347cd601a31aa96951799896 |
| Simulation / training | [Open Duck Playground](https://github.com/apirrone/Open_Duck_Playground) | b9be205ac64488c23504ca42e5ec790337adeec3 |

The upstream runtime documentation primarily describes Raspberry Pi Zero 2 W. It also contains Raspberry Pi 5 notes, but this project will preserve the known upstream locomotion stack first and evaluate a separate AI computer only after mass, power and thermal budgets are measured.

## Architecture principles

1. **Reuse before redesign.** Keep the reference leg linkage, joint axes, actuator interfaces and locomotion assumptions initially. Do not change leg geometry and expect the reference policy to remain valid.
2. **Armor is non-structural at first.** The original load-bearing frame and actuator mounts carry the loads. Armor panels must be removable, light and clear of joint travel.
3. **Separate real-time control from AI.** A local controller handles actuator timing, limits, balance and emergency stop. GPT is a high-level planner/interface; it never directly closes motor-control loops.
4. **Measure mass and inertia.** Every armor, camera, battery and computer addition changes center of mass and inertia. Revalidate simulation and real hardware after each change.
5. **Safety before free walking.** Use a support gantry, soft landing area, current limits and a physical emergency stop during early tests.

## Planned subsystems

- **Mechanical:** reference biped skeleton + original knight-style armor panels.
- **Locomotion:** upstream runtime and policy, then measured sim-to-real adaptation.
- **Embedded I/O:** actuator bus, IMU, foot contact, LEDs and auxiliary sensors.
- **AI companion:** camera, microphone, speaker, speech pipeline, vision and GPT API.
- **Power:** separate regulated rails for actuators and compute, battery protection, fusing and hard stop.
- **Future expansion:** arms, hands and a detachable flight-module research interface. Flight is **not part of V1**.

## Repository map

- docs/: design notes, architecture, safety and build procedures.
- hardware/bom/: verified and candidate bills of materials.
- hardware/cad/: original CAD and armor parts, to be added after validation.
- hardware/electronics/: schematics and PCB design, to be added.
- simulation/: URDF/MJCF/MuJoCo adaptation, to be added.
- software/locomotion/: upstream runtime integration, to be added.
- software/embedded/: ESP32 and auxiliary I/O, to be added.
- software/ai/: voice, vision and GPT agent, to be added.
- third_party/: upstream references and license/provenance notes.

## First milestone

**M0 — Reference audit, no bulk purchasing**

- [ ] Review the upstream V2 CAD and print list.
- [ ] Confirm the exact actuator model, voltage variant, quantity, bus interface and controller.
- [ ] Reconcile the assembly guide, BOM and runtime joint order/offsets.
- [ ] Obtain the original CAD and calculate the true skeleton envelope.
- [ ] Define a mass budget for armor, compute, battery and sensors.
- [ ] Build one joint/foot fit-check before ordering a full print batch.

See [Project status](docs/PROJECT_STATUS.md), [mechanical adaptation plan](docs/mechanical/reference-adaptation.md), [electronics and power plan](docs/electronics/power-and-control.md), and [safety notes](docs/safety/bench-test-safety.md).

## Upstream acknowledgement

This project builds on research and design work by the authors and contributors of:

- [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini)
- [Open Duck Mini Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime)
- [Open Duck Playground](https://github.com/apirrone/Open_Duck_Playground)

Their source files, CAD, models and documentation remain their authors' work and retain their original licenses and notices. This repository will not copy or relicense upstream files without preserving the applicable terms. See [third-party provenance](third_party/UPSTREAMS.md).

## Contributing

Early contributions welcome: mechanical review, CAD fit checks, BOM verification, simulation, electronics, documentation and safety review. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Disclaimer

This is an experimental hobby robotics project, not a certified consumer robot. A small biped can fall, pinch, overheat or damage its actuators. Never test walking near people, pets, stairs, glass or fragile objects. Do not operate a flight module based on this repository; any future aerial module requires a separate flight controller, independent failsafes and local regulatory review.
