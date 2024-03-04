from setuptools import setup

setup(
    name='cli1',
    version='0.1.0',
    py_modules=['CLI14_DZ_F'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cli1 = CLI14_DZ_F:main',
        ],
    },
)