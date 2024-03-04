"""
setup.py нужен для заупска CLI_DZ.py через команду cli1
"""

from setuptools import setup


setup(
    name='cli1',
    version='0.1.0',
    py_modules=['CLI_DZ'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cli1 = CLI_DZ:main',
        ],
    },
)
