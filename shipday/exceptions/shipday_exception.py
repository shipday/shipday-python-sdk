class ShipdayException(Exception):
    def __init__(self, message: str):
        super(ShipdayException, self).__init__(message)
