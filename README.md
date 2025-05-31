# Django Remix Icon 🎨

[![PyPI version](https://img.shields.io/pypi/v/django-remix-icon.svg)](https://pypi.org/project/django-remix-icon/)
[![Python versions](https://img.shields.io/pypi/pyversions/django-remix-icon.svg)](https://pypi.org/project/django-remix-icon/)
[![Django versions](https://img.shields.io/badge/django-3.2%2B-blue.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/github/license/brktrlw/django-remix-icon.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://django-remix-icon.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A beautiful and powerful Django package that seamlessly integrates [Remix Icons](https://remixicon.com/) into your Django projects. 🚀

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/brktrl)

## ✨ Demo

![Demo](https://raw.githubusercontent.com/Brktrlw/django-remix-icon/refs/heads/main/screenshots/demo.gif)

## ✨ Features

- 🎯 **Model Field**: Store Remix Icon identifiers in your Django models
- 🎨 **Template Tags**: Simple and powerful template tags for rendering icons
- 🎭 **Flexible Styling**: Support for size, color, and custom CSS classes
- 🎪 **Dynamic Icons**: Use variables and conditions for dynamic icon selection
- 🎯 **Type-Safe**: Full Python type hints support
- 🚀 **Zero Dependencies**: Only requires Django
- 🎭 **Responsive Design**: Works seamlessly on desktop and mobile
- 🎨 **Custom Attributes**: Support for data attributes and HTML attributes

## 📦 Installation

```bash
pip install django-remix-icon
```

Add to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'django_remix_icon',
]
```

## 🚀 Quick Start

### 1. Use in Your Model

```python
from django.db import models
from django_remix_icon.fields import RemixIconField

class Article(models.Model):
    title = models.CharField(max_length=200)
    icon = RemixIconField()
```

### 2. Use in Templates

#### With Model Field

You can use the `remix_icon` template tag to render icons stored in your model fields. The tag supports various HTML attributes, such as `size`, `color`, `extra_class`, and `data_tooltip`. Note that underscores in attribute names (e.g., `data_tooltip`) are automatically converted to hyphens (e.g., `data-tooltip`) in the rendered HTML.

```html
{% load remix_icon_tags %}

<h1>
    {% remix_icon article.icon size="24px" color="#007bff" extra_class="text-blue-500" data_tooltip="Article Icon" %}
    {{ article.title }}
</h1>
```

#### Without Model Field (Static Usage)

You can also use the `remix_icon` tag without a model field, directly specifying the icon name. This is useful for static icons in your templates. You can add custom HTML attributes like `data_tooltip` to enhance the icon's functionality.

```html
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
```

#### Color Usage

The `color` parameter accepts any valid CSS color value:

```html
{% load remix_icon_tags %}

<!-- Using hex colors -->
{% remix_icon 'star-fill' color="#ff0000" %}

<!-- Using named colors -->
{% remix_icon 'heart-fill' color="red" %}

<!-- Using RGB/RGBA -->
{% remix_icon 'check-fill' color="rgb(0, 128, 0)" %}

<!-- Using HSL -->
{% remix_icon 'info-fill' color="hsl(240, 100%, 50%)" %}
```

### 3. Include CSS in Your Base Template

```html
{% load remix_icon_tags %}
<head>
    {% remix_icon_css %}
</head>
```

## 🎨 Advanced Usage

### Dynamic Icon Selection

```html
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
```

### Common Patterns

#### Navigation Menu
```html
<nav class="flex space-x-4">
    <a href="/" class="flex items-center">
        {% remix_icon 'home-line' size="20px" color="#3b82f6" %}
        <span class="ml-2">Home</span>
    </a>
    <a href="/blog" class="flex items-center">
        {% remix_icon 'article-line' size="20px" color="#3b82f6" %}
        <span class="ml-2">Blog</span>
    </a>
</nav>
```

#### Status Indicators
```html
<div class="flex items-center">
    {% if task.status == 'completed' %}
        {% remix_icon 'check-circle-fill' size="20px" color="#22c55e" %}
    {% elif task.status == 'in_progress' %}
        {% remix_icon 'time-line' size="20px" color="#f59e0b" %}
    {% else %}
        {% remix_icon 'circle-line' size="20px" color="#94a3b8" %}
    {% endif %}
    <span class="ml-2">{{ task.name }}</span>
</div>
```

## 📋 Requirements

- Python 3.8+
- Django 3.2+

## 📚 Documentation

- [Full Documentation](https://django-remix-icon.readthedocs.io/)
- [Remix Icons](https://remixicon.com/)

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Report bugs or request features via [GitHub Issues](https://github.com/brktrlw/django-remix-icon/issues)
- Submit pull requests with tests and documentation

## 📄 License

MIT License © 2025 Berkay Şen
