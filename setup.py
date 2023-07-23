from setuptools import setup

setup(
    name="wing_api",
    packages=["wing_api", "wing_api.resources"],
    version="0.0.1",
    include_package_data=True,
    install_requires=["fastapi"],
)
