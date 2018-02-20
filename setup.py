from distutils.core import setup

setup(name='python-cryptowatch',
      version='0.0.1',
      author='uoshvis',
      packages=['cryptowatch'],
      install_requires=[
          'requests==2.18.4',
          'urllib3==1.22'
      ])
