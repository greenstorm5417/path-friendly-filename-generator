import platform
from functools import lru_cache

@lru_cache(maxsize=1)
def get_os_name():
    return platform.system()

@lru_cache(maxsize=1)
def get_invalid_characters():
    os_name = get_os_name()
    if os_name == 'Windows':
        invalid_chars = set('<>:"/\\|?*')
        invalid_chars.update(chr(i) for i in range(0, 32))
        invalid_chars.add(chr(127))
    elif os_name in ('Linux', 'Darwin', 'FreeBSD', 'Solaris', 'AIX', 'HP-UX'):
        invalid_chars = {'/', '\0'}
    else:
        invalid_chars = set('<>:"/\\|?*')
        invalid_chars.update(chr(i) for i in range(0, 32))
        invalid_chars.add(chr(127))
    return invalid_chars

@lru_cache(maxsize=1)
def get_max_filename_length():
    os_name = get_os_name()
    return 255  # Most filesystems support 255 characters

@lru_cache(maxsize=1)
def get_reserved_names():
    os_name = get_os_name()
    if os_name == 'Windows':
        reserved_names = {'CON', 'PRN', 'AUX', 'NUL'}
        reserved_names.update(f'COM{i}' for i in range(1, 10))
        reserved_names.update(f'LPT{i}' for i in range(1, 10))
    else:
        reserved_names = {'CON', 'NUL'}
    return reserved_names
