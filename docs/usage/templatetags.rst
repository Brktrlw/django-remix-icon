Template Tags
=============

Django Remix Icon provides template tags to easily render Remix Icons in your templates.

Loading Template Tags
---------------------

Load the template tags in your template:

.. code-block:: html

   {% load remix_icon_tags %}

Available Template Tags
-----------------------

remix_icon
~~~~~~~~~~

The main template tag for rendering icons.

**Basic Syntax:**

.. code-block:: html

   {% remix_icon 'icon-name' %}

**With Options:**

.. code-block:: html

   {% remix_icon 'icon-name' size="24px" extra_class="custom-class" data_tooltip="Icon Title" %}

remix_icon_css
~~~~~~~~~~~~~~~

Include the Remix Icons CSS file:

.. code-block:: html

   {% remix_icon_css %}

Parameters
----------

icon_name (required)
~~~~~~~~~~~~~~~~~~~

The name of the Remix Icon to render:

.. code-block:: html

   {% remix_icon 'home-line' %}
   {% remix_icon 'user-fill' %}
   {% remix_icon 'settings-3-line' %}

size (optional)
~~~~~~~~~~~~~~~

The size of the icon. Accepts any CSS size value:

.. code-block:: html

   {% remix_icon 'home-line' size="16px" %}
   {% remix_icon 'home-line' size="1.5rem" %}
   {% remix_icon 'home-line' size="24" %}

extra_class (optional)
~~~~~~~~~~~~~~~~~~~~~~

Additional CSS classes:

.. code-block:: html

   {% remix_icon 'home-line' extra_class="text-blue-500" %}
   {% remix_icon 'home-line' extra_class="nav-icon text-large" %}

style (optional)
~~~~~~~~~~~~~~~~

Inline CSS styles:

.. code-block:: html

   {% remix_icon 'home-line' style="color: red; margin-right: 8px;" %}

Additional Attributes
~~~~~~~~~~~~~~~~~~~~~

Pass any HTML attribute using underscores (converted to hyphens):

.. code-block:: html

   {% remix_icon 'home-line' data_tooltip="Go to homepage" %}
   {% remix_icon 'user-line' id="user-icon" title="User profile" %}
   {% remix_icon 'search-line' aria_label="Search" %}

Generated HTML
--------------

The template tag generates an ``<i>`` element:

.. code-block:: html

   <!-- Input -->
   {% remix_icon 'home-line' size="24px" extra_class="text-blue" data_tooltip="Home" %}

   <!-- Output -->
   <i class="ri-home-line text-blue"
      style="font-size: 24px;"
      data-tooltip="Home"
      aria-hidden="true"></i>

Using with Models
-----------------

Use with model fields:

.. code-block:: html

   {% load remix_icon_tags %}

   {% remix_icon article.icon %}
   {% remix_icon category.icon size="20px" %}
   {% remix_icon menu_item.icon extra_class="nav-icon" data_tooltip=category.name %}

Using Variables
---------------

Use with template variables:

.. code-block:: html

   {% remix_icon icon_name %}
   {% remix_icon icon_name size=icon_size %}
   {% remix_icon item.icon size=settings.icon_size extra_class=item.css_class %}

Static Usage
------------

Use without model fields:

.. code-block:: html

   <!-- Navigation -->
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

   <!-- Buttons -->
   <button type="submit">
       {% remix_icon 'save-line' size="16px" extra_class="btn-icon" %}
       Save
   </button>

   <button type="button" class="btn-danger">
       {% remix_icon 'delete-bin-line' size="16px" extra_class="btn-icon" %}
       Delete
   </button>

Dynamic Icons
-------------

Show different icons based on conditions:

.. code-block:: html

   <!-- User status -->
   {% if user.is_authenticated %}
       {% remix_icon 'user-fill' size="18px" extra_class="text-green-500" %}
   {% else %}
       {% remix_icon 'user-line' size="18px" extra_class="text-gray-400" %}
   {% endif %}

   <!-- File types -->
   {% if file.type == 'pdf' %}
       {% remix_icon 'file-pdf-line' size="24px" extra_class="file-icon" %}
   {% elif file.type == 'image' %}
       {% remix_icon 'image-line' size="24px" extra_class="file-icon" %}
   {% else %}
       {% remix_icon 'file-line' size="24px" extra_class="file-icon" %}
   {% endif %}

   <!-- Status indicators -->
   {% if task.completed %}
       {% remix_icon 'check-circle-fill' size="18px" extra_class="text-green-500" %}
   {% elif task.in_progress %}
       {% remix_icon 'time-line' size="18px" extra_class="text-yellow-500" %}
   {% else %}
       {% remix_icon 'circle-line' size="18px" extra_class="text-gray-400" %}
   {% endif %}

Size Units
----------

The ``size`` parameter accepts any CSS size unit:

.. code-block:: html

   {% remix_icon 'home-line' size="16px" %}    <!-- Pixels -->
   {% remix_icon 'home-line' size="1rem" %}    <!-- Relative to root font size -->
   {% remix_icon 'home-line' size="1.5em" %}   <!-- Relative to parent font size -->
   {% remix_icon 'home-line' size="120%" %}    <!-- Percentage -->
   {% remix_icon 'home-line' size="24" %}      <!-- Numbers (converted to pixels) -->

Error Handling
--------------

Invalid icon names show a warning:

.. code-block:: html

   {% remix_icon 'invalid-icon-name' %}
   <!-- Renders: <span class="remix-icon-error" title="Invalid icon: invalid-icon-name">⚠️</span> -->

The ``remix_icon_css`` Template Tag
----------------------------------

.. autofunction:: django_remix_icon.templatetags.remix_icon_tags.remix_icon_css

Usage
~~~~~

Add the Remix Icons CSS to your base template:

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

This will automatically include the latest version of Remix Icons from CDN.
