from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      long_description='Really, the funniest around.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke commedy flying circus',
      url='https://github.com/milanoid/funniest.git',
      author='Milan Vojnovic',
      author_email='milan.vojnovic@gmail.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
