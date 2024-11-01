
# Path-Friendly Filename Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![PyPI Version](https://img.shields.io/pypi/v/path-friendly-filename-generator.svg)
![Issues](https://img.shields.io/github/issues/greenstorm5417/path-friendly-filename-generator.svg)
![Forks](https://img.shields.io/github/forks/greenstorm5417/path-friendly-filename-generator.svg)
![Stars](https://img.shields.io/github/stars/greenstorm5417/path-friendly-filename-generator.svg)
[![Downloads](https://img.shields.io/pypi/dd/path-friendly-filename-generator)](https://pypi.org/project/path-friendly-filename-generator/)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
  - [Making Filenames Safe](#making-filenames-safe)
  - [Validating Filenames](#validating-filenames)
  - [Handling Reserved Names](#handling-reserved-names)
  - [Customizing Replacement Characters](#customizing-replacement-characters)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Advanced Configuration](#advanced-configuration)
- [Testing](#testing)
  - [Running Unit Tests](#running-unit-tests)
  - [Using pytest](#using-pytest)
- [Continuous Integration](#continuous-integration)
- [Contributing](#contributing)
  - [Guidelines](#guidelines)
  - [Code of Conduct](#code-of-conduct)
- [Changelog](#changelog)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Overview

**Path-Friendly Filename Generator** is a robust Python package crafted to ensure that filenames are safe, valid, and compliant across various operating systems. Whether you're developing cross-platform applications, managing file systems, or automating file operations, this tool streamlines the process by automatically sanitizing filenames, removing or replacing invalid characters, and adhering to OS-specific file system rules. It is an indispensable utility for developers, system administrators, and anyone engaged in file management tasks across multiple platforms.


## Features

- **Cross-Platform Compatibility:** Seamlessly handles filename rules for Windows, Linux, macOS, and other Unix-like systems.
- **Invalid Character Replacement:** Automatically detects and replaces or removes characters that are invalid in filenames.
- **Reserved Name Handling:** Identifies and modifies reserved filenames (e.g., `CON`, `PRN` on Windows) to prevent conflicts.
- **Filename Length Trimming:** Ensures filenames do not exceed the maximum allowed length for the target operating system.
- **Customizable Replacement Characters:** Offers flexibility to specify custom characters for replacing invalid characters.
- **Validation Utilities:** Provides comprehensive functions to validate filenames without altering them.
- **Legacy Windows Support:** Optionally trims filenames to comply with legacy Windows 8.3 filename conventions.
- **Unicode Support:** Effectively handles filenames with Unicode characters, ensuring broad compatibility.
- **Extensible Configuration:** Allows advanced users to modify default settings through configuration classes.

## Installation

Installing the **Path-Friendly Filename Generator** is straightforward. You can choose between installing via [PyPI](https://pypi.org/) or directly from the source repository on GitHub.

### Using pip (Recommended)

Install the package using `pip`:

```bash
pip install path-friendly-filename-generator
```

### From Source

Alternatively, install the package directly from the GitHub repository:

```bash
git clone https://github.com/greenstorm5417/path-friendly-filename-generator.git
cd path-friendly-filename-generator
pip install -e .
```

## Quick Start

After installation, you can quickly start using the package to sanitize filenames.

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

## Detailed Usage

### Making Filenames Safe

The primary function, `make_filename_safe`, sanitizes filenames by removing or replacing invalid characters and ensuring compliance with the target OS's rules.

```python
from path_friendly_filename_generator import make_filename_safe

original = 'report<>:"/\|?*.pdf'
safe = make_filename_safe(original)

print(safe)  # Output: report________.pdf
```

### Validating Filenames

Before sanitizing, you might want to check if a filename is already valid using the `is_valid_filename` function.

```python
from path_friendly_filename_generator import is_valid_filename

filename = 'valid_filename.txt'
is_valid = is_valid_filename(filename)

print(f"Is '{filename}' a valid filename? {'Yes' if is_valid else 'No'}")
```


### Handling Reserved Names

Certain filenames are reserved by operating systems (e.g., `CON`, `PRN` on Windows). The generator detects these and modifies them to prevent conflicts.

```python
from path_friendly_filename_generator import make_filename_safe

original = 'CON.txt'
safe = make_filename_safe(original)

print(safe)  # Output: CON_reserved.txt
```

### Customizing Replacement Characters

You can specify your own replacement character instead of the default underscore (`_`).

```python
from path_friendly_filename_generator import make_filename_safe

original = 'data*analysis?.csv'
safe = make_filename_safe(original, replacement_char='-')

print(safe)  # Output: data-analysis-.csv
```

## Testing

Ensuring the reliability and stability of the **Path-Friendly Filename Generator** is paramount. A comprehensive test suite has been developed using Python's built-in `unittest` framework and `pytest` for enhanced testing capabilities.

### Running Unit Tests

To run the unit tests:

1. **Clone the Repository (if not already done):**

   ```bash
   git clone https://github.com/greenstorm5417/path-friendly-filename-generator.git
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
   ......................
   ----------------------------------------------------------------------
   Ran 22 tests in 0.456s

   OK
   ```

### License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as per the license terms.

## Contact

**Sammy**  
Email: [dussinsa01@esj.org](mailto:dussinsa01@esj.org)  
GitHub: [greenstorm5417](https://github.com/greenstorm5417)

For any inquiries, feature requests, or support, feel free to reach out via email or open an issue on the [GitHub repository](https://github.com/greenstorm5417/path-friendly-filename-generator).
