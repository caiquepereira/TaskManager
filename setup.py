from setuptools import setup, find_packages
from ez_setup import use_setuptools
use_setuptools()


setup(
    name='ImagePlugins',
    version="1.0",
    description="Image plugins for the imaginary CMS 1.0 project",
    author="James Gardner",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["CMS>=1.0"],
    entry_points={
        'image.plugin': [
            'jpg_image = image_plugins:tweet_closed_task',
            'png_image = image_plugins:tweet_closed_project',
        ],
    },
)
