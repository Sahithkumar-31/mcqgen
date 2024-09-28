from setuptools import find_packages,setup

setup(
    name= "env",
    version= "0.0.1",
    author = "Sahith",
    author_email= "sahithkumar.ksrs@gamil.com",
    install_requires = ["openai", "langchain", "streamlit", "Python-dotenv", "PyPDF2"],
    
    packages = find_packages()
)
