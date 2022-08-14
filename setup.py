import setuptools

setuptools.setup(
    name="achae",
    version="v1",
    author="Matheus Carneiro",
    author_email="matheus.carneiro.dev@gmail.com",
    description="Mecanismo de busca pelo CLI",
    url="https://github.com/mtscarneiro/Achae",
    project_urls={
        "Bug Tracker": "https://github.com/mtscarneiro/Achae/issues",
    },
    entry_points = {
        'console_scripts': [
            'achae = acha.achae:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    keywords = ['achae', 'cli', 'search in command line'],
    zip_safe = False,
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)