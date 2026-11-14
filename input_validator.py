
"""
Input Validator Module
Educational simulation only.
"""

class InputValidator:

    def validate(self, request):

        allowed_requests = [
            "status",
            "simulate",
            "exit"
        ]

        if not isinstance(request, str):
            return False

        if request.strip().lower() in allowed_requests:
            return True

        return False

