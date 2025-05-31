"""Template tags for rendering Remix Icons."""

from typing import Any, Dict, Optional

from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from django.conf import settings
from django_remix_icon.defaults import REMIX_ICON_CDN_URL

from django_remix_icon.constants import ALL_ICONS

register = template.Library()


@register.simple_tag
def remix_icon(
    icon_name: str,
    size: Optional[str] = None,
    color: Optional[str] = None,
    extra_class: Optional[str] = None,
    style: Optional[str] = None,
    **kwargs: Any,
) -> str:
    """
    Render a Remix Icon with customizable attributes.

    Usage:
        {% remix_icon "home-line" %}
        {% remix_icon "user-fill" size="20px" color="#007bff" %}
        {% remix_icon "settings-line" extra_class="text-blue-500" %}
        {% remix_icon "heart-fill" size="20px" color="red" data_tooltip="Favorite" %}

    Args:
        icon_name: The icon identifier (e.g., "home-line", "user-fill")
        size: Icon size - one of keys or any CSS size
        color: Icon color - any valid CSS color value
        extra_class: CSS classes to add to the icon
        style: Inline CSS styles
        **kwargs: Additional HTML attributes

    Returns:
        HTML string for the icon
    """
    # Validate icon exists
    if not icon_name:
        return ""

    # Check if icon exists in our icon list
    valid_icons = [icon[0] for icon in ALL_ICONS]
    if icon_name not in valid_icons:
        # Return empty string or placeholder for invalid icons
        return format_html(
            '<span class="remix-icon-error" title="Invalid icon: {}">⚠️</span>',
            icon_name,
        )

    css_classes = [f"ri-{icon_name}"]

    # Support both css_class and class
    class_value = extra_class or kwargs.pop("class", None)
    if class_value:
        css_classes.extend(class_value.split())

    # Build style attribute
    styles = []
    if size:
        styles.append(f"font-size: {size}")
    if color:
        styles.append(f"color: {color}")
    if style:
        styles.append(style)

    # Build attributes dictionary
    attrs = {
        "class": " ".join(css_classes),
        "aria-hidden": "true",  # Icons are decorative by default
    }

    if styles:
        attrs["style"] = "; ".join(styles)

    # Add any additional attributes
    for key, value in kwargs.items():
        # Convert underscores to hyphens for HTML attributes
        attr_name = key.replace("_", "-")
        attrs[attr_name] = value

    # Build attribute string
    attr_string = " ".join(f'{key}="{value}"' for key, value in attrs.items())

    return format_html("<i {}></i>", mark_safe(attr_string))


@register.simple_tag
def remix_icon_css() -> str:
    """
    Include the Remix Icons CSS file.

    Usage:
        {% remix_icon_css %}

    Returns:
        HTML link tag for Remix Icons CSS

    Note:
        You can override the CDN URL in your settings.py:
        REMIX_ICON_CDN_URL = "your-custom-cdn-url"
    """

    cdn_url = getattr(settings, 'REMIX_ICON_CDN_URL', REMIX_ICON_CDN_URL)
    return format_html('<link rel="stylesheet" href="{}"/>', cdn_url)


@register.inclusion_tag("django_remix_icon/icon_list.html")
def remix_icon_list(category: Optional[str] = None) -> Dict[str, Any]:
    """
    Render a list of available icons, optionally filtered by category.

    Usage:
        {% remix_icon_list %}
        {% remix_icon_list "System" %}

    Args:
        category: Optional category to filter icons

    Returns:
        Context dictionary for template
    """
    from django_remix_icon.constants import REMIX_ICONS

    if category and category in REMIX_ICONS:
        icons = REMIX_ICONS[category]
        categories = {category: icons}
    else:
        categories = REMIX_ICONS

    return {
        "categories": categories,
        "single_category": category,
    }
