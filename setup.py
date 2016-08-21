from setuptools import setup

setup(
    name='read_env',
    version=__version__,
    py_modules=['read_env'],
    description='Read .env files for your python project',
    long_description=read('README.md'),
    author='Alexis Leon',
    author_email='alexis.leon@icloud.com',
    url='https://github.com/AlexisLeon/read_env',
    install_requires=[],
    license='MIT',
    zip_safe=False,
    keywords='env environment variables',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)