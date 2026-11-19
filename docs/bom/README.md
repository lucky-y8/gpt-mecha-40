# Bill of materials

This directory distinguishes **candidate parts** from **verified parts**.

No item is approved for bulk purchase until it is matched against:
1. upstream CAD interface and dimensions
2. upstream BOM and assembly guide
3. runtime joint order and motor IDs
4. exact voltage and communication variant
5. supplier datasheet and actual quotation

## Candidate baseline

| Item | Candidate | Status | Notes |
|---|---|---|---|
| Biped skeleton | Open Duck Mini V2 | Reference only | Approx. 42 cm with legs extended; validate CAD |
| Main actuators | Feetech STS3215 7.4 V variant | Verify | Match exact upstream BOM; do not substitute 12 V variant |
| IMU | BNO055 | Reference | Confirm board and mounting orientation |
| Motion computer | Raspberry Pi Zero 2 W | Upstream runtime reference | Runtime documents this baseline |
| AI computer | Raspberry Pi 5 / RK3588 | Candidate | Select only after mass, power and thermal budget |
| Auxiliary MCU | ESP32-S3 | Candidate | Non-critical I/O first |
| Foot contact | Mechanical switches | Reference | Verify quantity and wiring |
| Audio | I2S amplifier + speaker | Candidate | Validate speaker impedance and power |
| Camera | Compact USB/CSI camera | Candidate | Check compute interface and head volume |
| Battery | Upstream-compatible pack | Verify | Never choose from capacity alone |

## Procurement gate

Before ordering the full set, complete the reference audit in docs/PROJECT_STATUS.md. Initially buy only one actuator/connector test set and print one joint or foot fit-check.
