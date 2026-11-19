# Electronics, power and control architecture

## Architecture

### AI computer (high-level tasks)
Candidate: Raspberry Pi 5 or RK3588 Linux SBC, selected after measuring mass, power, thermal envelope and software compatibility.

Responsibilities:
- camera capture and vision
- speech pipeline and audio
- GPT API / agent orchestration
- user-facing task planning
- telemetry and logging

### Motion controller (real-time and safety)
Use the upstream-compatible controller and runtime first. An ESP32-S3 may be added for auxiliary I/O, LEDs and non-critical peripherals only after interface and timing are defined.

Responsibilities:
- actuator bus communication
- joint limits and safe startup
- IMU / foot-contact acquisition
- local stop and fault handling
- watchdog and telemetry

GPT must not issue raw high-frequency servo commands or bypass local limits. If the AI computer, Wi-Fi or cloud API fails, the motion controller must enter a defined safe state.

## Power domains

Keep actuator power and compute power as separately regulated domains. Their grounds and signal references must follow the chosen controller's electrical design.

Before selecting a battery or regulator, record:
- exact servo voltage variant and operating range
- servo peak and continuous current data
- measured current under representative loads
- regulator transient response and thermal rating
- wire gauge, connector and fuse ratings
- battery chemistry, cell arrangement, BMS and charger
- computer peak load and thermal requirements

Never connect a fully charged 2S pack directly to a servo rail unless the actuator's documented input range explicitly permits the pack's maximum voltage. Do not size the regulator from idle current. Stall-current sums are a fault/design bound, not a normal operating current.

## Required protections

- physical emergency stop that removes actuator drive power
- appropriately rated fuse close to battery
- battery protection and temperature monitoring
- undervoltage and overcurrent detection
- separate compute regulator
- strain relief and guarded connectors
- watchdog and communication-loss timeout
- current/temperature logging
- safe startup with torque disabled until calibration passes

## PCB plan

Do not design a custom servo power board until the upstream bus/controller and actual actuator variant are confirmed. First prototype with the known reference controller and documented wiring. A later custom PCB may provide protected power distribution, connectors, fusing, monitoring and auxiliary I/O; it must not silently alter servo timing or safety behavior.
