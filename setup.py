import setuptools


setuptools.setup(
    name="HiveWebCrawler",
    author="MehmetYukselSekeroglu",
    version="0.0.1",
    author_email="dijital_evren@protonmail.com",
    description="Simple Python 3.x Web Crawler, Images, Urls, Emails, Phone numbers",
    long_description=None,
    url="https://github.com/MehmetYukselSekeroglu/HiveWebCrawler",
    package_dir={"":"HiveWebCrawler"},
    packages=setuptools.find_packages(where="HiveWebCrawler"),
    python_requires=">=3.8",
    install_requires=["requests","beautifulsoup4"]
)