from setuptools import setup, find_packages

setup(
    name='howto',
    version='1.0.0',
    description='A command-line tool for security testing and assessment',
    author='GDDev',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'howto=howto.main:main',
        ],
    },
)

