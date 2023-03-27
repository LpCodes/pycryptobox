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


def encrypt_files_in_directory(dir_path):
    # Get the encryption key from keyring
    key = keyring.get_password(service_name, username)

    # If the key doesn't exist, create a new one and save it to keyring
    if not key:
        key = Fernet.generate_key()
        keyring.set_password(service_name, username, key.decode())

    # Create a Fernet object with the encryption key
    fernet = Fernet(key)

    # Initialize a counter for the number of files encrypted
    num_encrypted_files = 0

    # Loop through all files in the directory
    for filename in os.listdir(dir_path):

        # Skip subdirectories
        if os.path.isdir(os.path.join(dir_path, filename)):
            continue

        # Check if the file is already encrypted
        if filename.endswith('.enc'):
            print(f'{filename} is already encrypted and will not be encrypted again')
            continue

        # Open the file and read its contents
        with open(os.path.join(dir_path, filename), 'rb') as f:
            contents = f.read()

        # Encrypt the contents using Fernet
        encrypted_contents = fernet.encrypt(contents)

        # Write the encrypted contents to a new file with the .enc extension
        with open(os.path.join(dir_path, filename + '.enc'), 'wb') as f:
            f.write(encrypted_contents)

        # Remove the original file
        os.remove(os.path.join(dir_path, filename))

        num_encrypted_files += 1

    print(f'{num_encrypted_files} files encrypted')


def encrypt_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    if file_path.endswith('.enc'):
        print(f'{file_path} is already encrypted and will not be encrypted again')
        return f'{file_path} is already encrypted and will not be encrypted again'
    # Get the encryption key from keyring
    key = keyring.get_password(service_name, username)

    # If the key doesn't exist, create a new one and save it to keyring
    if not key:
        key = Fernet.generate_key()
        keyring.set_password(service_name, username, key.decode())

    # Create a Fernet object with the encryption key
    fernet = Fernet(key)

    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        contents = f.read()

    # Encrypt the contents using Fernet
    encrypted_contents = fernet.encrypt(contents)

    # Overwrite the file with the encrypted contents
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_contents)

    # Remove the original unencrypted file
    os.remove(file_path)

    print(f"{file_path} ssuccessfully encrypted")




# encrypt_files_in_directory(r"C:\Users\lovel\Downloads\New folder")
# decrypt_files_in_directory(r"C:\Users\lovel\Downloads\New folder")

# decrypt_file(r"C:\Users\lovel\Downloads\New folder\90-907986_hd-nature-images-wallpaper-of-natures-organic-plants. - Copy.jpg.enc")
