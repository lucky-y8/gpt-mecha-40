# China / Taobao sourcing plan — GPT-Mecha 40

Snapshot: 2026-11-19  
Status: **candidate sourcing guide; not an approved purchase order**.

The goal is to source in China first, avoid unnecessary premium boards, and buy only what is needed to validate the original Open Duck Mini V2 motion platform.

## Cost-control decisions

1. Keep the original Open Duck Mini V2 mechanical and locomotion baseline.
2. Keep Raspberry Pi Zero 2 W as the initial locomotion host. Do not buy Raspberry Pi 5 or RK3588 for V1.
3. Use an existing PC/phone as the early GPT voice/agent endpoint over Wi-Fi. Add a separate AI computer only after the biped works.
4. Buy one servo sample and one bus adapter first. Validate exact SKU, protocol, connector, ID programming and runtime communication before ordering the other 13 servos.
5. Ask a friend/maker space to print the 36 original STL designs (51 pieces) if possible. Outsource only if no suitable printer is available.
6. Do not buy flight hardware, complex hands, decorative servos, extra display or custom PCB for V1.

## 1. Lowest-cost candidate listings found

These are listing/search snapshots, not guaranteed checkout prices. Some are aggregator records that link to Taobao; inspect the selected SKU and seller chat before paying.

### A. Main actuators — the biggest cost item

The exact reference target is **Feetech STS3215-C001, 7.4V, 19.5 kg·cm stall torque**. The manufacturer brochure gives 55g, 45.2 × 24.7 × 35 mm, 5 kg·cm rated torque, 650mA rated current and 2.5A stall current at 7.4V.

