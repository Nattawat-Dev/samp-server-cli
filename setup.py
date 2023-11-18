from distutils.core import setup

setup(
  name='samp-server-cli',
  version='1.0',
  author='NattawatDev',
  author_email='nattawatwichaiyo1@gameil.com',
  url='https://github.com/Zeex/samp-server-cli',
  description='Developer By Nattawat Dev',
  license='BSD',
  py_modules = ['samp_server_cli'],
  entry_points = {
    'console_scripts': ['samp-server-cli=samp_server_cli:main']
  },
)
