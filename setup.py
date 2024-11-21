from setuptools import setup, find_packages

setup(
    name="Notes App",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # dependencies, e.g.:
        # "other_library>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "notepad=Notes App.main:main",
        ],
    },
    author="Yoni Desta",
    author_email="yonidesta9@gmail.com",
    description="A notepad application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/yonDest/Text-Editor",
)