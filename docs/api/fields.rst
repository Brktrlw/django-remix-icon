Fields API Reference
====================

.. automodule:: django_remix_icon.fields
   :members:
   :undoc-members:
   :show-inheritance:

RemixIconField
--------------

.. autoclass:: django_remix_icon.fields.RemixIconField
   :members:
   :undoc-members:
   :show-inheritance:

   .. method:: __init__(self, *args, **kwargs)

      Initialize a new RemixIconField.

      :param blank: Allow empty values in forms (default: False)
      :type blank: bool
      :param null: Allow NULL values in database (default: False)
      :type null: bool
      :param default: Default icon value
      :type default: str
      :param help_text: Help text for forms
      :type help_text: str
      :param verbose_name: Human-readable field name
      :type verbose_name: str
      :param validators: List of field validators
      :type validators: list

   .. method:: get_internal_type(self)

      Return the internal type for this field.

      :returns: The internal field type
      :rtype: str

   .. method:: to_python(self, value)

      Convert the value to a Python string.

      :param value: The value to convert
      :type value: str or None
      :returns: The converted value
      :rtype: str or None

   .. method:: validate(self, value, model_instance)

      Validate that the value is a valid Remix Icon identifier.

      :param value: The value to validate
      :type value: str
      :param model_instance: The model instance
      :raises ValidationError: If the value is not a valid icon

Example Usage
-------------

Basic Field Definition
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from django.db import models
   from django_remix_icon.fields import RemixIconField

   class Category(models.Model):
       name = models.CharField(max_length=100)
       icon = RemixIconField()

Field with Options
~~~~~~~~~~~~~~~~~~

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

Field with Custom Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Database Representation
-----------------------

The field stores icon names as VARCHAR fields in the database:

.. code-block:: sql

   CREATE TABLE myapp_category (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       icon VARCHAR(50)
   );

Validation Details
------------------

Icon Name Validation
~~~~~~~~~~~~~~~~~~~~

The field validates that the provided value is a valid Remix Icon identifier:

- Must be a string
- Must match the pattern of Remix Icon names (e.g., 'home-line', 'user-fill')
- Must exist in the list of available Remix Icons

Error Messages
~~~~~~~~~~~~~~

The field provides helpful error messages:

- ``"Invalid icon name: '{value}'"`` - When an invalid icon name is provided
- ``"This field cannot be blank."`` - When required field is left empty
- Custom validation messages from additional validators

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
