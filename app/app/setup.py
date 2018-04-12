from setuptools import setup, find_packages

setup(
    name='myapi',
    version='0.0.1',
    packages=find_packages(exclude=["tests.*", "tests"]),
    author="",
    author_email="",
    description="",
    license="",
    keywords="",
    url="",
    zip_safe=False,
    install_requires=["requests", "Flask", "connexion"],
    include_package_data=True
)
