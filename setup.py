from setuptools import setup

setup(
    name='vortexwebserver',
    packages=['vortexwebserver'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy'
    ],
)
