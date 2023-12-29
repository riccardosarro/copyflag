from setuptools import setup, find_packages

setup(
    name='CopyFlag',
    version='0.1',
    packages=find_packages(),
    description='Package to search and copy to clipboard if found a flag in a text',
    author='Ricy',
    author_email='riccardoricy@gmail.com',
    url='',
    install_requires=[
        'pyperclip',
    ],
)