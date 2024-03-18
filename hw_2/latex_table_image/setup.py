from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='latex_table_and_image',
  version='0.0.2',
  author='denisd',
  author_email='denisderkach2003@gmail.com',
  description='Latex generator',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://upload.pypi.org/legacy/',
  packages=find_packages(),
  install_requires=['requests>=2.25.1',
                    "pillow>=10.2.0"],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/Dpbt'
  },
  python_requires='>=3.6'
)