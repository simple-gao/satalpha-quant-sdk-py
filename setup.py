from setuptools import setup, find_packages

setup(
    name="satalpha-quant-sdk-py",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["websockets>=11.0.3"],
    author="Your Name",
    author_email="you@example.com",
    description="A simple Python SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourname/satalpha-quant-sdk-py",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
