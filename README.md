# Device Fingerprint
```markdown

`device_fingerprint` is a Python library designed to generate a unique digital fingerprint based on the physical characteristics of an electronic device. This includes the device's current battery status, exact system time (with millisecond precision), and the MAC address. The library provides functionality to hash these parameters using SHA-256 and encrypt them using AES encryption for secure data handling.

## Features

- **Generate Device Fingerprint**: Create a unique fingerprint based on device characteristics.
- **Encrypt and Decrypt Data**: Securely encrypt and decrypt data using AES encryption.
- **Retrieve Device Information**: Get current battery status, system time, and MAC address.

## Installation

You can install the package using `pip`:

```bash
pip install device_fingerprint
```

## Usage

### Generating a Fingerprint

Here’s how to use the `device_fingerprint` library to generate a unique fingerprint:

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
