import setuptools

setuptools.setup(
    name="fruit1",
    version="0.0.1",
    packages=setuptools.find_namespace_packages(include=["fruit1.*"]),
)