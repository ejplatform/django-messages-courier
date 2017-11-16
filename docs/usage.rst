=====
Usage
=====

To use Django Courier in a project, add it to your `INSTALLED_APPS`:

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
