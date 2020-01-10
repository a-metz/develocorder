import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="develocorder-wahtak",
    version="0.1",
    author="Alexander Metz",
    author_email="alexander.wt.metz@gmail.com",
    description="Simple live value logger using matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wahtak/develocorder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["matplotlib"],
)
