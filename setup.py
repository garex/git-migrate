from setuptools import setup

import textwrap

# To redeploy run `python setup.py sdist bdist_wheel upload`

setup(
    name='git-migrate',
    version='0.2',
    description='Execute commands from shell file, storing last successful execution in detached git branch.',
    long_description=textwrap.dedent(open('README.rst', 'r').read()),
    keywords='git migrate shell script',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',
    ],
    url='https://github.com/garex/git-migrate',
    author='Alexander Ustimenko',
    author_email='a@ustimen.co',
    license='MIT',

    packages=['git_migrate'],
    entry_points = {
        'console_scripts': ['git-migrate=git_migrate.cli:main'],
    },

    include_package_data=True,
    zip_safe=False
)
