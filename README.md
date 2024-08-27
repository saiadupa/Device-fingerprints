---

# Device Fingerprint

`device_fingerprint` is a Python library designed to generate a unique digital fingerprint based on the physical characteristics of an electronic device. It captures details like the device's battery status, exact system time (with millisecond precision), and MAC address. This library also provides secure handling of data by hashing with SHA-256 and encrypting using AES encryption.

## Features

- **Generate Device Fingerprint**: Create a unique fingerprint based on device characteristics.
- **Encrypt and Decrypt Data**: Securely encrypt and decrypt data using AES encryption.
- **Retrieve Device Information**: Get current battery status, system time, and MAC address.

## Installation

To install the `device_fingerprint` library, use `pip`:

```bash
pip install device-fingerprint
```

## Usage

### Generating a Fingerprint

Here's how to use the `device_fingerprint` library to generate a unique fingerprint:

```python
from device_fingerprint import DeviceFingerprint

# Define a 16-byte key for AES encryption
# AES key must be either 16, 24, or 32 bytes long
key = b'ThisIs16BytesKey!'

# Initialize the DeviceFingerprint class with your encryption key
fingerprint_generator = DeviceFingerprint(encryption_key=key)

# Generate a unique fingerprint for the device
fingerprint = fingerprint_generator.generate_fingerprint()
print(f"Fingerprint: {fingerprint}")

# Retrieve the device's MAC address
mac_address = fingerprint_generator.get_mac_address()
print(f"MAC Address: {mac_address}")

# Encrypt and decrypt data
encrypted_mac = fingerprint_generator.encrypt_data(mac_address)
print(f"Encrypted MAC Address: {encrypted_mac}")

decrypted_mac = fingerprint_generator.decrypt_data(encrypted_mac)
print(f"Decrypted MAC Address: {decrypted_mac}")
```

## API Reference

### `DeviceFingerprint`

- **Constructor: `DeviceFingerprint(encryption_key: bytes)`**
  - Initializes the `DeviceFingerprint` class with the specified AES encryption key.
  - `encryption_key`: A byte string for AES encryption. Must be 16, 24, or 32 bytes long.

- **Method: `generate_fingerprint()`**
  - Generates a unique fingerprint based on device characteristics.
  - Returns: A string representing the unique device fingerprint.

- **Method: `get_mac_address()`**
  - Retrieves the MAC address of the device.
  - Returns: A string representing the MAC address.

- **Method: `encrypt_data(data: str)`**
  - Encrypts the given data using AES encryption.
  - `data`: A string of data to encrypt.
  - Returns: A string representing the encrypted data.

- **Method: `decrypt_data(encrypted_data: str)`**
  - Decrypts the given encrypted data using AES decryption.
  - `encrypted_data`: A string of encrypted data.
  - Returns: A string representing the decrypted data.

## Security

- Ensure that your AES encryption key is kept secure and private.
- The library uses SHA-256 for hashing and AES for encryption to provide secure data handling.
---

Feel free to adjust the repository links and license details as needed.
