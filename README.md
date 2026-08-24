# XOR_Enc

A lightweight, dependency-free command-line tool for encrypting and decrypting text using the XOR cipher, written in pure Python.

## Overview

XOR_Enc demonstrates the fundamentals of symmetric-key encryption using the bitwise XOR operation. The same key is used to both encrypt and decrypt a message, and the cipher works by repeating the key over the length of the input data and XOR-ing byte by byte. Encrypted output is hex-encoded for safe display and transport as plain text.

> **Note:** XOR with a repeating key is a classic teaching cipher, not a secure encryption scheme for real-world use. It's vulnerable to frequency analysis and known-plaintext attacks, especially with short or reused keys. This project is intended for learning purposes — see [Security Notes](#security-notes) below.

## Features

- Simple, readable Python implementation of the XOR cipher
- Encrypts arbitrary text input using a user-supplied key
- Outputs ciphertext as a hex string for easy copy/paste or storage
- Decrypts hex-encoded ciphertext back to the original message
- No external dependencies — runs with the Python standard library only

## How It Works

1. **Encryption** (`Encryption.py`)
   - Takes plaintext and a key as input
   - Converts both to bytes
   - XORs each byte of the plaintext with the corresponding byte of the key (repeating the key as needed)
   - Encodes the resulting bytes as a hex string and prints it

2. **Decryption** (`Decryption.py`)
   - Takes the hex-encoded ciphertext and the same key used for encryption
   - Converts the hex string back to bytes
   - XORs each byte with the repeating key to recover the original plaintext
   - Decodes and prints the recovered message

Since XOR is its own inverse, the same operation is used for both directions — only the input/output framing differs.

## Requirements

- Python 3.x
- No third-party libraries required

## Usage

### Encrypt a message

```bash
python Encryption.py
```

You'll be prompted for:
- The data (plaintext) you want to encrypt
- The encryption key

Example:
```
Plz input data you want to encrypt: Hello World
plz input encryption key: mykey
Encrypted message:  2d041e1807120e0010...
```

### Decrypt a message

```bash
python Decryption.py
```

You'll be prompted for:
- The encrypted (hex) message
- The same key that was used to encrypt it

Example:
```
plz input encrypted message: 2d041e1807120e0010...
plz input Encryption key: mykey
Hello World
```

## Project Structure

```
XOR_Enc/
├── Encryption.py   # Encrypts plaintext into a hex-encoded XOR cipher
├── Decryption.py   # Decrypts a hex-encoded XOR cipher back to plaintext
└── README.md
```

## Security Notes

This project was built to explore the mechanics of symmetric encryption and byte-level operations in Python, not to provide production-grade security. Key limitations of the XOR cipher as implemented here:

- **Key reuse** across a long message leaks patterns that can be exploited via frequency analysis.
- **No authentication** — there's no way to detect if a message has been tampered with.
- **No key derivation or salting** — keys are used as-is.

For real-world encryption needs, use established, audited libraries such as Python's `cryptography` package (Fernet, AES-GCM, etc.).

## Future Improvements

- [ ] Add file encryption/decryption support (not just text)
- [ ] Add command-line arguments (argparse) instead of interactive prompts
- [ ] Add unit tests
- [ ] Compare against a proper symmetric cipher (e.g., AES) as a learning extension

## Author

**Kanchana Samarakoon** (Tharindu)
- GitHub: [@smtkanchana66](https://github.com/smtkanchana66)
- Blog: [smtkanchana66.github.io](https://smtkanchana66.github.io/blog.html)
