from functools import lru_cache

class Config:
    def __init__(self):
        self.replacement_char = '_'

    def set_replacement_char(self, char):
        self.replacement_char = char

config = Config()

@lru_cache(maxsize=1)
def get_replacement_char():
    return config.replacement_char
