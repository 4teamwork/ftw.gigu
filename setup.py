import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'ftw.gigu'
VERSION = '0.0.1'
AUTHOR = '4teamwork'
EMAIL = 'info@4teamwork.ch'
DESCRIPTION = 'Pings into pull requests which are not reviewed/proceeding.'
URL = 'https://github.com/4teamwork/ftw.gigu'
REQUIRED = [
    'python-dotenv==0.9.1',
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
        'console_scripts': ['ping_everywhere=gigu.command_line:main'],
    },
)
