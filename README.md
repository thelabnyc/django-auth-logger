# Django Auth Logger 

# Purpose

This is a modest django app that contains how thelab likes to log authentication
for staff users.
It may be useful to others, but could easily just be copied.

# Install

1. `pip install django-auth-logger`
2. Add `auth_logger` to INSTALLED_APPS

# Usage

By default log in success and failure is logged to standard python logging INFO.

In the future we may decide to add more configuration options.

# Contribution

The scope of this project is small and specific - but we welcome adding configuration settings
to change behavior and meet more use cases. All configuration options should have a test to
verify it works.

If we do add said configuration it should look something like

```
AUTH_LOGGER = {
    'LOG_ONLY_STAFF': True
}
```
