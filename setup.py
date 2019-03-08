import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'ftw.gigu'
VERSION = '0.0.1'
AUTHOR = '4teamwork'
EMAIL = 'info@4teamwork.ch'
DESCRIPTION = 'Analyzes data from github organisation.'
URL = 'https://github.com/4teamwork/ftw.gigu'
REQUIRED = [
    'python-dotenv==0.9.1',
    'github3.py==1.2.0',
    'matplotlib==3.0.2'
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': ['analyze_data=gigu.command_line:main'],
    },
)
