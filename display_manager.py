
"""
Display Manager Module
Educational simulation only.
This module displays simulated status and messages.
It does not control any real medical device.
"""


class DisplayManager:

    def __init__(self):
        self.current_screen = "WELCOME"
        self.last_message = "System initialized"

    def show_status(self, status):
        self.current_screen = "STATUS"
        self.last_message = str(status)
        print("System Status:", self.last_message)
        return self.last_message

    def show_message(self, message):
        self.current_screen = "MESSAGE"
        self.last_message = str(message)
        print("Display Message:", self.last_message)
        return self.last_message

    def show_warning(self, warning):
        self.current_screen = "WARNING"
        self.last_message = str(warning)
        print("WARNING:", self.last_message)
        return self.last_message

    def clear_display(self):
        self.current_screen = "WELCOME"
        self.last_message = ""
        print("Display cleared")

    def get_current_screen(self):
        return self.current_screen

    def get_last_message(self):
        return self.last_message
