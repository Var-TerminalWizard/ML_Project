from setuptools import setup,find_packages
from typing import List
def get_requirements(file_path)->List[str]:
    require=[]
    with open(file_path) as f:
        require=f.readlines()
        [req.replace('\n','') for req in require]
    if '-e .' in require:        require.remove('-e .')
    return require


setup(
    name='ML_Project',
    version='0.0.1',
    author='Varun',
    author_email='bestavarunsai@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)