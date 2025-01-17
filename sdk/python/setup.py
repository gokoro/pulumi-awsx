# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-awsx. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.0"
def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "awsx Pulumi Package - Development Version"


setup(name='pulumi_awsx',
      python_requires='>=3.7',
      version=VERSION,
      description="Pulumi Amazon Web Services (AWS) AWSX Components.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords='pulumi aws awsx kind/component category/cloud',
      url='https://pulumi.com',
      project_urls={
          'Repository': 'https://github.com/pulumi/pulumi-awsx'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'pulumi_awsx': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.76.1,<4.0.0',
          'pulumi-aws>=6.0.4,<7.0.0',
          'pulumi-docker>=4.4.3,<5.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
