from setuptools import setup, find_packages

setup(name='bullshit',
      version='1.0',
      description='Bullshit the dice game',
      author='Eric Ulrich',
      url='https://github.com/nahanoo/bullshit',
      packages=find_packages(),
      install_requires=['pillow>=8.0.1',
                        'names>=0.3.0'],
      include_package_data=True,
      package_data={'':['dices/*.png']}
     )