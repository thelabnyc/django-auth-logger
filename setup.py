from setuptools import setup, find_packages

setup(
    name="django-auth-logger",
    version="1.0.0",
    author="David Burke",
    author_email="david@thelabnyc.com",
    description="A tiny project to log login attempts. Log them only to standard logging - not the database.",
    license="Apache License",
    keywords="django wagtail",
    url="https://gitlab.com/thelabnyc/wagtail-links",
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
)

