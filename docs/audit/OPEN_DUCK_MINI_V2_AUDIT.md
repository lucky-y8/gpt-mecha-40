# Open Duck Mini V2 reference audit

Audit date: 2026-11-19  
Purpose: establish a reproducible baseline before any bulk purchase or custom armor CAD.

## 1. Pinned upstream sources

| Area | Repository / revision | Use in GPT-Mecha 40 |
|---|---|---|
| Mechanical design, print files, assembly | [Open_Duck_Mini v2](https://github.com/apirrone/Open_Duck_Mini/tree/v2), commit `b23317a485b3cec7d8417f352478778b3475173c` | Reference skeleton, Onshape CAD, STL list, assembly notes |
| On-robot runtime | [Open_Duck_Mini_Runtime v2](https://github.com/apirrone/Open_Duck_Mini_Runtime/tree/v2), commit `376de65435c93486347cd601a31aa96951799896` | Servo bus, joint IDs, offsets, IMU and runtime reference |
| Simulation / training | [Open_Duck_Playground main](https://github.com/apirrone/Open_Duck_Playground), commit `b9be205ac64488c23504ca42e5ec790337adeec3` | MuJoCo model, sensor names, policy joint order and training reference |

Do not use a moving branch as a reproducible engineering baseline. Re-check upstream changes and record a new commit before intentionally updating the reference.

## 2. Physical scale and model mass

- Upstream V2 README describes approximately **42 cm with its legs extended**. Treat this as the reference scale, not a guarantee of final GPT-Mecha height after new armor.
- The pinned MuJoCo XML contains inertial mass entries whose sum is approximately **2.1071 kg**. This is a simulation-model baseline, not a measured scale weight. We must weigh a real reference build and use slicer-estimated masses for printed parts before finalizing armor.
- Do not uniformly scale the complete robot STL to force a 400 mm height. Servos, bearings, horns, connectors and clearances do not scale. If a strict 400 mm limit is required, it becomes a mechanical redesign and requires renewed kinematic and policy validation.

## 3. Actuator layout and runtime motor IDs

The runtime hardware interface uses 14 main STS3215 bus servos. Its configured motor IDs are:

| Group | Joint | Runtime motor ID | MuJoCo reference range |
|---|---|---:|---:|
| Left leg | left_hip_yaw | 20 | -30° to +30° |
| Left leg | left_hip_roll | 21 | -25° to +25° |
| Left leg | left_hip_pitch | 22 | -70° to +30° |
| Left leg | left_knee | 23 | -90° to +90° |
| Left leg | left_ankle | 24 | -90° to +90° |
| Head/neck | neck_pitch | 30 | -20° to +65° |
| Head/neck | head_pitch | 31 | -45° to +45° |
| Head/neck | head_yaw | 32 | -160° to +160° |
| Head/neck | head_roll | 33 | -30° to +30° |
| Right leg | right_hip_yaw | 10 | -30° to +30° |
| Right leg | right_hip_roll | 11 | -25° to +25° |
| Right leg | right_hip_pitch | 12 | -30° to +70° |
| Right leg | right_knee | 13 | -90° to +90° |
| Right leg | right_ankle | 14 | -90° to +90° |

**Important distinctions:**

- The physical/runtime configuration contains 14 main actuators: 5 per leg and 4 for head/neck.
- The MuJoCo Playground locomotion policy's `JOINTS_ORDER_NO_HEAD` contains only the 10 leg joints. The head/neck actuators are excluded from that gait-policy action order.
- The runtime HWI dictionary order is left leg, head/neck, then right leg. The gait-policy order is left leg then right leg. Never map policy outputs to servo IDs by assuming these orders are identical.
- The joint ranges above are simulation-model limits. They are not verified safe firmware limits or guaranteed physical travel limits. Use conservative commissioning limits and verify against the exact servo, horn and mechanical stops.

## 4. Communication and sensors

The pinned runtime HWI opens the Feetech serial bus at **1,000,000 baud**, default device `/dev/ttyACM0`. The upstream runtime documentation describes:
- BNO055 IMU over I2C.
- Servo controller over USB serial.
- Foot contact switches.
- Optional eye LEDs, projector, antennas, speaker, microphone and camera.

The runtime example configuration defaults the optional expression features to false. The upstream assembly guide explicitly says instructions for the camera, antennas, eye LEDs, projector and speaker still need to be added. Therefore, do not assume camera, microphone and speaker are all included and fully documented in the base build.

The runtime configuration stores per-joint offsets and an `imu_upside_down` setting. Every physical build must calibrate its own motor offsets and verify IMU orientation; do not reuse another robot's offsets blindly.

## 5. Print package audit

The upstream print guide lists **36 STL designs / 51 printed pieces**:
- Standard PLA, 15% infill for the listed structural parts.
- TPU, 40% infill for the two foot-bottom pads.
- Exact print orientation, material and strength must be checked against each part and the chosen printer.

The printed-piece count is derived from the quantities in the pinned upstream print guide. It excludes all new GPT-Mecha armor panels.

## 6. Assembly/documentation gaps

The pinned upstream assembly guide contains explicit unfinished items:
- Exact M3 screw count is still marked TODO.
- Servo-driver-board mounting photo/instructions are marked TODO.
- Expression-feature installation instructions are marked TODO.
- IMU orientation note says the pictured installation is upside down and a natural orientation is preferable; configuration must match the actual mounting.

The runtime `checklist.md` is also marked TODO and lists joint positions/offsets, IMU orientation and foot switches as pre-policy checks. It is not a complete commissioning checklist.

The runtime setup guide says the prebuilt image is currently confirmed on Raspberry Pi Zero 2 W, and requires motor configuration, IMU calibration, Bluetooth pairing where used, and a per-build `duck_config.json` before operation.

## 7. Power-system audit — important voltage conflict

The upstream V2 wiring diagram labels:
- two 18650 cells in series,
- a 2S BMS,
- USB-C charging,
- a UBEC / 5V output for the Raspberry Pi,
- a 7.4V supply path to the motor controller.

The FEETECH manufacturer documentation for **ST-3215-C001** specifies:
- rated input range: **4.0–7.4V**;
- 7.4V stall torque: **19.5 kg·cm**;
- 7.4V rated torque: **5 kg·cm**;
- rated current: **650mA**;
- stall current: **2.5A**;
- over-voltage protection above 7.4V is described in the older product specification.

A 2S lithium-ion pack is nominally 7.2–7.4V but reaches **8.4V when fully charged**. A BMS protects cells; it does not regulate the output down to 7.4V.

**This is a real compatibility conflict to resolve before powering the servos:** do not assume that the upstream 2S wiring diagram can be copied literally with STS3215-C001. Obtain written confirmation from FEETECH for the exact servo revision, or design a properly rated regulated servo rail that stays within the selected servo's input range across the entire battery discharge cycle.

Power design must include battery protection, correctly rated wiring/connectors, fusing, separate regulated compute power, voltage/current monitoring and a physical actuator-power emergency stop. The 14-servo stall-current sum is 35A (14 × 2.5A), a fault/design bound rather than normal continuous draw. Measure real load profiles before sizing the regulator, BMS, fuse, wires and connectors. A 5V UBEC is for the compute rail, not the servo rail.

Battery assembly and charging must follow the exact cell/BMS/charger specifications; do not improvise a lithium pack.

References:
- [FEETECH 2024 brochure](https://www.feetech.cn/Data/feetechrc/upload/file/20240706/2024%E9%A3%9E%E7%89%B9%E5%AE%A3%E4%BC%A0%E5%86%8C.pdf)
- [FEETECH STS3215-C001 datasheet](https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf)

## 8. Existing armor-cover reference

The upstream V2 repository includes a community contribution at `print/mods/v2_Jaimes_Mods`, authored by **Jaime Machuca**. It includes body and leg covers, cable guides, an emergency-stop panel and STEP/3MF files.

Its README explicitly warns that the covers change mass distribution and may slightly reduce stability or cause extra recovery steps with the existing RL policy. This is useful evidence that removable covers are feasible, but it also confirms that armor mass and center of mass must be measured and the policy revalidated. The Jaime mod is not the GPT-Mecha light-knight design and must retain its author attribution if reused.

## 9. License and provenance gate

- Open_Duck_Mini v2 has an Apache-2.0 LICENSE file.
- The inspected Open_Duck_Mini_Runtime v2 repository tree has no root LICENSE/COPYING/NOTICE file. Treat its code as reference-only and do not copy it into this repository until its licensing terms are confirmed.
- The inspected Open_Duck_Playground root has no root LICENSE file, although key source files such as `base.py` and `constants.py` contain Apache-2.0 headers. Check the exact file header and included asset license before copying any file.
- The Jaime armor-cover mod has a specific attribution request in its README. Preserve it if any files are reused.

See [third-party provenance](../../third_party/UPSTREAMS.md).

## 10. M0 result

**M0 is partially complete, not passed.**

Completed:
- Pinned the three upstream revisions.
- Recorded the 14-actuator map and motor IDs.
- Identified the 10-joint gait-policy interface.
- Counted the upstream print package.
- Identified major assembly, power, documentation and license gaps.
- Found an existing community body-cover mod and its stability warning.
- Found low-cost China-side servo/adapter candidates, but exact SKU compatibility is still unverified.
- Identified the 2S battery / 7.4V servo maximum-voltage conflict.

Still required before bulk procurement:
- Export and inspect the exact Onshape CAD revision.
- Verify servo SKU, voltage range, connectors and supplier datasheet.
- Confirm a regulated servo power solution and current ratings.
- Reconcile every BOM item against the CAD and assembly steps.
- Confirm servo controller revision and bus wiring.
- Measure/estimate the baseline physical mass and center of mass.
- Establish a maximum armor mass budget.
- Print one joint/foot fit-check and verify assembly tolerances.
- Complete a supported, low-torque bench commissioning procedure.
