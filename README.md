# Device Fingerprint Library

This Python library generates a unique digital fingerprint based on the physical characteristics of an electronic device. The fingerprint is generated using the device's current battery status, exact system time (down to milliseconds), and MAC address. The library also includes functionality for encrypting and decrypting the collected data using AES encryption.

## Installation

Install the required dependencies:

```bash
pip install psutil cryptography
