from setuptools import find_packages, setup

setup(
    name="your-package-name",
    version="0.1.0",
    description="A very nice python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
    ],
    install_requires=[
        "setuptools",
    ],
    extras_require={
        "test": ["pytest"],
        "benchmark": ["pytest-benchmark"],
    },
)
