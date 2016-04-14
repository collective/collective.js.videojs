from setuptools import setup, find_packages

version = '5.8.9.dev0'
description = 'Integration of  Video.js, an open source HTML5 & Flash video player, in Plone.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='collective.js.videojs',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
      ],
      keywords='plone',
      author='Rodrigo Ferreira de Souza aka rodfersou',
      author_email='rodfersou@gmail.com',
      url='https://github.com/collective/collective.js.videojs',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
