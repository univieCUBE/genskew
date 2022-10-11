import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Genskew-univiecube",
    version="0.1.3",
    author="Thomas Rattei, Julius Krämer",
    url="https://genskew.csb.univie.ac.at/library_documentation",
    description="A program that calculates the skew of two selectable nucleotides for a genome sequence in FASTA or GenBank format.",
    long_description=long_description,
    license="Creative Commons",
#    long_description="The minimum and maximum of a GC-skew can be used to predict the origin of replication (minimum) and the terminus location (maximum) in prokaryotic genomes.",
    long_description_content_type="text/markdown",
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
          'Genskew-cc',
          'GUIskew',
          'numpy',
      ],
)
