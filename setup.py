import  setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_URL = "kidney_Disease_classfication_Mlops_project"
AUTHOR = "qosain-bukhari"
SRC_REPO = "kidney_disease_classification"
AUTHOR_EMAIL = "bukhariqosain824@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A Deep Learning Mlops project for Kidney Disease Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_URL}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_URL}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)
