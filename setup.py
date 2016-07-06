from setuptools import setup, find_packages
from ez_setup import use_setuptools
use_setuptools()


setup(
    name='TwitterPlugin',
    version="1.0",
    description="Twitter Plugin for the TaskManager project",
    author="Caique Pereira",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["CMS>=1.0"],
    entry_points={
        'twitter.plugin': [
            'tweet_task = twitter_plugin:tweet_closed_task',
            'tweet_project = twitter_plugin:tweet_closed_project',
        ],
    },
)
