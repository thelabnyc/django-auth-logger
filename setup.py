from setuptools import setup, find_packages, Distribution

Distribution().fetch_build_eggs('versiontag')

from versiontag import get_version, cache_git_tag  # NOQA


packages = find_packages('src')

install_requires = [
    'Django>=1.11',
    'django-ipware>=1.1.6',
]

extras_require = {
    'development': [
        'flake8>=3.2.1',
    ],
}

cache_git_tag()

setup(
    name="django-auth-logger",
    version=get_version(pypi=True),
    author="David Burke",
    author_email="david@thelabnyc.com",
    description="A tiny project to log login attempts. Log them only to standard logging - not the database.",
    license="Apache License",
    keywords="django wagtail",
    url="https://gitlab.com/thelabnyc/django-auth-logger",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=install_requires,
    extras_require=extras_require,
)
