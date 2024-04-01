from streamlit import *

my_readme = open("README.md")
data = my_readme.read()

markdown(data)
