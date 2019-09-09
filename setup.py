import setuptools
from minds import version


with open("README.md", "r") as fh:
    long_description = fh.read()


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="minds",
    version=version,
    author="Alexandr Seleznyov",
    author_email="alexandr@getoffice.com.com",
    description="A package to provide a fancy text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexandrSeleznev/minds.git",
    packages=["minds"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
