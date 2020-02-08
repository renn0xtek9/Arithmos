from setuptools import setup

setup(
    name="Demo",
    packages=["arithmosdemo"],
    package_data={"arithmosdemo": ["icons/*.svg"]},
    classifiers=["Example :: Invalid"],
    # Declare arithmosdemo package to contain widgets for the "Demo" category
    entry_points={"arithmos.widgets": "Demo = arithmosdemo"},
)
