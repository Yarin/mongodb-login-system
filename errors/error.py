class Error(Exception):
    """Base class for custom execptions"""
    def __init__(self, message):
        super().__init__(message)
