from setuptools import setup, find_packages

setup(
    name='titanic-survival-predictor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn'
        
    ],
    author='Sakshi Sonawane',
    author_email='sakshisonawanepatil@gmail.com',
    description='Predicting Titanic Passenger Survival',
    url='https://github.com/sakshisonawane12/TITANIC-SURVIVAL-PREDICTION',
    
)