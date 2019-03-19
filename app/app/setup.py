from setuptools import setup, find_packages

setup(
    name='myapi',
    version='0.0.4',
    packages=find_packages(exclude=["tests.*", "tests"]),
    author="",
    author_email="",
    description="",
    license="",
    keywords="",
    url="",
    zip_safe=False,
    install_requires=["requests",
                      "Flask",
                      "connexion[swagger-ui]"],
    package_data={'myapi': ['openapi.yaml']}
)
