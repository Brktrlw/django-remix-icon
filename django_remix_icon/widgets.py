"""Custom widgets for Django Remix Icon package."""

from typing import Any, Dict, Optional

from django.forms import Media, Widget
from django.forms.widgets import Select
from django.utils.safestring import mark_safe
from django.conf import settings

from django_remix_icon.constants import ICON_CHOICES, REMIX_ICONS
from django_remix_icon.defaults import REMIX_ICON_CDN_URL


class RemixIconWidget(Widget):
    """
    A custom select widget for choosing Remix Icons with preview functionality.

    This widget provides:
    - Icon previews in the dropdown options
    - Search functionality
    - Organized by categories
    - Live preview of selected icon
    """

    template_name = 'django_remix_icon/widgets/remix_icon_widget.html'

    class Media:
        css = {
            "all": [
                getattr(settings, 'REMIX_ICON_CDN_URL', REMIX_ICON_CDN_URL),
                "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css",
                "django_remix_icon/css/remix-icon-widget.css",
                "django_remix_icon/css/admin.css",
            ]
        }
        js = [
            "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js",
            "django_remix_icon/js/remix-icon-widget.js",
        ]

    def __init__(self, attrs: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize the RemixIconWidget.

        Args:
            attrs: Widget attributes
        """
        default_attrs = {
            "class": "remix-icon-select",
            "data-widget": "remix-icon",
        }
        if attrs:
            default_attrs.update(attrs)

        super().__init__(attrs=default_attrs, choices=ICON_CHOICES)

    @property
    def media(self) -> Media:
        """
        Return the media files needed for this widget.

        Returns:
            Media instance with CSS and JS files
        """
        return Media(
            css={
                "all": [
                    getattr(settings, 'REMIX_ICON_CDN_URL', REMIX_ICON_CDN_URL),
                    "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css",
                    "django_remix_icon/css/remix-icon-widget.css",
                    "django_remix_icon/css/admin.css",
                ]
            },
            js=[
                "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js",
                "django_remix_icon/js/remix-icon-widget.js",
            ],
        )

    def create_option(
        self,
        name: str,
        value: Any,
        label: str,
        selected: bool,
        index: int,
        subindex: Optional[int] = None,
        attrs: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Create an option for the select widget with icon preview.

        Args:
            name: The option name
            value: The option value
            label: The option label
            selected: Whether the option is selected
            index: The option index
            subindex: The option subindex
            attrs: Additional attributes

        Returns:
            Option dictionary
        """
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )

        # Add icon preview data if value is not empty
        if value and value != "":
            option["attrs"]["data-icon"] = value
            # Create preview HTML with icon
            icon_html = f'<i class="ri-{value}"></i>'
            option["attrs"]["data-preview"] = icon_html

        return option

    def format_value(self, value: Any) -> str:
        """
        Format the value for display.

        Args:
            value: The value to format

        Returns:
            Formatted value
        """
        if value is None or value == "":
            return ""
        return str(value)

    def render(
        self,
        name: str,
        value: Any,
        attrs: Optional[Dict[str, Any]] = None,
        renderer=None,
    ) -> str:
        """
        Render the widget as HTML.

        Args:
            name: The widget name
            value: The widget value
            attrs: Widget attributes
            renderer: Template renderer

        Returns:
            HTML string
        """
        if attrs is None:
            attrs = {}

        # Ensure value is properly formatted
        if value is None:
            value = ""

        # Add data attributes for JavaScript
        attrs.update(
            {
                "data-current-value": value or "",
                "data-categories": mark_safe(self._get_categories_json()),
            }
        )

        # Get the base select HTML and return it directly
        return super().render(name, value, attrs, renderer)

    def _get_categories_json(self) -> str:
        """
        Get categories data as JSON string for JavaScript.

        Returns:
            JSON string with categories data
        """
        import json

        return json.dumps(REMIX_ICONS)
