import setuptools

with open("README.md", "r", encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "ML_for_MLFlow"
AUTHER_USER_NAME = "naresh5422"
SRC_REPO = "ML_Project"
AUTHER_EMAIL = "naresh09022cm023@gmail.com"

setuptools.setup(
    name = SRC_REPO, 
    version=__version__, 
    author = AUTHER_USER_NAME,
    author_email = AUTHER_EMAIL, 
    description="A small python package for ML APP",
    long_description=long_description, 
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls ={"Bug_Trackers": f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",},
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where = "src"))