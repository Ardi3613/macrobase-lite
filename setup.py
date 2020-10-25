import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="macrobase",
    version="0.0.1",
    author="Piotr Zakrzewski",
    author_email="crvc-no-reply@protonmail.com",
    description="Minimalistic implementation of Macrobase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PiotrZakrzewski/mb-lite",
    packages=["mb_lite"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["pandas", "scipy", "numpy", "efficient_apriori"],
    entry_points={"console_scripts": ["mb=mb_lite:main"]},
)
