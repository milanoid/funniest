from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/milanoid/funniest.git',
      author='Milan Vojnovic',
      author_email='milan.vojnovic@gmail.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)

