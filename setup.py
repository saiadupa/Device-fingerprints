from setuptools import setup, find_packages

setup(
    name='device_fingerprint',
    version='0.1',
    description='A Python library to generate a unique digital fingerprint based on the physical characteristics of an electronic device.',
    author='Adupa Nithin Sai',
    author_email='adupanithinsai@gmail.com',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'cryptography'
    ],
)
