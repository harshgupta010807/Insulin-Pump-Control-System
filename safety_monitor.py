
"""
Safety Monitor Module
Educational simulation only.
This module does not control any real insulin pump.
"""


class SafetyMonitor:

    def __init__(self):
        self.battery_ok = True
        self.motor_ok = True
        self.reservoir_ok = True
        self.fault_detected = False

    def check_battery(self):
        return self.battery_ok

    def check_motor(self):
        return self.motor_ok

    def check_reservoir(self):
        return self.reservoir_ok

    def detect_fault(self):
        if not self.battery_ok:
            self.fault_detected = True
            return "Battery fault detected"

        if not self.motor_ok:
            self.fault_detected = True
            return "Motor fault detected"

        if not self.reservoir_ok:
            self.fault_detected = True
            return "Reservoir fault detected"

        self.fault_detected = False
        return None

    def check_limits(self, request):
        if self.detect_fault():
            return False

        return True

    def enter_safe_state(self):
        self.fault_detected = True
        return "System entered safe state"

    def get_status(self):
        return {
            "battery": self.battery_ok,
            "motor": self.motor_ok,
            "reservoir": self.reservoir_ok,
            "fault": self.fault_detected
        }
