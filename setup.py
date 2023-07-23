from setuptools import find_packages, setup
import pmt

with open("pmt/README.md", "r") as f:
    long_description = f.read()

setup(
    name="posaydones-material-theming",
    version="1.0.0",
    description="Small gui + cli app for managing your colorscheme using material color utilities",
    packages=find_packages(),
    package_data={"data": ["*.ui"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/posaydone/pmt",
    author="posaydone",
    author_email="poseaydone@ya.ru",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["toml", "material-color-utilities-python", "chevron", "pygobject"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'pmt=pmt.__main__:main',
        ],
    },
)
