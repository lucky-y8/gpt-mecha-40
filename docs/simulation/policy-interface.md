# Locomotion policy interface

## Reference source

Pinned simulation source: [Open_Duck_Playground](https://github.com/apirrone/Open_Duck_Playground), commit `b9be205ac64488c23504ca42e5ec790337adeec3`.

The MuJoCo model includes 14 actuated joints (10 leg joints + 4 head/neck joints). However, the locomotion constants define `JOINTS_ORDER_NO_HEAD` as a 10-joint list.

## Policy action order

Do not reorder this list without adapting the policy and validating the model:

1. left_hip_yaw
2. left_hip_roll
3. left_hip_pitch
4. left_knee
5. left_ankle
6. right_hip_yaw
7. right_hip_roll
8. right_hip_pitch
9. right_knee
10. right_ankle

The head/neck joints are not part of this gait action vector.

## Runtime motor mapping

The hardware runtime maps the above gait joints to IDs:

| Policy index (0-based) | Joint | Servo ID |
|---:|---|---:|
| 0 | left_hip_yaw | 20 |
| 1 | left_hip_roll | 21 |
| 2 | left_hip_pitch | 22 |
| 3 | left_knee | 23 |
| 4 | left_ankle | 24 |
| 5 | right_hip_yaw | 10 |
| 6 | right_hip_roll | 11 |
| 7 | right_hip_pitch | 12 |
| 8 | right_knee | 13 |
| 9 | right_ankle | 14 |

The runtime HWI dictionary has a different full-device ordering because the four head/neck joints appear between the left and right leg groups. Use explicit joint-name mapping; do not rely on array position across modules.

## Model and policy compatibility

The current policy assumes a particular:
- joint naming and ordering
- joint axis and direction
- joint range
- actuator response and backlash model
- body mass and inertia
- foot geometry and contact model
- IMU and foot sensor frame

Any armor, battery, computer, camera or backpack changes the mass and inertia. The new robot MJCF must use measured or slicer-estimated component masses and must be evaluated in simulation before real walking tests.

Do not assume that the original ONNX policy remains safe or stable after adding armor. Initially preserve the reference geometry and test the unarmored baseline. Add armor incrementally, remeasure mass properties and compare simulation behavior. Retrain or fine-tune only after the model and hardware are accurately identified.

## Safe test stages

1. Parse and load the untouched reference MJCF.
2. Verify joint names, axes, limits, sensors and action order.
3. Run policy inference in simulation only.
4. Add one armor component to the simulation and update its mass/inertia.
5. Repeat simulation checks.
6. On hardware, use a support gantry, soft landing area, low torque and physical emergency stop.
7. Only consider untethered walking after documented, supervised stability tests.
