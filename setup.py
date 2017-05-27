from distutils.core import setup
from anita import __version__

setup(name='anita',
      version=__version__,
      description='Automated NetBSD Installation and Test Application',
      author='Andreas Gustafsson',
      author_email='gson@gson.org',
      url='http://www.gson.org/netbsd/anita/',
      py_modules=['anita'],
      scripts=['anita'],
      data_files=[('man/man1', ['anita.1'])],
      )
