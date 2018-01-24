"""The module that setup loklak python API."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

description = "Python API for loklak, Anonymous distributed P2P Systems."
try:
    long_description = open("README.rst").read()
except IOError:
    long_description = description
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
setup(name='python-loklak-api',
      version='1.7',
      description=description,
      long_description=long_description,
      author='Sudheesh Singanamalla',
      author_email='sudheesh95@gmail.com',
      url='https://github.com/loklak/loklak_python_api',
      license='',
      include_package_data=True,
      platforms='Linux/Mac',
      py_modules=['loklak'],
      python_requires='>=2.7.0',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Internet',
      ],
      keywords="Twitter Loklak Anonymous API",
      install_requires=requirements,
      zip_safe=False,
      download_url='https://github.com/loklak/loklak_python_api/archive/v1.7.tar.gz',
      scripts=['bin/loklak']
      )
