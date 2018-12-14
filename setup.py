# encoding=utf8
from setuptools import setup

version = '0.0.1'

long_description = '腾讯AI开放平台API'

setup(
    name='aiplat',
    version=version,
    url='https://github.com/FloydaGithub/aiplat',
    author='Floyda',
    author_email='floyda@163.com',
    description=long_description,
    long_description=long_description,
    py_modules=['apiutil'],
    zip_safe=False
)
