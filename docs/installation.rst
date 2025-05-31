Installation
============

Requirements
------------

Django Remix Icon requires:

* Python 3.8 or higher
* Django 3.2 or higher

Supported Django Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Django 3.2 LTS
* Django 4.0
* Django 4.1
* Django 4.2 LTS
* Django 5.0

Supported Python Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Python 3.8
* Python 3.9
* Python 3.10
* Python 3.11
* Python 3.12

Install with pip
----------------

Install Django Remix Icon using pip:

.. code-block:: bash

   pip install django-remix-icon

Configuration
-------------

Add ``django_remix_icon`` to your ``INSTALLED_APPS``:

.. code-block:: python

   # settings.py
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',

       # Add django_remix_icon
       'django_remix_icon',

       # Your other apps
       'myapp',
   ]

CDN Configuration
----------------

By default, Django Remix Icon uses the Remix Icons CDN from cdnjs. You can override this in your settings:

.. code-block:: python

   # settings.py
   REMIX_ICON_CDN_URL = "https://your-custom-cdn-url/remixicon.css"

This setting is used by both the template tags and the admin widget.

Include Remix Icons CSS
-----------------------

Add the Remix Icons CSS to your base template using the template tag. This will automatically include the latest version of Remix Icons from CDN:

.. code-block:: html

   {% load remix_icon_tags %}

   <!DOCTYPE html>
   <html>
   <head>
       {% remix_icon_css %}
   </head>
   <body>
       <!-- Your content -->
   </body>
   </html>

The template tag automatically includes the latest version of Remix Icons from CDN (currently using `cdn.jsdelivr.net`). This ensures you always have access to the latest icons and optimizes loading performance.

Collect Static Files
--------------------

Run collectstatic:

.. code-block:: bash

   python manage.py collectstatic

That's it! You're ready to use Django Remix Icon.

Next Steps
----------

* :doc:`quickstart` - Learn how to use Django Remix Icon
* :doc:`usage/fields` - Learn about the RemixIconField
* :doc:`usage/templatetags` - Learn about template tags
