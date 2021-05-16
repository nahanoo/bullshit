from setuptools import setup, find_packages

setup(name='bullshit',
      version='1.0',
      description='Bullshit the dice game',
      author='Eric Ulrich',
      #author_email='gward@python.net',
      url='https://github.com/nahanoo/bullshit',
      #packages=['bullshit'],
      #package_dir={'': 'bullshit'},
      install_requires=['pillow>=8.0.1'],
      packages=find_packages(),
     )