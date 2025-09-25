from setuptools import setup, find_packages
from typing import List

def get_requirements(requirements_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(requirements_path) as file_obejct:
        requriments = file_obejct.readlines()
        requriments = [req.replace('\n','') for req in requriments]

        if '-e .' in requriments:
            requriments.remove('-e .')
    return requriments
    



setup(name='ml_project',
    version='0.1.0',
    author='Sangameshgouda horapeti',
    author_email='sangameshgouda1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(requirements_path='requirements.txt')
    )