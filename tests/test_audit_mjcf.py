import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_mjcf import audit_model


ROOT = Path(__file__).parent


class AuditMjcfTests(unittest.TestCase):
    def test_valid_fixture_passes(self):
        report, errors = audit_model(
            ROOT / "fixtures/minimal_mjcf.xml",
            ROOT / "fixtures/minimal_joint_map.json",
        )
        self.assertEqual(errors, [])
        self.assertEqual(report["runtime_actuator_count"], 1)
        self.assertEqual(report["gait_policy_action_count"], 1)
        self.assertAlmostEqual(report["mjcf_inertial_mass_sum_kg"], 1.25)
        self.assertEqual(report["joints"][0]["runtime_motor_id"], 20)

    def test_mismatch_is_reported(self):
        source = json.loads((ROOT / "fixtures/minimal_joint_map.json").read_text())
        source["runtime_motor_ids"]["right_hip_yaw"] = 10
        with tempfile.TemporaryDirectory() as tmp:
            mapping = Path(tmp) / "mapping.json"
            mapping.write_text(json.dumps(source))
            _, errors = audit_model(ROOT / "fixtures/minimal_mjcf.xml", mapping)
        self.assertTrue(any("missing from MJCF" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
