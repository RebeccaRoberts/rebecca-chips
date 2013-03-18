from setuptools import setup, find_packages

setup(
    name='jmbo-ic-project',
    version='0.0.1',
    description='A tool to hold information about ICs.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Rebecca Roberts',
    author_email='becci.rr@gmail.com',
    license='BSD',
    url='',
    packages = find_packages(),
    install_requires = [
        'jmbo-foundry>=1.1.15',
    ],
    include_package_data=True,
    tests_require = []
    test_suite="setuptest.setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 1 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
