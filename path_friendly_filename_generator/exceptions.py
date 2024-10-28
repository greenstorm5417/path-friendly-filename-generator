class PathFriendlyFilenameGeneratorError(Exception):
    """Base exception for Path-Friendly Filename Generator."""
    pass

class InvalidReplacementCharacterError(PathFriendlyFilenameGeneratorError):
    """Raised when the replacement character is invalid."""
    def __init__(self, char):
        self.char = char
        self.message = f"'{self.char}' is an invalid replacement character."
        super().__init__(self.message)
