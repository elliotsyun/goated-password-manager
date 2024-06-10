from setuptools import setup, find_packages

setup(
    name="goated-password-manager",
    version="1.0.0",
    author="Elliot Yun",
    author_email="elliot.yun@example.com",
    description="A password manager with encryption features",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/goated-password-manager",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pycryptodome>=3.9.9"
    ],
    test_suite='tests',
)
