from setuptools import setup, find_packages

setup(
    name="facebook-dataset-analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
    ],
    author="Prem",
    description="Analysis tool for Facebook Marketplace data",
    python_requires=">=3.8",
)
