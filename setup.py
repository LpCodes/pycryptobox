from setuptools import setup, find_packages,Extension

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pycryptobox",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "encode-encrypt-dir = pycryptobox.encryption:encrypt_dir",
            "encrypt-file = pycryptobox.encryption:encrpt_file",
            "decode-decrypt-dir = pycryptobox.decryption:decrypt_dir",
            "decrypt-file = pycryptobox.decryption:decrypt_file",
        ]
    },
    install_requires=["pyAesCrypt==6.0.0", "python-dotenv"],
    author="Lpcodes",
    author_email="lovelesh_p@outlook.com",
    description="A package for encrypting and decrypting files",
    long_description=long_description,
    keywords="encryption decryption file-security cryptography",
    url="https://github.com/LpCodes/pycryptobox",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Archiving :: Compression",
    ],
    include_package_data=True,
)
