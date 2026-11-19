#!/usr/bin/env python3
"""Audit a MuJoCo MJCF model against the GPT-Mecha reference joint map.

Uses only the Python standard library. This is a static file audit; it does not
load MuJoCo, run a policy, validate real servo limits, or prove hardware safety.
"""
from __future__ import annotations

import argparse
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def _parse_range(raw: str | None) -> list[float] | None:
    if not raw:
        return None
    values = [float(value) for value in raw.split()]
    if len(values) != 2:
        raise ValueError(f"Expected two values in joint range, got: {raw!r}")
    return values


def audit_model(model_path: Path, mapping_path: Path) -> tuple[dict[str, Any], list[str]]:
    root = ET.parse(model_path).getroot()
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))

    named_joints: dict[str, ET.Element] = {}
    for element in root.iter("joint"):
        name = element.get("name")
        if name:
            if name in named_joints:
                raise ValueError(f"Duplicate named joint in MJCF: {name}")
            named_joints[name] = element

    actuator_parent = root.find("actuator")
    actuator_joint_names: list[str] = []
    if actuator_parent is not None:
        for actuator in list(actuator_parent):
            joint_name = actuator.get("joint")
            if joint_name:
                actuator_joint_names.append(joint_name)

    if len(actuator_joint_names) != len(set(actuator_joint_names)):
        raise ValueError("Duplicate actuator joint mapping found in MJCF")

    runtime_map: dict[str, int] = {
        str(name): int(motor_id)
        for name, motor_id in mapping.get("runtime_motor_ids", {}).items()
    }
    policy_order: list[str] = list(mapping.get("gait_policy_joint_order", []))
    expected_limits: dict[str, list[float]] = mapping.get(
        "simulated_joint_limits_deg", {}
    )

    errors: list[str] = []
    runtime_names = set(runtime_map)
    actuator_names = set(actuator_joint_names)
    model_joint_names = set(named_joints)

    missing_model_joints = sorted(runtime_names - model_joint_names)
    missing_actuators = sorted(runtime_names - actuator_names)
    unexpected_actuators = sorted(actuator_names - runtime_names)
    missing_policy_joints = sorted(set(policy_order) - actuator_names)

    if missing_model_joints:
        errors.append("Runtime joints missing from MJCF: " + ", ".join(missing_model_joints))
    if missing_actuators:
        errors.append("Runtime joints missing from MJCF actuator section: " + ", ".join(missing_actuators))
    if unexpected_actuators:
        errors.append("Unexpected MJCF actuators not in runtime map: " + ", ".join(unexpected_actuators))
    if missing_policy_joints:
        errors.append("Gait-policy joints missing from actuator section: " + ", ".join(missing_policy_joints))

    motor_ids = list(runtime_map.values())
    if len(motor_ids) != len(set(motor_ids)):
        errors.append("Duplicate runtime motor IDs found")

    expected_actuator_count = mapping.get("expected_actuator_count")
    if expected_actuator_count is not None and len(actuator_joint_names) != int(expected_actuator_count):
        errors.append(
            f"Expected {expected_actuator_count} actuators, found {len(actuator_joint_names)}"
        )

    expected_policy_count = mapping.get("expected_gait_action_count")
    if expected_policy_count is not None and len(policy_order) != int(expected_policy_count):
        errors.append(
            f"Expected {expected_policy_count} gait-policy joints, found {len(policy_order)}"
        )

    joint_rows: list[dict[str, Any]] = []
    for name, motor_id in runtime_map.items():
        element = named_joints.get(name)
        raw_range = _parse_range(element.get("range") if element is not None else None)
        range_deg = [round(math.degrees(value), 3) for value in raw_range] if raw_range else None
        expected = expected_limits.get(name)
        if expected is not None and range_deg is not None:
            if any(abs(a - float(b)) > 0.15 for a, b in zip(range_deg, expected)):
                errors.append(
                    f"Joint range mismatch for {name}: MJCF {range_deg} deg, expected {expected} deg"
                )
        elif expected is not None and range_deg is None:
            errors.append(f"Expected a simulated range for {name}, but MJCF has none")
        joint_rows.append(
            {
                "joint": name,
                "runtime_motor_id": motor_id,
                "in_gait_policy": name in policy_order,
                "mjcf_range_deg": range_deg,
            }
        )

    inertial_masses = [
        float(element.get("mass"))
        for element in root.iter("inertial")
        if element.get("mass") is not None
    ]
    model_mass_sum = sum(inertial_masses)

    sensor_parent = root.find("sensor")
    sensors = []
    if sensor_parent is not None:
        for sensor in list(sensor_parent):
            sensors.append({"type": sensor.tag, "name": sensor.get("name")})

    report: dict[str, Any] = {
        "model": root.get("model"),
        "model_file": str(model_path),
        "mapping_file": str(mapping_path),
        "runtime_actuator_count": len(runtime_map),
        "mjcf_actuator_count": len(actuator_joint_names),
        "gait_policy_action_count": len(policy_order),
        "gait_policy_joint_order": policy_order,
        "joints": joint_rows,
        "sensor_count": len(sensors),
        "sensors": sensors,
        "mjcf_inertial_mass_sum_kg": round(model_mass_sum, 6),
        "mass_note": "Sum of inertial mass attributes in this MJCF file; not a measured physical robot weight.",
        "errors": errors,
    }
    return report, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mjcf", type=Path, help="Path to a MuJoCo MJCF XML file")
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path("config/reference/open_duck_mini_v2.json"),
        help="Reference runtime/policy joint mapping JSON",
    )
    parser.add_argument("--json-out", type=Path, help="Optional path to write the JSON report")
    args = parser.parse_args()

    report, errors = audit_model(args.mjcf, args.mapping)
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
