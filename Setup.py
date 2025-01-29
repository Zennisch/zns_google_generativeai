from setuptools import setup, find_packages

setup(
    name="zns_google_generativeai",
    version="1.0.0",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zennisch",
    author_email="zennisch@gmail.com",
    url="https://github.com/Zennisch/zns_google-generativeai",
    packages=find_packages(),
    install_requires=[
        "zns_logging",
        "google",
        "google-generativeai",
    ],
    python_requires=">=3.10",
)
