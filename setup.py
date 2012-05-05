from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='fifteenminutesoffame',
      version=version,
      description="A social website with curated content.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Aleksandr Vladimirskiy',
      author_email='aleksandr@butchershopcreative.com',
      url='http://fifteenminutesoffame.butchershopcreative.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
