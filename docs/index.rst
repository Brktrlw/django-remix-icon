Django Remix Icon Documentation
=================================

.. image:: https://img.shields.io/pypi/v/django-remix-icon.svg
   :target: https://pypi.org/project/django-remix-icon/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/django-remix-icon.svg
   :target: https://pypi.org/project/django-remix-icon/
   :alt: Python versions

.. image:: https://img.shields.io/badge/django-3.2%2B-blue.svg
   :target: https://www.djangoproject.com/
   :alt: Django versions

.. image:: https://img.shields.io/github/license/brktrlw/django-remix-icon.svg
   :target: https://github.com/brktrlw/django-remix-icon/blob/main/LICENSE
   :alt: License

A Django package that provides model fields and template tags for integrating Remix Icons
into Django projects. This package makes it easy to use Remix Icons in your Django models,
forms, and templates with a beautiful and user-friendly interface.

Features
--------

* **Model Field**: Store Remix Icon identifiers in your Django models
* **Template Tags**: Simple and powerful template tags for rendering icons
* **Flexible Styling**: Support for size, color, and custom CSS classes
* **Dynamic Icons**: Use variables and conditions for dynamic icon selection
* **Type-Safe**: Full Python type hints support
* **Zero Dependencies**: Only requires Django
* **Responsive Design**: Works seamlessly on desktop and mobile
* **Custom Attributes**: Support for data attributes and HTML attributes

Quick Start
-----------

Install the package:

.. code-block:: bash

   pip install django-remix-icon

Add to your Django settings:

.. code-block:: python

   INSTALLED_APPS = [
       # ... your other apps
       'django_remix_icon',
   ]

Usage Examples
-------------

Model Field Usage
~~~~~~~~~~~~~~~~

Create a model with an icon field:

.. code-block:: python

   from django.db import models
   from django_remix_icon.fields import RemixIconField

   class Article(models.Model):
       title = models.CharField(max_length=200)
       icon = RemixIconField(
           blank=True,
           null=True,
           default='article-line',
           help_text='Choose an icon for this article'
       )

Template Usage with Model Field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Render icons from your model fields:

.. code-block:: html

   {% load remix_icon_tags %}

   <h1>
       {% remix_icon article.icon size="24px" color="#007bff" extra_class="text-blue-500" data_tooltip="Article Icon" %}
       {{ article.title }}
   </h1>

Static Icon Usage
~~~~~~~~~~~~~~~~

Use icons without a model field:

.. code-block:: html

   {% load remix_icon_tags %}

   <nav>
       <a href="{% url 'home' %}">
           {% remix_icon 'home-line' size="20px" color="#333" extra_class="nav-icon" data_tooltip="Home" %}
           Home
       </a>
       <a href="{% url 'profile' %}">
           {% remix_icon 'user-line' size="20px" color="#666" extra_class="nav-icon" data_tooltip="Profile" %}
           Profile
       </a>
   </nav>

Dynamic Icon Selection
~~~~~~~~~~~~~~~~~~~~~

Use conditions to select icons dynamically:

.. code-block:: html

   {% load remix_icon_tags %}

   <!-- User status -->
   {% if user.is_authenticated %}
       {% remix_icon 'user-fill' size="18px" color="#22c55e" %}
   {% else %}
       {% remix_icon 'user-line' size="18px" color="#94a3b8" %}
   {% endif %}

   <!-- File type -->
   {% if document.file_type == 'pdf' %}
       {% remix_icon 'file-pdf-line' size="24px" color="#ef4444" %}
   {% elif document.file_type == 'image' %}
       {% remix_icon 'image-line' size="24px" color="#3b82f6" %}
   {% else %}
       {% remix_icon 'file-line' size="24px" color="#6b7280" %}
   {% endif %}

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   usage/fields
   usage/templatetags
   usage/admin
   usage/widgets

.. toctree::
   :maxdepth: 2
   :caption: Examples

   examples/basic
   examples/advanced
   examples/customization

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/fields
   api/widgets
   api/templatetags
   api/constants

.. toctree::
   :maxdepth: 1
   :caption: About

   license
   authors

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
