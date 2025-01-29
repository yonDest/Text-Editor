from setuptools import setup, find_packages

setup(
    name="notes-app",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "notes_app": ["resources/*.png"],
    },
    install_requires=[
        "typing-extensions; python_version < '3.8'",
        "pillow",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "notes-app=notes_app.main:main",  # Changed from notepad to notes-app
        ],
    },
    author="Yoni Desta",
    author_email="yonidesta9@gmail.com",
    description="A notepad application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/yonDest/Text-Editor",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Text Editors",
    ],
    python_requires=">=3.6",
)