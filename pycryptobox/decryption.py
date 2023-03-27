import os
import keyring
import configparser
from cryptography.fernet import Fernet

# Load the configuration file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Get the keyring service name and username from the configuration file
service_name = config.get('KEYRING', 'service_name')
username = config.get('KEYRING', 'username')


def decrypt_files_in_directory(dir_path):
    # Get the encryption key from keyring
    key = keyring.get_password(service_name, username)

    # If the key doesn't exist, raise an error
    if not key:
        raise ValueError('Encryption key not found in keyring')

    # Create a Fernet object with the encryption key
    fernet = Fernet(key)

    # Initialize a counter for the number of files decrypted
    num_decrypted_files = 0

    # Loop through all files in the directory
    for filename in os.listdir(dir_path):
        # Skip subdirectories
        if os.path.isdir(os.path.join(dir_path, filename)):
            continue

        # Check if the file is already decrypted
        if not filename.endswith('.enc'):
            print(f'{filename} is not encrypted and will not be decrypted')
            continue

        # Open the file and read its contents
        with open(os.path.join(dir_path, filename), 'rb') as f:
            contents = f.read()

        # Decrypt the contents using Fernet
        decrypted_contents = fernet.decrypt(contents)

        # Write the decrypted contents to a new file without the .enc extension
        with open(os.path.join(dir_path, filename[:-4]), 'wb') as f:
            f.write(decrypted_contents)

        # Remove the original encrypted file
        os.remove(os.path.join(dir_path, filename))

        num_decrypted_files += 1

    print(f'{num_decrypted_files} files decrypted')


def decrypt_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    if not file_path.endswith('.enc'):
        print(f'{file_path} is not encrypted and will not be decrypted')
        return f'{file_path} is not encrypted and will not be decrypted'
    # Get the encryption key from keyring
    key = keyring.get_password(service_name, username)

    # If the key doesn't exist, raise an error
    if not key:
        raise ValueError('Encryption key not found in keyring')

    # Create a Fernet object with the encryption key
    fernet = Fernet(key)

    # Check if the file is already decrypted
    if not file_path.endswith('.enc'):
        raise ValueError('File is not encrypted')

    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        contents = f.read()

    # Decrypt the contents using Fernet
    decrypted_contents = fernet.decrypt(contents)

    # Overwrite the file with the decrypted contents
    with open(file_path[:-4], 'wb') as f:
        f.write(decrypted_contents)

    # Remove the encrypted file
    os.remove(file_path)

    print(f"{file_path} ssuccessfully decrypted")
