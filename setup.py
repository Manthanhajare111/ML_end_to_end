from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'
def get_requiremets(file_path:str)->List[str]:
    '''
    This function will return the requirements list
    '''
    requiremets = []
    with open(file_path) as file_obj:
        requiremets = file_obj.readlines()
        requiremets = [req.replace('\n','') for req in requiremets]

        if hypen_e_dot in requiremets:
            requiremets.remove(hypen_e_dot)

    return requiremets

setup(
name="mlproject",
version='0.0.1',
author="Manthan",
author_email='manteshwarhajare@gmail.com',
packages=find_packages(),
install_requires = get_requiremets('requirements.txt')



)