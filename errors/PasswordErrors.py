from .error import Error

class WrongPasswordError(Error):
    """WrongPasswordError Exeception raised when trying to log in with wrong password

    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message = "Incorrect Password"):
        super().__init__(message)

class SamePasswordError(Error):
    """SamePasswordError Exepction raised when changing password to current password

    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message = "Can't change password to current password"):
        super().__init__(message)