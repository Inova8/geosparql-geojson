from setuptools import setup


def get_version() -> str:
    from pathlib import Path

    with open(Path(__file__).parent / "geojson" / "__init__.py") as file_:
        for line in file_.readlines():
            if line.startswith("__version__"):
                return line.split('"')[1]
        return ''


setup(
    name="geosparql-geojson",
    version=get_version(),
    description="GeoSPARQL DGGS functions implemented as SPARQL extension in RDFLib",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    maintainer="Peter Lawrence",
    maintainer_email="peter.lawrence@inova8.com",
    url="https://github.com/Inova8/geosparql-geojson",
    license="BSD",
    packages=["geojson"],
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    test_suite="tests",
    install_requires=["rdflib>=6.0.0", "shapely"],
    tests_require=["pytest"],
)