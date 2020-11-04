import os
from setuptools import setup

with open(os.path.join('VERSION')) as version_file:
    VERSION = version_file.read().strip()

setup(name='calculator',
      version=VERSION,
      description='Simple Calculator',
      url='https://github.com/AkshatBajaj/simple-calculator',
      author='Akshat Bajaj',
      author_email='akshat.bajaj@outlook.com',
      include_package_data=True,
      packages=[
        'calculator'
      ],
      license="BSD-3-Clause License",
      zip_safe=False)
