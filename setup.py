from codecs import open

from setuptools import find_packages, setup

# Package information
AUTHOR = "Damego"
AUTHOR_EMAIL = "danyabatueff@gmail.com"
DESCRIPTION = "REST api for your bot"
PROJECT_NAME = "interactions-simple-api"
MAIN_PACKAGE_NAME = "interaction.ext.api"
URL = "https://github.com/Damego/interactions-simple-api"

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()


setup(
    name=PROJECT_NAME,
    version="0.0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    include_package_data=True,
    install_requires=requirements,
    license="GPL-3.0 License",
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
