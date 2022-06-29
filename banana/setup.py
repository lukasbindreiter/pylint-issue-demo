import setuptools

setuptools.setup(
    name="banana",
    version="0.0.1",
    packages=setuptools.find_namespace_packages(include=["fruit2.*"]),
)