============================
Django Authentication Logger
============================

|  |build| |license| |kit| |format|

This is a modest Django app that contains how thelab likes to log authentication for staff users. It may be useful to others, but could easily just be copied.


Install
=======

First, install the package from PyPI.

.. code-block:: bash

    pip install django-auth-logger

Then, add `auth_logger` to your Django project's `INSTALLED_APPS` setting.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'auth_logger',
        ...
    ]


Usage
=====

By default both successful and failed log-ins are logged to standard Python logging (at `INFO` level).

In the future we may decide to add more configuration options.


Contribution
============

The scope of this project is small and specific - but we welcome adding configuration settings to change behavior and meet more use cases. All configuration options should have a test to verify it works.

If we do add said configuration it will probably look something like this:

.. code-block:: python

    AUTH_LOGGER = {
        'LOG_ONLY_STAFF': True
    }



Changelog
=========

1.1.0
------------------
- Log all login attempts, instead of just logins for staff users.
- Fix bug which prevented failed login attempts from being correctly logged.

1.0.1
------------------
- Add support for Django 2.0.

1.0.0
------------------
- Initial release.


.. |build| image:: https://gitlab.com/thelabnyc/django-auth-logger/badges/master/build.svg
    :target: https://gitlab.com/thelabnyc/django-auth-logger/commits/master
.. |license| image:: https://img.shields.io/pypi/l/django-auth-logger.svg
    :target: https://pypi.python.org/pypi/
.. |kit| image:: https://badge.fury.io/py/django-auth-logger.svg
    :target: https://pypi.python.org/pypi/django-auth-logger
.. |format| image:: https://img.shields.io/pypi/format/django-auth-logger.svg
    :target: https://pypi.python.org/pypi/django-auth-logger
