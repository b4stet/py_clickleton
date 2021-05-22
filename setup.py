from setuptools import setup, find_packages


entrypoints = """
[console_scripts]
py_clickleton=clickleton.cli:cli
"""

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()


setup(
    name='py_clickleton',
    version='0.1',
    author="b4stet",
    description="a CLI short description",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url="URL of the project",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points=entrypoints,
)
