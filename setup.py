from setuptools import setup, find_packages, Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pycryptobox",
    version="1.0.7",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "encode-encrypt-dir = pycryptobox.encryption:encrypt_dir",
            "encrypt-file = pycryptobox.encryption:encrpt_file",
            "decode-decrypt-dir = pycryptobox.decryption:decrypt_dir",
            "decrypt-file = pycryptobox.decryption:decrypt_file",
        ]
    },
    include_package_data=True,
    install_requires=["setuptools==67.6.0", "keyring==23.13.1", "cryptography==39.0.1"],
    author="https://github.com/LpCodes",
    description="A package for encrypting and decrypting files",
    long_description_content_type="text/markdown",
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
    package_data={
        'pycryptobox': ['config.ini'],
    },
)
