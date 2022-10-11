import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Genskew_cc",
    version="0.1.2",
    author="Thomas Rattei, Julius Krämer",
    url="https://genskew.csb.univie.ac.at/genskew_cc",
    description="A program that calculates genskew.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Creative Commons",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
          'matplotlib',
          'Biopython',
          'argparse',
          'Genskew_univiecube',
          'GUIskew',
      ],
)
