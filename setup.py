from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
       name='brat2CoNLL',
       version='1.0',
       description='A convertor from brat annotation format to CoNLL format for the Named Entity Recognition task',
       author='Pranav Shetty',
       author_email='pranav.shetty@gatech.edu',
       packages=find_packages(),  
       install_requires=[],
    )
