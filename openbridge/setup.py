import os, sys
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

requires = [
        'requests'
    ]

ver = sys.version_info[1]
if ver > 6:
    requires.append('rfc3987')

setup(name='openbridge',
      version='0.1',
      description='Openbridge API',
      url='https://github.com/openbridge/api-datavault',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
