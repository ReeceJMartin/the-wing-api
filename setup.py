from setuptools import setup

setup(
    name='the-wing-api',
    packages=['the-wing-api'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful'
    ],
)