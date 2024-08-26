from setuptools import find_packages,setup
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:        #['pandas','numpy','seaborn']
   
    """
    This funciton will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace('\n','') for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements
        



setup(name='INDUSTRY PROJECT',
      version='1.0',
      description='I am trying to the write the modular coding of the ml with the help of krish naik',
      author='Vishnu Vardhan',
      author_email='vishnuvardhankalva8@gmail.com',
      packages= find_packages(),     #['distutils', 'distutils.command'],
      install_requires= get_requirements('requirements.txt')              #['pandas','numpy','seaborn']
     )