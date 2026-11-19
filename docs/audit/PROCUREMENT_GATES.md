# Procurement gates — no bulk order yet

This document is a mandatory checklist before buying the complete robot.

## Gate A — actuator identity

- [ ] Obtain a photo of the exact STS3215 label and connector.
- [ ] Obtain the matching Feetech datasheet with full suffix/revision.
- [ ] Confirm the exact input-voltage range, stall current, rated torque and communication protocol.
- [ ] Confirm the servo is the 7.4V version used by the pinned upstream BOM.
- [ ] Confirm all 14 units are the same compatible revision.
- [ ] Confirm the 14 IDs can be configured individually before they are connected to a shared bus.
- [ ] Confirm the bus adapter pinout and 1 Mbps serial compatibility.

Do not select a servo only because a seller title says “STS3215”. Product revisions and datasheets may specify different voltage limits and performance.

## Gate B — battery and power

- [ ] Confirm the two 18650 cells are an approved matched pair.
- [ ] Confirm the 2S BMS cell chemistry, current rating, balancing and protection behavior.
- [ ] Confirm the charger is designed for the exact 2S pack and BMS.
- [ ] Confirm the maximum fully charged pack voltage.
- [ ] Confirm the servo rail is within the exact servo datasheet range at all battery states.
- [ ] Confirm the 5V regulator supports the selected compute board's peak load.
- [ ] Size wire, connectors, fuse and switch for measured load and fault conditions.
- [ ] Add a physical actuator-power emergency stop.
- [ ] Test all rails with a multimeter before connecting electronics.

The upstream wiring diagram shows a 2S 18650 pack, BMS, USB-C charging, a 7.4V motor-controller input and a 5V compute rail. The pack reaches approximately 8.4V when fully charged. Do not assume the phrase “7.4V servo” alone proves that every STS3215 revision can accept 8.4V.

## Gate C — mechanical parts

- [ ] Export the pinned Onshape CAD and record its revision.
- [ ] Match all 36 print designs and 51 piece quantities to the print guide.
- [ ] Verify bearing size, M3 insert count, screw lengths and horn hardware from CAD.
- [ ] Confirm structural print material, infill and print orientation.
- [ ] Print one joint and one foot fit-check before the full set.
- [ ] Weigh printed parts and record slicer-estimated mass.

The upstream assembly guide still marks the exact M3 screw count as TODO. Do not guess the fastener order quantity.

## Gate D — compute and AI additions

- [ ] Preserve Raspberry Pi Zero 2 W as the initial locomotion baseline unless the runtime is validated on another host.
- [ ] Add camera, microphone, speaker and display only after measuring available volume and current budget.
- [ ] Treat ESP32-S3 as an auxiliary I/O candidate, not a replacement for the upstream locomotion host.
- [ ] Do not add Raspberry Pi 5 / RK3588 until mass, heat and power impact are measured.
- [ ] Keep cloud GPT calls and high-level planning separate from real-time motor control.

## Gate E — supplier and shipping

For each China supplier, record:
- seller and product link
- exact model / suffix
- dated quotation and stock status
- datasheet link
- connector and cable details
- return policy
- package weight
- shipping to the build location
- whether the item is genuine or a compatible substitute

No bulk purchase is approved until Gates A–C are complete.
