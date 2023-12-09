from setuptools import setup, find_packages

setup(
    name="your_package_name",
    version="0.1.0",
    description="Your package description",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/your_username/your_package_name",
    packages=find_packages(where="src"),
    install_requires=[
        "requirement1",
        "requirement2",
    ],
)