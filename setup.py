from setuptools import setup

import stimprep
long_description = 'Prepare audio files for stimulus presentation',
setup(
    name='stimprep',
    scripts=['stimprep.py'],
    version=stimprep.__version__,
    url='http://github.com/kylerbrown/stimprep',
    license='GPL',
    author='Kyler Brown',
    install_requires=['numpy',
                      'scipy',
                      'matplotlib',
                      ],
    author_email='kylerjbrown@gmail.com',
    description=long_description,
    long_description=long_description,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
    ],
)
