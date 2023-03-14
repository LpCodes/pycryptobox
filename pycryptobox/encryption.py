#!/usr/bin/env python3


import os

import pyAesCrypt
from dotenv import load_dotenv

# Encryption parameters
bufferSize = 64 * 1024

# Load environment variables from .env file
load_dotenv()
# Access the MY_PASSWORD environment variable
password = os.getenv('MY_PASSWORD')


# # Read the password from a configuration file
# config = configparser.ConfigParser()
# config.read('myconfig.ini')
# password = config['DEFAULT']['pwd']


def encrypt_dir(dir_path):
    """
    Encrypt all files in a directory and remove the unencrypted files.

    Args:
        dir_path (str): The path to the directory to encrypt.

    Returns:
        None
    """
    print("running encryption...")
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            filename, ext = os.path.splitext(file)
            if ext == '.locked':
                continue
            file_count += 1
            file_path = os.path.join(dirpath, file)
            enctyped_output_path = file_path + ".locked"
            try:
                # Encrypt the file
                pyAesCrypt.encryptFile(file_path, enctyped_output_path, password, bufferSize)
            except Exception as e:
                print(f"Error encrypting file {file_path}: {e}")
                continue
            try:
                # Remove the unencrypted file
                os.remove(file_path)
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")
                continue
    print("Encryption Completed Total no of files encrypted : %s" % file_count)


def encrpt_file(file):
    """    Encrypts a single file.

    Args:
        file (str): The path to the file to encrypt.

    Returns:
        None
    """
    if os.path.isfile(file):
        filename, ext = os.path.splitext(file)
        if ext == ".locked":
            print(f"provided {file} is already encrypted")
            return
        file_path = os.path.abspath(file)
        encrypted_output_path = file_path + ".locked"
        try:
            # Encrypt the file
            pyAesCrypt.encryptFile(file_path, encrypted_output_path, password, bufferSize)
            print(f"{file} successfully encrypted.")
        except Exception as e:
            print(f"Error: Failed to encrypt {file}: {e}")
        os.remove(file_path)
    else:
        print(f"Error: {file} is not a valid file path.")



