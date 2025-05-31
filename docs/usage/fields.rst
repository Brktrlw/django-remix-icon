Fields
=======

The RemixIconField
------------------

.. autoclass:: django_remix_icon.fields.RemixIconField
   :members:
   :undoc-members:
   :show-inheritance:

Basic Usage
-----------

Add a RemixIconField to your model:

.. code-block:: python

   from django.db import models
   from django_remix_icon.fields import RemixIconField

   class Category(models.Model):
       name = models.CharField(max_length=100)
       icon = RemixIconField()
       description = models.TextField(blank=True)

       def __str__(self):
           return self.name

Field Options
-------------

The RemixIconField accepts all standard Django field options:

.. code-block:: python

   class Article(models.Model):
       title = models.CharField(max_length=200)
       icon = RemixIconField(
           blank=True,
           null=True,
           default='article-line',
           help_text='Choose an icon for this article',
           verbose_name='Article Icon'
       )

Validation
----------

The field automatically validates that the provided value is a valid Remix Icon identifier:

.. code-block:: python

   from django.core.exceptions import ValidationError

   def validate_navigation_icon(value):
       """Validate that only navigation icons are used."""
       nav_icons = [
           'home-line', 'dashboard-line', 'settings-line',
           'user-line', 'logout-box-line'
       ]
       if value and value not in nav_icons:
           raise ValidationError(
               f'{value} is not a valid navigation icon.'
           )

   class MenuItem(models.Model):
       title = models.CharField(max_length=100)
       icon = RemixIconField(validators=[validate_navigation_icon])

Database Storage
---------------

The field stores icon names as VARCHAR fields in the database:

.. code-block:: sql

   CREATE TABLE myapp_category (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       icon VARCHAR(50)
   );

Querysets and Filtering
-----------------------

You can filter and query models using icon field values:

.. code-block:: python

   # Filter by specific icon
   categories = Category.objects.filter(icon='home-line')

   # Filter by multiple icons
   categories = Category.objects.filter(
       icon__in=['home-line', 'folder-line', 'file-line']
   )

   # Exclude specific icons
   categories = Category.objects.exclude(icon='delete-bin-line')

   # Check for empty icons
   categories_with_icons = Category.objects.exclude(icon='')
   categories_without_icons = Category.objects.filter(icon='')
