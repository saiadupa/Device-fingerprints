import unittest
from device_fingerprint import DeviceFingerprint

class TestDeviceFingerprint(unittest.TestCase):

    def setUp(self):
        self.encryption_key = b'Sixteen byte key' 
        self.fingerprint_generator = DeviceFingerprint(self.encryption_key)

    def test_generate_fingerprint(self):
        fingerprint = self.fingerprint_generator.generate_fingerprint()
        self.assertIsNotNone(fingerprint)
        print(f"Fingerprint: {fingerprint}")

    def test_encrypt_decrypt(self):
        mac_address = self.fingerprint_generator.get_mac_address()
        encrypted_mac = self.fingerprint_generator.encrypt_data(mac_address)
        decrypted_mac = self.fingerprint_generator.decrypt_data(encrypted_mac)
        self.assertEqual(mac_address, decrypted_mac)
        print(f"Original MAC: {mac_address}")
        print(f"Decrypted MAC: {decrypted_mac}")

if __name__ == '__main__':
    unittest.main()
