from setuptools import setup

setup(
    name="termii_sdk",
    version="1.0",
    description="The `termii_sdk` is a Python package that facilitates seamless integration with the Termii API, empowering developers to send SMS, voice, and email messages within their applications.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=["termii_sdk"],
    install_requires=["requests"],
)
