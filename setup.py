import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="develocorder",
    version="0.1",
    author="Alexander Wah Tak Metz",
    author_email="alexander.wt.metz@gmail.com",
    description="Simple live value plotter using Matplotlib",
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
    install_requires=["numpy", "matplotlib"],
)
