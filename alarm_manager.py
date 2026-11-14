
"""
Alarm Manager Module
Educational simulation only.
This module manages simulated alarms.
It does not control real medical equipment.
"""


class AlarmManager:

    def __init__(self):
        self.active_alarms = []
        self.acknowledged_alarms = []

    def raise_alarm(self, code):
        alarm_code = str(code)

        if alarm_code not in self.active_alarms:
            self.active_alarms.append(alarm_code)

        print("ALARM RAISED:", alarm_code)
        return True

    def clear_alarm(self, code):
        alarm_code = str(code)

        if alarm_code in self.active_alarms:
            self.active_alarms.remove(alarm_code)

        if alarm_code in self.acknowledged_alarms:
            self.acknowledged_alarms.remove(alarm_code)

        print("ALARM CLEARED:", alarm_code)
        return True

    def acknowledge_alarm(self, code):
        alarm_code = str(code)

        if alarm_code in self.active_alarms:
            if alarm_code not in self.acknowledged_alarms:
                self.acknowledged_alarms.append(alarm_code)

            print("ALARM ACKNOWLEDGED:", alarm_code)
            return True

        return False

    def get_active_alarms(self):
        return self.active_alarms.copy()

    def has_active_alarms(self):
        return len(self.active_alarms) > 0

    def get_alarm_status(self):
        return {
            "active_alarms": self.active_alarms.copy(),
            "acknowledged_alarms": self.acknowledged_alarms.copy()
        }
