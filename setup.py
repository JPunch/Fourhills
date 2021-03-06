import setuptools

setuptools.setup(
    name="fourhills",
    version="0.0.1",
    author="Simeon Jenkins",
    author_email="55206+smuj@users.noreply.github.com",
    description="A package for managing D&D campaigns",
    license="GPL",
    packages=setuptools.find_packages(exclude=["*.tests"]),
    include_package_data=True,
    install_requires=[
        "appdirs",
        "beautifulsoup4",
        "click",
        "dataclasses",
        "jinja2",
        "markdown",
        "pyyaml",
        "PyQt5",
    ],
    extras_require={
        "dev": ["pytest", "flake8"],
        "install": ["cx_freeze"],
    },
    entry_points={
        'console_scripts': [
            '4h = fourhills.fourhills:main',
            'fourhills = fourhills.fourhills:main',
        ],
        'gui_scripts': [
            '4hgui = fourhills.gui.main_window:main',
        ],
    }
)
