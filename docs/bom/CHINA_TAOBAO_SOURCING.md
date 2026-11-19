# China / Taobao sourcing plan — GPT-Mecha 40

Snapshot: 2026-11-19  
Status: **candidate sourcing guide; not an approved purchase order**.

The goal is to source in China first, avoid unnecessary premium boards, and buy only what is needed to validate the original Open Duck Mini V2 motion platform.

## Cost-control strategy

1. Keep the original Open Duck Mini V2 mechanical and locomotion baseline.
2. Keep Raspberry Pi Zero 2 W as the initial locomotion host; do not buy Raspberry Pi 5 or RK3588 for V1.
3. Use the existing development PC/phone as the early GPT voice/agent endpoint over Wi-Fi. Add a separate AI computer only after the biped works.
4. Buy one servo sample and one driver first. Validate the SKU, bus protocol, connector and firmware before ordering the other 13.
5. Ask a friend/maker space to print the 36 original STL designs (51 pieces) if possible. Outsource only if no suitable printer is available.
6. Do not buy the flight module, arms, hands, decorative servos, extra display or custom PCB for V1.

## Taobao search shortlist

Prices below are indicative listing/search references observed on 2026-11-19. They are not guaranteed checkout prices, and listing variants can be mixed.

| Priority | Item | Qty | Taobao search keywords | Indicative price / notes | Buy gate |
|---|---|---:|---|---|---|
| P0 | Feetech STS3215-C001 7.4V 19.5 kg·cm | 14 total | `飞特 STS3215-C001 7.4V 19.5KG 双轴 总线舵机` | Search listings roughly ¥99–130 each; a DFRobot-branded listing was seen around ¥119. | Buy 1 sample first. Require photo of label/model suffix, datasheet, 3-pin cable/connector, TTL half-duplex bus support and 1 Mbps operation. All 14 must be same version. |
| P0 | Bus servo adapter | 1 | `微雪 Bus Servo Adapter A 总线舵机驱动板` | Reference listing around ¥95. | Must explicitly support Feetech STS3215 / ST-series half-duplex TTL bus, correct connector and 1 Mbps. Do not substitute PCA9685 PWM board. |
| P0 | IMU | 1 | `BNO055 九轴姿态传感器 I2C 3.3V 模块` | Search references around ¥35–140. | Ask for chip marking, pinout, 3.3V logic and board dimensions. Low-cost clones require bench validation. |
| P0 | Motion computer | 1 | `树莓派 Zero 2 W 原装` | Search references around ¥228–243. | Keep this as the known upstream locomotion baseline. Avoid buying a Pi 5 / RK3588 for V1. |
| P0 | Foot contact switch | 4 | `SS-10 微动开关` | Roughly ¥0.5–1 each in low-cost listings. | Match size and mounting to the foot; verify normally-open/normally-closed wiring. |
| P0 | Battery cells | 2 | `Molicel INR18650-P30B 3000mAh 30A` | Price not reliably confirmed in this search. | Buy only genuine matched high-discharge cells from a traceable seller; avoid used/re-wrapped cells. |
| P0 | Battery holder / BMS / charger | 1 set | `18650 2串电池盒`, `2S 锂电池 BMS 均衡保护板`, `8.4V 2S 锂电池充电器` | Price not confirmed. | Match cell chemistry, current rating, balance/protection and charging topology. Do not buy a low-current generic BMS. |
| P0 | Regulated power | 1 set | `大电流 DC-DC 降压 7.4V`, `5V 5A UBEC` | Price depends heavily on current rating. | Exact servo input limit must be confirmed first. Size servo rail for measured transient current; compute rail is separate. |
| P1 | Bearings | 3 candidate | `6804ZZ 轴承 20x32x7` | Candidate only; not yet confirmed from the exact CAD export. | Do not buy until exact Onshape CAD confirms bearing designation and fit. |
| P1 | Fasteners / inserts | 1 kit | `M3 热熔铜螺母 M3螺丝套装` | Buy small mixed kit only. | Upstream assembly guide still has an unresolved exact M3 screw count. Confirm lengths and insert count from CAD first. |
| P1 | 3D printing | 1 batch | `3D打印代打 PETG PLA TPU` | A China-side estimate found about ¥500–800 outsourced; self-print estimate around ¥150. | Original print guide: PLA for most parts and TPU for foot pads. Confirm printer volume, material and orientation. |
| P2 | Camera / mic / speaker / LEDs | 1 set | `树莓派 Zero 摄像头`, `I2S 数字麦克风`, `MAX98357 I2S 功放`, `小尺寸喇叭` | Defer. | Add after motion platform works and internal volume/power are measured. |
| P2 | ESP32-S3 auxiliary board | 1 | `ESP32-S3 开发板` | Defer. | Not needed for the first locomotion baseline; add later for LEDs and auxiliary I/O if useful. |

