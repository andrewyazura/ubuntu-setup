from setuptools import setup, find_packages

setup(
    name="ubuntu_setup",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "ubuntu_setup": [
            "ubuntu_setup = ubuntu_setup:cli",
        ],
    },
)
