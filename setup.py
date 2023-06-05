from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ensembl_converter',
    version='0.0.1',
    author='Muhammad Ammar Malik',
    author_email='malik.ammar1993@gmail.com',
    description='Convert Ensembl IDs to gene symbols',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmmarMalik93/ensembl-converter",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'tqdm',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