## Critical electrical warning — servo voltage

The Feetech STS3215-C001 specification found for the 7.4V version lists a rated input range up to 7.4V. A 2S lithium-ion pack is nominally 7.2–7.4V but reaches 8.4V when fully charged.

Therefore:
- Do not assume a 2S pack can be connected directly to the servo bus.
- Obtain the exact datasheet for the exact SKU supplied.
- If its maximum is 7.4V, design a suitably rated regulated servo rail; a small 5A UBEC is not a servo-bus regulator.
- The 14-servo stall-current sum is a fault/design bound, not a normal operating current. Measure the real current profile and size the regulator, BMS, fuse, wires and connectors accordingly.
- Keep the compute rail separately regulated.
- Add a physical actuator-power emergency stop.

The upstream wiring diagram shows a 2S battery arrangement, but this project must verify the exact servo revision and rail voltage rather than blindly copy a diagram.

## Important substitution warnings

- Do not buy a listing titled merely “STS3215” without confirming the suffix. Search results mix 7.4V 19kg·cm and 12V 30kg·cm versions.
- Do not replace the serial bus servos with ordinary PWM servos.
- Do not replace the bus adapter with a PCA9685 board; it is a different interface.
- Do not replace BNO055 with an arbitrary IMU unless the runtime driver and calibration are adapted.
- Do not buy 608ZZ / 6804ZZ bearings until the exact CAD is inspected. Search results for other OpenDuck replicas can refer to different mechanical designs.
- Do not bulk-buy M3 fasteners before reconciling the upstream assembly guide and CAD.

## What to ask a China-side helper to do

For each candidate listing, send back:
1. Taobao product URL or screenshot.
2. Exact model/suffix and package contents.
3. Seller name and whether it is the manufacturer/authorized store.
4. Price for 1 pc and for the full quantity.
5. Datasheet or clear label photo.
6. Connector/cable photo.
7. Shipping cost and delivery time inside China.

Start by sourcing only:
- 1 × STS3215-C001 sample
- 1 × compatible Bus Servo Adapter
- 1 × BNO055 module
- 1 × SS-10 switch sample pack

After the sample test passes, buy the remaining servos and the rest of the mechanical/electrical kit.

## Budget planning

A practical target is:
- **Self-print / low-price sourcing:** roughly ¥2,500–3,500 for the initial biped baseline.
- **Outsourced printing / higher servo quote / power redesign:** roughly ¥3,000–4,300 or more.

These are planning ranges, not supplier quotes. The servo SKU and safe high-current power design are the largest cost and compatibility risks. AI compute upgrades, arms, hands, custom PCB and flight hardware are excluded.

## References

- Open Duck Mini V2 BOM: https://docs.google.com/spreadsheets/d/1gq4iWWHEJVgAA_eemkTEsshXqrYlFxXAPwO515KpCJc/edit
- Open Duck Mini V2 print guide: https://github.com/apirrone/Open_Duck_Mini/blob/v2/docs/print_guide.md
- Feetech STS3215-C001 datasheet: https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf
- Feetech official product information: https://www.feetech.cn/
