
"""
Pump Driver Module
Educational simulation only.
This module does not operate real pump hardware.
"""


class PumpDriver:

    def __init__(self):
        self.status = "STOPPED"

    def start(self):
        self.status = "SIMULATED_RUNNING"
        return "Pump simulation started"

    def stop(self):
        self.status = "STOPPED"
        return "Pump simulation stopped"

    def get_status(self):
        return self.status

    def is_running(self):
        return self.status == "SIMULATED_RUNNING"
