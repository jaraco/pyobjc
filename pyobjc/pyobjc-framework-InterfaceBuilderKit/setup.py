''' 
Wrappers for framework 'InterfaceBuilderKit'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: To run the unittests for this framework use::

    $ env DYLD_FRAMEWORK_PATH='/Developer/Library/PrivateFrameworks/' python setup.py test

This is needed because the InterfaceBuilderKit framework won't load otherwise.
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-InterfaceBuilderKit',
    version='2.2b1',
    description = "Wrappers for the framework InterfaceBuilderKit on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "InterfaceBuilderKit" ],
    package_dir = { '': 'Lib' },
    setup_requires = [ 
    ],
    install_requires = [ 
        'pyobjc-core>=2.2b1', 
        'pyobjc-framework-Cocoa>=2.2b1', 
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('InterfaceBuilderKit'),
    zip_safe = True,
)