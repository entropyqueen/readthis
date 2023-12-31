from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='readthis',
    version='0.1.1',
    description='readthis - A command line tool to read a text file aloud',
    author='Emy Canton',
    author_email='emy.canton@proton.me',
    url='https://github.com/entropyqueen/readthis',
    license='MIT',
    setup_requires=[
        'setuptools',
        'wheel',
    ],
    install_requires=[
        'gTTS==2.3.2',
        'pydub==0.25.1',
        'validators==0.20.0',
        'trafilatura==1.6.1',
    ],
    packages=['readthis'],
    package_dir={'readthis': 'src/readthis'},
    package_data={
        'readthis': ['data/*.txt'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'readthis = readthis.readthis:main',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
