
"""
Pump Controller Module
Educational simulation only.
"""

from input_validator import InputValidator
from safety_monitor import SafetyMonitor
from pump_driver import PumpDriver
from display_manager import DisplayManager
from alarm_manager import AlarmManager
from event_logger import EventLogger


class PumpController:

    def __init__(self):
        self.validator = InputValidator()
        self.safety = SafetyMonitor()
        self.pump = PumpDriver()
        self.display = DisplayManager()
        self.alarm = AlarmManager()
        self.logger = EventLogger()

        self.state = "SELF_TEST"

    def run_cycle(self):

        self.display.show_status(
            "Running system self-test..."
        )

        if self.safety.detect_fault():
            self.enter_safe_state(
                "System self-test failed"
            )
            return

        self.state = "READY"

        self.display.show_status(
            "System is ready."
        )

        self.logger.log(
            "System self-test successful"
        )

        self.display.show_message(
            "Educational simulation started."
        )

    def show_status(self):

        print("\n------ SYSTEM STATUS ------")
        print("Controller State:", self.state)
        print("Pump Status:", self.pump.get_status())

        self.logger.log(
            "System status checked"
        )

    def show_logs(self):

        self.logger.read_log()

    def enter_safe_state(self, reason):

        self.pump.stop()

        self.state = "SAFE_STATE"

        self.alarm.raise_alarm(reason)

        self.logger.log(
            "SAFE STATE: " + reason
        )

