from shipday.exceptions.shipday_exception import ShipdayException

class ShipdayRateLimitException(ShipdayException):
    def __init__(self, message):
        super().__init__(message)
