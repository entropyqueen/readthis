from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='readit',
    version='1.0',
    description='readit - A command line tool to read a text file aloud',
    author='Emy Canton',
    author_email='emy.canton@proton.me',
    url='https://github.com/entropyqueen/readit',
    license='MIT',
    scripts=['readit'],
    install_requires=[
        'certifi==2023.5.7',
        'charset-normalizer==3.1.0',
        'click==8.1.3',
        'gTTS==2.3.2',
        'idna==3.4',
        'pydub==0.25.1',
        'requests==2.31.0',
        'urllib3==2.0.3',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
