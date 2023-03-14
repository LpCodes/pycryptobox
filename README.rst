.. image:: https://img.shields.io/pypi/v/pycryptobox?style=flat
   :alt: PyPI
.. image:: https://static.pepy.tech/personalized-badge/pycryptobox?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads
 :target: https://pepy.tech/project/pycryptobox
pyCryptobox
===========

pyCryptobox is a Python package that provides a simple way to encrypt
and decrypt files and directories using the AES encryption algorithm..

Installation
------------

Use the package manager `pip` to install pycryptobox.

.. code:: bash

   pip install pycryptobox

Usage
-----

Encryption
~~~~~~~~~~

To encrypt a single file, use the ``encrypt_file()`` function:

.. code:: python

   from pycryptobox import encrypt_file

   file_path = r"/path/to/file.txt"
   encrypt_file(file_path)

To encrypt all files in a directory, use the ``encrypt_dir()`` function

.. code:: python

   from pycryptobox import encrypt_dir

   dir_path = "/path/to/directory"
   encrypt_dir(dir_path)

Decryption
~~~~~~~~~~

To decrypt a single file, use the decrypt_file() function:

::

   from pycryptobox import decrypt_file

   file_path = "/path/to/file.txt.locked"
   decrypt_file(file_path)

To decrypt all files in a directory, use the decrypt_dir() function:

::

   from pycryptobox import decrypt_dir

   dir_path = "/path/to/directory"
   decrypt_dir(dir_path)

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
