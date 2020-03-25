import sys
from codecs import open

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

MAJOR               = 0
MINOR               = 0
MICRO               = 4
VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


class PyTest(TestCommand):
    """Handle test execution from setup."""

    user_options = [('pytest-args=', 'a', "Arguments to pass into pytest")]

    def initialize_options(self):
        """Initialize the PyTest options."""
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def finalize_options(self):
        """Finalize the PyTest options."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run the PyTest testing suite."""
        try:
            import pytest
        except ImportError:
            raise ImportError('Running tests requires additional dependencies.'
                              '\nPlease run (pip install moviepy[test])')

        errno = pytest.main(self.pytest_args.split(" "))
        sys.exit(errno)


cmdclass = {'test': PyTest}  # Define custom commands.

# Define the requirements for specific execution needs.
requires = [
]

test_reqs = [
        'pytest-cov>=2.5.1',
        'pytest>=3.0.0',
        'coveralls>=1.1,<2.0',
        'rstvalidator',
]

doc_reqs = [
        'sphinx_rtd_theme>=0.1.10b0S',
        'Sphinx>=1.5.2',
]

extra_reqs = {
    "doc": doc_reqs,
    "test": test_reqs
}

with open('README.rst', 'r', 'utf-8') as fh:
    long_description = fh.read()
print(long_description)
setup(
    name="pyser",
    version=VERSION,
    author="Jonne Kaunisto",
    author_email="jonneka@gmail.com",
    description="Python Serializer and Deserializer",
    long_description=long_description,
    url="https://github.com/jonnekaunisto/pyser",
    license='MIT License',
    keywords="serialize, deserialize",
    packages=find_packages(exclude=['docs', 'test']),
    cmdclass=cmdclass,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    tests_require=test_reqs,
    extras_require=extra_reqs,
)
