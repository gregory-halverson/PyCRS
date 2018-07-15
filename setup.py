from os.path import join, abspath, dirname

try:
    from setuptools import setup
except:
    from distutils.core import setup

with open(join(abspath(dirname(__file__)), 'requirements.txt'), 'r') as f:
    install_requires = f.readlines()

setup(
    long_description=open("README.rst").read(),
    name="""PyCRS""",
    license="""MIT""",
    author="""Karim Bahgat""",
    author_email="""karim.bahgat.norway@gmail.com""",
    url="""http://github.com/karimbahgat/PyCRS""",
    version="""0.1.4""",
    keywords="""GIS spatial CRS coordinates format""",
    packages=['pycrs', 'pycrs/elements'],
    classifiers=['License :: OSI Approved', 'Programming Language :: Python', 'Development Status :: 4 - Beta',
                 'Intended Audience :: Developers', 'Intended Audience :: Science/Research',
                 'Intended Audience :: End Users/Desktop', 'Topic :: Scientific/Engineering :: GIS'],
    description="""GIS package for reading, writing, and converting between CRS formats.""",
    install_requires=install_requires
)
