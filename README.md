[![PyPI version](https://badge.fury.io/py/pycryptobox.svg)](https://badge.fury.io/py/pycryptobox) [![Downloads](https://static.pepy.tech/personalized-badge/pycryptobox?period=month&units=none&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/pycryptobox)[![Publish Package](https://github.com/LpCodes/pycryptobox/actions/workflows/python-publish.yml/badge.svg)](https://github.com/LpCodes/pycryptobox/actions/workflows/python-publish.yml)

# pyCryptobox

pyCryptobox is a package in Python that offers a straightforward approach to safeguard your confidential data by encrypting and decrypting files and directories using the AES encryption algorithm.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pycryptobox
```

## Usage

### Encryption

To encrypt a single file, use the `encrypt_file()` function:

```python
from pycryptobox import encrypt_file

file_path = r"/path/to/file.txt"
encrypt_file(file_path)

```

To encrypt all files in a directory, use the `encrypt_dir()` function

```python
from pycryptobox import encrypt_dir

dir_path = "/path/to/directory"
encrypt_dir(dir_path)


```

### Decryption

To decrypt a single file, use the decrypt_file() function:

```
from pycryptobox import decrypt_file

file_path = "/path/to/file.txt.locked"
decrypt_file(file_path)
```

To decrypt all files in a directory, use the decrypt_dir() function:

```
from pycryptobox import decrypt_dir

dir_path = "/path/to/directory"
decrypt_dir(dir_path)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
