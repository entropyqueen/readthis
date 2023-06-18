from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='readthis',
    version='0.0.5',
    description='readthis - A command line tool to read a text file aloud',
    author='Emy Canton',
    author_email='emy.canton@proton.me',
    url='https://github.com/entropyqueen/readthis',
    license='MIT',
    scripts=['readthis'],
    setup_requires=[
        'setuptools',
        'wheel',
    ],
    install_requires=[
        'gTTS==2.3.2',
        'pydub==0.25.1',
    ],
    package_data={
        'readthis': ['data/*.txt'],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