| Candidate | Listing snapshot | Indicative price | Assessment |
|---|---|---:|---|
| Shenzhen Feetech servo factory, “S0-100,101 / OpenDuck dedicated ST3215” | [Taobao listing mirror](https://tao.k7dj.com/goods-n5xzxDNFMt3X76VYrGHkkot0tP-OpRwwaFZPQj3JpZu7.html) | **¥60** | Cheapest candidate. The title does not prove the selected SKU is STS3215-C001 7.4V. Ask for label photo, suffix, voltage and exact SKU before buying. Sample only. |
| Mixed C001 / C018 STS3215 listing | [Taobao search snapshot](https://tao.hooos.com/search?w=STS3215) | about ¥101.83–115.83 | Listing mixes variants. Must select and confirm C001 / 7.4V specifically. |
| DFRobot ST3215 7.4V 19.5kg·cm | [DFRobot product page](https://www.dfrobot.com.cn/goods-4174.html) | **¥119** | More explicit 7.4V / 19.5kg specification; use as a safer price benchmark, not proof that every listing variant is identical. |
| FEETECH manufacturer specifications | [2024 FEETECH brochure](https://www.feetech.cn/Data/feetechrc/upload/file/20240706/2024%E9%A3%9E%E7%89%B9%E5%AE%A3%E4%BC%A0%E5%86%8C.pdf) | Datasheet | Confirm exact C001 mechanical/electrical specification. |

**Potential 14-servo total:**
- If the ¥60 listing is confirmed to be the exact compatible 7.4V version: about **¥840**.
- At ¥102–119 each: about **¥1,428–1,666**.

Do not buy all 14 at ¥60 just from the listing title. Ask the seller to confirm in writing:
1. Exact model: STS3215-C001 (or the exact model specified by the upstream BOM).
2. 7.4V version, not 12V.
3. 19.5 kg·cm stall torque at 7.4V.
4. 55g / 45.2 × 24.7 × 35 mm body dimensions.
5. TTL half-duplex serial bus, supported baud rate including 1 Mbps.
6. Connector type and cable included.
7. Whether all 14 pieces can be supplied from the same revision/batch.

### B. Servo bus adapter — do not overpay before checking the simple board

| Candidate | Taobao item | Indicative price | Assessment |
|---|---|---:|---|
| ST/SC serial bus servo driver board | [Taobao item 1005305041207](https://item.taobao.com/item.htm?id=1005305041207) | about ¥22 | Low-cost candidate from a third-party OpenDuck sourcing list. Verify half-duplex TTL, 1 Mbps, direction control, connector and USB/UART interface. |
| ZLink USB/TTL debug + bus adapter | [Taobao item 570100064201](https://item.taobao.com/item.htm?id=570100064201) | about ¥22.50 | Candidate only; verify it can be used by the Open Duck runtime / rustypot serial interface. |
| Waveshare ST/SC bus servo driver board | [Taobao item 954634564409](https://item.taobao.com/item.htm?id=954634564409) | about ¥24 | Candidate listing; verify exact SKU/revision and power path. |
| TTL_Adapter_(A), ST/SC Feetech | [Taobao item 983866781632](https://item.taobao.com/item.htm?id=983866781632) | about ¥26 | Candidate listing; verify pinout and serial adapter chip. |
| Waveshare Bus Servo Adapter (A) | [Official product documentation](https://docs.waveshare.net/Bus_Servo_Adapter_A/) | about ¥78.78 on Waveshare store snapshot | Reference-compatible brand option; more expensive. |

The cheap adapters are **not yet verified drop-in replacements** for the upstream Waveshare adapter. Buy one sample and test with the exact runtime, bus and servo before ordering. A PCA9685 PWM board is not a substitute for a Feetech serial bus adapter.

### C. IMU

| Candidate | Listing / source | Indicative price | Assessment |
|---|---|---:|---|
| GY-BNO055 module | Taobao search: [BNO055](https://s.taobao.com/search?q=GY-BNO055) | about ¥38.8–55 | Cheap candidate modules; verify actual chip marking, I2C address, 3.3V logic and mounting orientation. |
| DFRobot BNO055 SEN0374 | [DFRobot product page](https://mall.dfrobot.com.cn/goods-2946.html) | ¥129 | More expensive branded module and clearer specifications. |

The upstream runtime expects BNO055. Do not substitute BNO080/BNO085 or a generic MPU6050 without changing the driver, calibration and runtime configuration.

### D. Motion computer and storage

| Item | Listing / source | Indicative price | Assessment |
|---|---|---:|---|
| Raspberry Pi Zero 2 W / WH | [Taobao listing snapshot](https://www.taouq.com/id-RZX7dw6IZtjJn2BanRFr4McMt6-JRMPPdFMj68QGJdIg/) | about ¥240–243 | Keep this as the upstream runtime baseline. Confirm genuine board and whether headers are soldered. |
| 32GB microSD A1/A2 | Search brand-name SanDisk / Samsung | Not fixed | Use a genuine card; avoid no-name cards for the OS drive. |

Do not buy a Pi 5 or RK3588 for V1. The upstream runtime is primarily documented on Pi Zero 2 W; porting to another SBC adds software work and can increase mass and power.

### E. Foot switches and print

| Item | Search phrase | Indicative price / notes |
|---|---|---|
| SS-10 foot contact switches | `SS-10 微动开关` | Low-cost switch samples; confirm dimensions and NO/NC contacts against the foot CAD. |
| Original skeleton print | [Upstream print guide](https://github.com/apirrone/Open_Duck_Mini/blob/v2/docs/print_guide.md) | 36 STL designs / 51 pieces. Original guide specifies PLA for most parts and TPU for the two foot pads. |
| Outsourced print | `Open Duck Mini V2 STL 3D打印代打` | Ask for a quote using the exact 51-piece list; do not accept a quote based only on “42cm robot”. |

## 2. Electrical issue found — resolve before battery purchase

The FEETECH STS3215-C001 datasheet lists a **rated input range of 4.0–7.4V** and describes over-voltage protection above 7.4V. A 2S lithium-ion pack reaches **8.4V when fully charged**.

The upstream wiring diagram shows two 18650 cells in series and a 7.4V servo-controller path. That creates a voltage compatibility question: nominal 7.4V is not the same as the 8.4V fully charged voltage.

Therefore:
- Do not connect a fully charged 2S pack directly to the servo bus unless FEETECH confirms the exact selected servo revision permits 8.4V.
- Obtain the exact datasheet for the exact supplied SKU.
- Design a regulated servo rail whose output remains within the servo's specified range across battery states.
- The 5V UBEC is for compute electronics; it is not the servo-bus supply.
- The 14-servo stall-current sum is 35A (14 × 2.5A). This is a fault/design bound, not expected continuous draw. Measure real current profiles and size regulators, battery, BMS, wiring, connectors and fuses accordingly.
- Keep compute power separately regulated.
- Add a physical actuator-power emergency stop.

## 3. Sample-first purchase plan

**First sample order only:**
- 1 × candidate STS3215 7.4V bus servo (prefer the ¥60 Shenzhen listing only if seller confirms exact model; otherwise use a clear ¥119 listing).
- 1 × low-cost ST/SC serial bus adapter (¥22–26 candidate) OR the official Waveshare adapter (¥78.78).
- 1 × GY-BNO055 module.
- 4 × SS-10 switches.

Do not buy the remaining 13 servos, battery cells, BMS, charger, regulator, bearings or full print batch until the sample and CAD/power checks pass.

Sample acceptance:
1. Read the servo model label and voltage.
2. Confirm communication at 1 Mbps with the intended adapter.
3. Read position, voltage, temperature and load feedback.
4. Change the ID on the sample and confirm the new ID.
5. Verify the runtime can read the servo without changing its protocol.
6. Check adapter connector polarity and power path.
7. Test BNO055 I2C detection and orientation.
8. Verify the foot switch dimensions against the CAD.

## 4. Cost envelope — honest version

Known-price subtotal only (not a complete robot):
- 14 servos: ¥840 at the unverified ¥60 listing, or ¥1,428–1,666 at ¥102–119.
- Pi Zero 2 W: about ¥240–243.
- Servo adapter: about ¥22–26 for candidate boards, or about ¥78.78 for Waveshare.
- BNO055: about ¥39–55 for low-cost modules, or ¥129 for DFRobot.
- Four switches: small cost, but exact listing not fixed.

That puts the known-price subtotal at roughly **¥1,145–2,127**, before battery, safe high-current servo power conversion, BMS/charger, wiring, fasteners, bearings, print cost, shipping and spare parts.

Planning target:
- **Self-print / low-cost verified parts:** aim for roughly ¥2,000–3,000, but only if the ¥60 servo is confirmed and power parts are sourced economically.
- **More conservative servo sourcing or outsourced printing:** roughly ¥2,700–3,800+.

These are planning targets, not supplier quotes. The servo SKU and safe power conversion are the largest unknowns. AI computer upgrades, arms, hands, custom PCB and flight hardware are excluded.

## 5. What to ask the China-side helper

For each listing, send back:
1. Taobao product URL or screenshot.
2. Exact model/suffix and selected SKU.
3. Seller name and whether manufacturer/authorized.
4. Price for 1 piece and for 14 pieces.
5. Datasheet or clear product label photo.
6. Connector/cable photo.
7. Shipping cost and delivery time inside China.

## 6. Do not buy these yet

- Raspberry Pi 5 / RK3588.
- ESP32-S3 custom PCB.
- Camera, microphone and speaker bundle.
- Flight module, motors or propellers.
- Complex hands or arm servos.
- Bearings before the Onshape CAD export confirms size.
- Bulk M3 screws before the unresolved assembly count is reconciled.
- Any 12V ST3215 / 30kg·cm version as a substitute for the 7.4V reference servo.

## References

- Open Duck Mini V2 BOM: https://docs.google.com/spreadsheets/d/1gq4iWWHEJVgAA_eemkTEsshXqrYlFxXAPwO515KpCJc/edit
- Open Duck Mini V2 print guide: https://github.com/apirrone/Open_Duck_Mini/blob/v2/docs/print_guide.md
- FEETECH 2024 brochure (C001 mechanical/electrical summary): https://www.feetech.cn/Data/feetechrc/upload/file/20240706/2024%E9%A3%9E%E7%89%B9%E5%AE%A3%E4%BC%A0%E5%86%8C.pdf
- FEETECH STS3215-C001 datasheet: https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf
- Waveshare Bus Servo Adapter (A) documentation: https://docs.waveshare.net/Bus_Servo_Adapter_A/
- DFRobot ST3215 7.4V listing: https://www.dfrobot.com.cn/goods-4174.html
- DFRobot BNO055 SEN0374 listing: https://mall.dfrobot.com.cn/goods-2946.html
- Third-party China-side adapter sourcing references: https://github.com/fanhao375/microduck-replica/blob/master/docs/%E7%94%B5%E6%8E%A7%E9%87%87%E8%B4%AD%E6%B8%85%E5%8D%95.md
