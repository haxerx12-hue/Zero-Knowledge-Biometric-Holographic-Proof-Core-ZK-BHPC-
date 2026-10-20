from setuptools import setup, find_packages
setup(
    name="zk_bhpc",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy", "pyserial", "cryptography"],
)
