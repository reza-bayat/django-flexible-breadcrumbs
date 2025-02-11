from setuptools import setup, find_packages

setup(
    name='django-flexible-breadcrumbs',
    version='0.1.0',
    description='A flexible and customizable breadcrumbs package for Django projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Reza Bayat',
    author_email='mrrezabayat@gmail.com.com',
    url='https://github.com/reza-bayat/django-flexible-breadcrumbs',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',  
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)