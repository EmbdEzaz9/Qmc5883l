import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qmc5883l",
    version="0.2.9",
    author="EmbdEzaz9",
    author_email="embdezaz9@gmail.org",
    description="Python driver for the QMC5883L 3-axis magnetic sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EmbdEzaz9/qmc5883l",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
