#!/usr/bin/env python3


import os

import pyAesCrypt
from dotenv import load_dotenv

# Encryption parameters
bufferSize = 64 * 1024

# Load environment variables from .env file
load_dotenv()
# Access the MY_PASSWORD environment variable
password = 'K1yxy7szb_'


def decrypt_dir(dir_path):
    """
    Decrypt all files in a directory that have been encrypted using AES.

    Args:
        dir_path (str): The path to the directory to decrypt.

    Returns:
        None
    """
    if not os.path.isdir(dir_path):
        print(f"Error: {dir_path} is not a directory.")
        return
    if not os.access(dir_path, os.R_OK):
        print(f"Error: {dir_path} is not readable.")
        return
    print("running decryption...")
    file_count = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Check if the file is encrypted
            filename, ext = os.path.splitext(file)
            # print(filename, ext)
            if ext == ".locked":
                file_count += 1
                # Construct the file paths
                input_path = os.path.join(root, file)
                output_path = input_path[:-7]
                try:
                    # Decrypt the file
                    pyAesCrypt.decryptFile(
                        input_path, output_path, password, bufferSize
                    )
                except Exception as e:
                    print(f"Error decrypting file {input_path}: {e}")
                    continue

                # Remove the encrypted file
                try:
                    os.remove(input_path)
                except FileNotFoundError:
                    pass
    print(f"Decryption completed. Total number of files decrypted: {file_count}")


def decrypt_file(file):
    """
    Decrypts a single file that has been encrypted using AES.

    Args:
        file (str): The path to the file to decrypt.

    Returns:
        None
    """
    if os.path.isfile(file):
        file_path = os.path.abspath(file)
        filename, ext = os.path.splitext(file)
        if ext != ".locked":
            print(f"{file} was not encrypted using this library")
            return
        # print(filename, ext)
        if ext == ".locked":
            output_path = file_path[:-7]
            try:
                # Check that the file exists
                if not os.path.exists(file_path):
                    raise Exception(f"File not found: {file_path}")
                # Decrypt the file
                pyAesCrypt.decryptFile(file_path, output_path, password, bufferSize)
            except Exception as e:
                print(f"Error decrypting file {file_path}: {e}")
                return

            # Remove the encrypted file
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")
                return

            print(f"{file} successfully decrypted.")

    else:
        print(f"Error: {file} is not a valid file path.")
