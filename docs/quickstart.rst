Quick Start Guide
==================

This guide will help you get up and running with Django Remix Icon in just a few minutes.

Basic Usage
-----------

1. Create a Model with Icon Field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a model that uses a Remix Icon:

.. code-block:: python

   # models.py
   from django.db import models
   from django_remix_icon.fields import RemixIconField

   class Category(models.Model):
       name = models.CharField(max_length=100)
       icon = RemixIconField()
       description = models.TextField(blank=True)

       def __str__(self):
           return self.name

2. Create and Run Migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

3. Include CSS in Base Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the Remix Icons CSS to your base template:

.. code-block:: html

   <!-- templates/base.html -->
   {% load remix_icon_tags %}

   <!DOCTYPE html>
   <html>
   <head>
       <title>My Django App</title>
       {% remix_icon_css %}
   </head>
   <body>
       {% block content %}{% endblock %}
   </body>
   </html>

4. Use in Templates
~~~~~~~~~~~~~~~~~~~

Display your categories with icons:

.. code-block:: html

   <!-- templates/categories.html -->
   {% extends "base.html" %}
   {% load remix_icon_tags %}

   {% block content %}
   <div class="categories">
       {% for category in categories %}
           <div class="category-item">
               {% remix_icon category.icon size="24px" extra_class="category-icon" %}
               <h3>{{ category.name }}</h3>
               <p>{{ category.description }}</p>
           </div>
       {% endfor %}
   </div>
   {% endblock %}

5. Create a View
~~~~~~~~~~~~~~~~

.. code-block:: python

   # views.py
   from django.shortcuts import render
   from .models import Category

   def category_list(request):
       categories = Category.objects.all()
       return render(request, 'categories.html', {'categories': categories})

Template Tags Usage
-------------------

Basic Icon Rendering
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   <!-- Simple icon -->
   {% remix_icon 'home-line' %}

   <!-- Icon with custom size -->
   {% remix_icon 'user-line' size="32px" %}

   <!-- Icon with CSS classes -->
   {% remix_icon 'settings-line' extra_class="text-blue-500" %}

   <!-- Icon with attributes -->
   {% remix_icon 'heart-fill' size="20px" extra_class="text-red-500" data_tooltip="Favorite" %}

Using with Model Objects
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   <!-- From model field -->
   {% remix_icon article.icon %}
   {% remix_icon category.icon size="20px" %}
   {% remix_icon category.icon size="24px" data_tooltip=category.name %}

Using Variables
~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   {% remix_icon icon_name size="16px" %}
   {% remix_icon icon_name size=icon_size extra_class=icon_class %}

Usage Without Model Fields
---------------------------

Static Icons
~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   <nav>
       <a href="{% url 'home' %}">
           {% remix_icon 'home-line' size="20px" extra_class="nav-icon" %}
           Home
       </a>
       <a href="{% url 'profile' %}">
           {% remix_icon 'user-line' size="20px" extra_class="nav-icon" %}
           Profile
       </a>
   </nav>

Dynamic Icon Selection
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   <!-- User status -->
   {% if user.is_authenticated %}
       {% remix_icon 'user-fill' size="18px" extra_class="text-green-500" %}
   {% else %}
       {% remix_icon 'user-line' size="18px" extra_class="text-gray-400" %}
   {% endif %}

   <!-- File type -->
   {% if document.file_type == 'pdf' %}
       {% remix_icon 'file-pdf-line' size="24px" extra_class="file-icon" %}
   {% elif document.file_type == 'image' %}
       {% remix_icon 'image-line' size="24px" extra_class="file-icon" %}
   {% else %}
       {% remix_icon 'file-line' size="24px" extra_class="file-icon" %}
   {% endif %}

CSS Sizing
----------

The size parameter accepts any CSS size unit:

.. code-block:: html

   {% load remix_icon_tags %}

   {% remix_icon 'home-line' size="16px" %}   <!-- Pixels -->
   {% remix_icon 'home-line' size="1rem" %}   <!-- Relative units -->
   {% remix_icon 'home-line' size="120%" %}   <!-- Percentage -->
   {% remix_icon 'home-line' size="20" %}     <!-- Numbers (converted to pixels) -->

Common Patterns
---------------

Navigation Menu
~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   <ul class="nav-menu">
       <li><a href="/">
           {% remix_icon 'home-line' size="18px" extra_class="nav-icon" %}
           Home
       </a></li>
       <li><a href="/blog/">
           {% remix_icon 'article-line' size="18px" extra_class="nav-icon" %}
           Blog
       </a></li>
       <li><a href="/contact/">
           {% remix_icon 'mail-line' size="18px" extra_class="nav-icon" %}
           Contact
       </a></li>
   </ul>

Buttons with Icons
~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   <button class="btn btn-primary">
       {% remix_icon 'save-line' size="16px" extra_class="btn-icon" %}
       Save
   </button>

   <button class="btn btn-danger">
       {% remix_icon 'delete-bin-line' size="16px" extra_class="btn-icon" %}
       Delete
   </button>

Status Indicators
~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% load remix_icon_tags %}

   {% for order in orders %}
       <div class="order-item">
           {% if order.status == 'completed' %}
               {% remix_icon 'check-circle-fill' size="20px" extra_class="text-success" %}
           {% elif order.status == 'processing' %}
               {% remix_icon 'time-line' size="20px" extra_class="text-warning" %}
           {% else %}
               {% remix_icon 'circle-line' size="20px" extra_class="text-muted" %}
           {% endif %}
           Order #{{ order.id }}
       </div>
   {% endfor %}

Next Steps
----------

* :doc:`usage/fields` - Learn about the RemixIconField
* :doc:`usage/templatetags` - Complete template tags reference
