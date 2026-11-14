
"""
Event Logger Module
Insulin Pump Control System
Educational simulation only.
"""

from datetime import datetime


class EventLogger:

    def __init__(self):
        self.log_file = "event_log.txt"

    def log(self, event):
        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(self.log_file, "a") as file:
            file.write(
                f"{current_time} - {event}\n"
            )

        print("[LOG]", event)

    def read_log(self):
        try:
            with open(self.log_file, "r") as file:
                print("\n===== EVENT HISTORY =====")
                print(file.read())

        except FileNotFoundError:
            print("No event history available.")

    def clear_log(self):
        with open(self.log_file, "w") as file:
            file.write("")

        print("Event log cleared successfully.")


