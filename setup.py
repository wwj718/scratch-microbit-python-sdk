from setuptools import setup

setup(
    name='microbitble',
    version='0.1',
    description='Python SDK for scratch-microbit HEX',
    long_description='A Python SDK, which provides an API for connecting and controlling micro:bit(with scratch-microbit HEX). Requires BLED112 Bluetooth LE module.',
    url='https://github.com/wwj718/scratch-microbit-python-sdk',
    author='wwj718',
    author_email='wuwenjie718@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: Software Development'
    ],
    keywords='SDK microbit education',
    packages=[
        "microbitble",
        "microbitble.bluetooth",
        "microbitble.input_output",
        "microbitble.services",
        "microbitble.utils"
    ],
    install_requires=['pygatt==3.1.1']
)

