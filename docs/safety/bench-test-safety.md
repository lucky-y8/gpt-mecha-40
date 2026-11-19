# Bench and locomotion safety

This is an experimental moving robot. Small mechanisms can still pinch fingers, fall, damage property, overheat or start unexpectedly.

## Before powering

- Inspect wiring polarity and continuity.
- Verify battery voltage and regulator outputs with a multimeter.
- Confirm fuse and wire ratings.
- Secure the robot to a support gantry before actuator tests.
- Keep hands, hair, cables and loose clothing clear of joints.
- Remove armor panels during initial actuator calibration.
- Keep a physical emergency stop within reach.

## Actuator commissioning

1. Test one actuator at a time with torque disabled during wiring.
2. Verify model, voltage, bus ID and direction.
3. Set conservative current, speed and position limits.
4. Calibrate zero offsets using the upstream procedure.
5. Test small movements while supported.
6. Monitor current, temperature, communication errors and mechanical interference.
7. Do not proceed if a joint binds, oscillates, overheats or draws unexpected current.

## Standing and walking

- Use a rated support gantry and slack safety tether.
- Place a soft landing mat beneath the robot.
- Keep people and pets outside the fall envelope.
- Do not test near stairs, glass, hot surfaces or fragile objects.
- Start with static pose tests, then weight shifts, then single-step tests.
- Never run an unverified learned policy untethered.
- Revalidate after any mass, inertia, battery or armor change.

## AI and autonomy

- AI commands are high-level requests, not direct actuator authority.
- The local controller enforces joint, speed, current and workspace limits.
- Loss of network, API, perception or host process must not disable the emergency stop.
- Require explicit confirmation for potentially hazardous motions.
- Log command source, safety state and actuator faults.

## Flight

Flight is out of scope for V1. A future detachable aerial module is a separate aircraft project with its own flight controller, independent failsafes, guards, testing procedure and regulatory review. Do not use GPT as a flight stabilization controller.
