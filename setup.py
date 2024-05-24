from setuptools import setup, find_packages

setup(
    name='http_load_tester',  # Defines the package name
    version='0.1.0',  # Defines the package version
    packages=find_packages(),  # Finds and includes all packages (directories with __init__.py)
    install_requires=[  # Specifies dependencies that pip will install
        'requests',
        'click'
    ],
    entry_points={  # Defines entry points for command-line scripts
        'console_scripts': [
            'http_load_tester=http_load_tester.cli:main'
        ]
    },
)
