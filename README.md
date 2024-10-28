
# Path-Friendly Filename Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![PyPI Version](https://img.shields.io/pypi/v/path-friendly-filename-generator.svg)
![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/path-friendly-filename-generator/python-package.yml?branch=main)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Making Filenames Safe](#making-filenames-safe)
  - [Validating Filenames](#validating-filenames)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

**Path-Friendly Filename Generator** is a Python package designed to ensure that filenames are safe and valid across different operating systems. It automatically removes or replaces invalid characters and trims excessively long filenames based on OS-specific file system rules. This tool is invaluable for developers, system administrators, and anyone dealing with file operations across multiple platforms.

## Features

- **Cross-Platform Compatibility:** Handles filename rules for Windows, Linux, and macOS.
- **Invalid Character Replacement:** Automatically replaces or removes characters that are invalid in filenames.
- **Reserved Name Handling:** Detects and modifies reserved filenames (e.g., `CON`, `PRN` on Windows).
- **Filename Length Trimming:** Ensures filenames do not exceed the maximum allowed length for the target OS.
- **Customizable Replacement Characters:** Allows users to specify their own replacement characters.
- **Validation Utilities:** Provides functions to validate filenames without modifying them.

## Installation

You can install the **Path-Friendly Filename Generator** package via [PyPI](https://pypi.org/):

```bash
pip install path-friendly-filename-generator
```

Alternatively, install it directly from the source repository:

```bash
git clone https://github.com/yourusername/path-friendly-filename-generator.git
cd path-friendly-filename-generator
pip install -e .
```

## Usage

### Making Filenames Safe

Use the `make_filename_safe` function to sanitize filenames by removing or replacing invalid characters and ensuring they comply with the target OS's rules.

```python
from path_friendly_filename_generator import make_filename_safe

original_filename = 'example<filename>:with*invalid|chars?.txt'
safe_filename = make_filename_safe(original_filename)

print(f"Original: {original_filename}")
print(f"Safe: {safe_filename}")
```

**Output:**

```
Original: example<filename>:with*invalid|chars?.txt
Safe: example_filename__with_invalid_chars_.txt
```

### Validating Filenames

Use the `is_valid_filename` function to check if a filename is already valid without modifying it.

```python
from path_friendly_filename_generator import is_valid_filename

filename = 'valid_filename.txt'
is_valid = is_valid_filename(filename)

print(f"Is '{filename}' a valid filename? {'Yes' if is_valid else 'No'}")
```

**Output:**

```
Is 'valid_filename.txt' a valid filename? Yes
```

## Examples

### Example 1: Basic Usage

```python
from path_friendly_filename_generator import make_filename_safe

# Original filename with invalid characters
original = 'report<>:"/\|?*.pdf'

# Generate a safe filename
safe = make_filename_safe(original)

print(safe)  # Output: report________.pdf
```

### Example 2: Custom Replacement Character

```python
from path_friendly_filename_generator import make_filename_safe

original = 'data*analysis?.csv'

# Use '-' as the replacement character instead of '_'
safe = make_filename_safe(original, replacement_char='-')

print(safe)  # Output: data-analysis-.csv
```

### Example 3: Handling Reserved Names on Windows

```python
from path_friendly_filename_generator import make_filename_safe

# Reserved name in Windows
original = 'CON.txt'

safe = make_filename_safe(original)

print(safe)  # Output: CON_reserved.txt
```

## API Reference

### `make_filename_safe(filename: str, replacement_char: str = '_') -> str`

Sanitizes the provided filename by removing or replacing invalid characters, handling reserved names, and trimming the filename length based on the operating system's rules.

- **Parameters:**
  - `filename` (`str`): The original filename to be sanitized.
  - `replacement_char` (`str`, optional): The character to replace invalid characters with. Defaults to `'_'`.

- **Returns:**
  - `str`: A path-friendly filename that is safe to use across different operating systems.

### `is_valid_filename(filename: str) -> bool`

Checks if the provided filename is valid according to the current operating system's rules without modifying it.

- **Parameters:**
  - `filename` (`str`): The filename to validate.

- **Returns:**
  - `bool`: `True` if the filename is valid, `False` otherwise.

## Testing

To ensure the package functions correctly, a comprehensive test suite is provided using Python's built-in `unittest` framework.

### Running Tests

1. **Clone the Repository (if not already done):**

   ```bash
   git clone https://github.com/yourusername/path-friendly-filename-generator.git
   cd path-friendly-filename-generator
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -e .
   ```

4. **Run the Test Suite:**

   ```bash
   python -m unittest discover -s tests
   ```

   **Expected Output:**

   ```
   ...........
   ----------------------------------------------------------------------
   Ran 11 tests in 0.123s

   OK
   ```

### Using `pytest` (Optional)

For a more feature-rich testing experience, you can use `pytest`.

1. **Install `pytest`:**

   ```bash
   pip install pytest
   ```

2. **Run Tests with `pytest`:**

   ```bash
   pytest
   ```

## Contributing

Contributions are welcome! Whether you're fixing bugs, improving documentation, or suggesting new features, your help is appreciated.

### How to Contribute

1. **Fork the Repository**

2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Your Changes**

4. **Run Tests:**

   Ensure all tests pass before submitting.

   ```bash
   python -m unittest discover -s tests
   ```

5. **Commit Your Changes:**

   ```bash
   git commit -m "Add your detailed description of the changes"
   ```

6. **Push to Your Fork:**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request:**

   Go to the original repository and submit a pull request with a detailed description of your changes.

### Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing to this project.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

**Your Name**  
Email: [your.email@example.com](mailto:your.email@example.com)  
GitHub: [yourusername](https://github.com/yourusername)
