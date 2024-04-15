import setuptools

long_describe = ''
long_describe_format = 'text/markdown'

with open('README.md','r') as readmeFile:
    long_describe = readmeFile.read()

setuptools.setup(
    name='HiveWebCrawler',
    author='MehmetYukselSekeroglu',
    version='0.0.4',
    author_email='dijital_evren@protonmail.com',
    description='Python 3.x Web Crawler, Images, Urls, Emails, Phone numbers',
    long_description=long_describe,
    long_description_content_type=long_describe_format,
    keywords='PyPi, Web Crawler, Web Image Crawler, Web URL Crawler, Web Email Crawler, Web Phone Number Crawler',
    project_urls={
        'Bug Reports':'https://github.com/MehmetYukselSekeroglu/HiveWebCrawler/issues',
        'Source Code':'https://github.com/MehmetYukselSekeroglu/HiveWebCrawler'
    },
    url='https://github.com/MehmetYukselSekeroglu/HiveWebCrawler',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=['requests','beautifulsoup4'], 
)