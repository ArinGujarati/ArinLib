# setup.py

from setuptools import setup, find_packages

setup(
    name='ArinLib',
    version='0.2',
    packages=find_packages(),
    description='A Simplify and accelerate your machine learning and deep learning projects with ease.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arin Gujarati',
    author_email='aeringujarati1110@gmail.com',
    url='https://github.com/ArinGujarati/ArinLib',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
