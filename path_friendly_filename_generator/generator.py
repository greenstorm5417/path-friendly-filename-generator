import re
from .validators import is_reserved_name
from .utils import get_invalid_characters, get_max_filename_length, get_reserved_names
from .config import get_replacement_char
from .exceptions import InvalidReplacementCharacterError

def make_filename_safe(filename, replacement_char=None, legacy_windows=False):
    if replacement_char is None:
        replacement_char = get_replacement_char()
    
    if replacement_char in get_invalid_characters():
        raise InvalidReplacementCharacterError(replacement_char)
    
    if filename is None:
        filename = ''
    
    invalid_chars = get_invalid_characters()
    max_length = get_max_filename_length()
    reserved_names = get_reserved_names()

    safe_filename = ''.join(c if c not in invalid_chars else replacement_char for c in filename)
    safe_filename = re.sub(r'[^\w\-.]', replacement_char, safe_filename)
    safe_filename = safe_filename.strip(' .' + replacement_char)
    safe_filename = re.sub(f'{re.escape(replacement_char)}+', replacement_char, safe_filename)
    
    if not safe_filename or all(c in (replacement_char, '.') for c in safe_filename):
        safe_filename = 'untitled'
    
    if '.' in safe_filename:
        name_part, extension = safe_filename.rsplit('.', 1)
        extension = '.' + extension
    else:
        name_part, extension = safe_filename, ''
    
    if name_part.upper() in reserved_names or name_part.strip().upper() in reserved_names:
        name_part += replacement_char + 'reserved'
    safe_filename = name_part + extension
    
    if legacy_windows:
        if '.' in safe_filename:
            name_part, extension = safe_filename.rsplit('.', 1)
            name_part = name_part[:8]
            extension = extension[:3]
            safe_filename = f"{name_part}.{extension}"
        else:
            safe_filename = safe_filename[:8]
    
    if len(safe_filename) > max_length:
        if '.' in safe_filename:
            name_part, extension = safe_filename.rsplit('.', 1)
            extension = '.' + extension
        else:
            name_part, extension = safe_filename, ''
        allowed_length = max_length - len(extension)
        safe_filename = name_part[:allowed_length] + extension
    
    return safe_filename if safe_filename else 'untitled'