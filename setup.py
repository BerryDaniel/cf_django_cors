from setuptools import setup, find_packages

with open('README.rst', 'r') as inp:
    LONG_DESCRIPTION = inp.read()

setup(
    name='cf_django_cors',
    version='1.0.0',
    author='Daniel Berry',
    author_email='dberry@boundlessgeo.com',
    url='https://github.com/boundlessgeo/cf_django_cors',
    download_url="https://github.com/boundlessgeo/cf_django_cors",
    description="django middleware to add cors response headers",
    long_description=LONG_DESCRIPTION,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Topic :: Utilities',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Operating System :: Other OS',
        'Programming Language :: Python :: 2.7',
    ]
)
