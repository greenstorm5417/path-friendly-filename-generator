from .utils import get_invalid_characters, get_max_filename_length, get_reserved_names

def contains_invalid_characters(filename):
    invalid_chars = get_invalid_characters()
    return any(char in invalid_chars for char in filename)

def is_too_long(filename):
    max_length = get_max_filename_length()
    return len(filename) > max_length

def is_reserved_name(filename):
    name_part = filename.split('.')[0].upper()
    reserved_names = get_reserved_names()
    return name_part in reserved_names

def is_valid_filename(filename):
    if not filename or filename.strip(' .') == '':
        return False
    if contains_invalid_characters(filename):
        return False
    if is_too_long(filename):
        return False
    if is_reserved_name(filename):
        return False
    return True