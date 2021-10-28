from setuptools import setup

REQUIREMENTS = [
    "click==8.0.3",
    "Pillow==8.4.0"
]

setup(
    name='imgsz',
    version='0.1',
    py_modules=['imgsz'],
    install_requires=REQUIREMENTS,
    entry_points='''
        [console_scripts]
        imgsz=src.cli.main:cli
    ''',
)

