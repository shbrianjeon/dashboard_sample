from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dashboard_sample",
    version="0.1.0",
    author="Brian Jeon",
    # author_email="your.email@example.com",
    description="Just a sample dashboard",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/shbrianjeon/dashboard_sample",
    packages=find_packages(),
    install_requires=[
        "streamlit==0.89.0",
        "pandas==1.3.3",
        "numpy==1.21.2",
        "seaborn==0.11.2",
        "matplotlib==3.4.3",
        "plotly==5.3.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
