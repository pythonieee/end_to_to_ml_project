from setuptools import find_packages,setup
from typing import List
hyphen_e_dot='-e .'
def get_requirements(file_path:str)->List[str] :
    '''
    This function will return all my dependencies 
    '''
    requiments=[]
    with open(file_path) as file_obj :
        requiments=file_obj.readlines()
        requiments=[req.replace('\n','') for req in requiments ]

        if hyphen_e_dot in requiments:
            requiments.remove(hyphen_e_dot)
        return requiments

setup(
    name="Mlproject",
    author="Vedant Patil",
    author_email="vedantsp2007@gmail.com",
    packages=find_packages(),
    version='0.0.1',
    install_requires=get_requirements("requirements.txt")
 
)