=============================
Django Courier
=============================

.. image:: https://badge.fury.io/py/django-courier.svg
    :target: https://badge.fury.io/py/django-courier

.. image:: https://travis-ci.org/luanguimaraesla/django-courier.svg?branch=master
    :target: https://travis-ci.org/luanguimaraesla/django-courier

.. image:: https://codecov.io/gh/luanguimaraesla/django-courier/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/luanguimaraesla/django-courier

Simple notification framework for Django

Documentation
-------------

The full documentation is at https://django-courier.readthedocs.io.

Quickstart
----------

Install Django Courier::

    pip install django-courier

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'courier.apps.CourierConfig',
        ...
    )

Add Django Courier's URL patterns:

.. code-block:: python

    from courier import urls as courier_urls


    urlpatterns = [
        ...
        url(r'^', include(courier_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
