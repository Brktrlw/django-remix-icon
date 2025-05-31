"""Model fields for the remix_icon app."""

from typing import Any, Optional

from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_remix_icon.constants import ALL_ICONS, ICON_CHOICES
from django_remix_icon.widgets import RemixIconWidget


class RemixIconField(models.CharField):
    """
    A CharField that stores Remix Icon identifiers and provides admin integration.

    This field automatically provides a dropdown widget in the admin with icon
    previews and search functionality.
    """

    description = _("A Remix Icon identifier")

    def __init__(
        self,
        verbose_name: Optional[str] = None,
        name: Optional[str] = None,
        max_length: int = 100,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the RemixIconField.

        Args:
            verbose_name: Human-readable name for the field
            name: Field name
            max_length: Maximum length of the icon identifier
            **kwargs: Additional field options
        """
        # Set default values
        kwargs.setdefault("choices", ICON_CHOICES)
        kwargs.setdefault("help_text", _("Choose a Remix Icon for this field"))

        super().__init__(
            verbose_name=verbose_name, name=name, max_length=max_length, **kwargs
        )

    def validate(self, value: Any, model_instance: Any) -> None:
        """
        Validate that the icon identifier is valid.

        Args:
            value: The value to validate
            model_instance: The model instance

        Raises:
            ValidationError: If the icon identifier is invalid
        """
        super().validate(value, model_instance)

        if value and value not in [icon[0] for icon in ALL_ICONS]:
            raise ValidationError(
                _("'%(value)s' is not a valid Remix Icon identifier."),
                code="invalid_choice",
                params={"value": value},
            )

    def formfield(self, **kwargs: Any) -> forms.Field:
        """
        Return a form field for this model field.

        Args:
            **kwargs: Additional formfield options

        Returns:
            The form field instance
        """
        # Set the custom widget
        kwargs.setdefault("widget", RemixIconWidget)

        # Call parent formfield method
        return super().formfield(**kwargs)

    def deconstruct(self) -> tuple:
        """
        Return details for Django migrations.

        Returns:
            Tuple containing field details for migrations
        """
        name, path, args, kwargs = super().deconstruct()

        # Remove choices from kwargs as they're set automatically
        if "choices" in kwargs and kwargs["choices"] == ICON_CHOICES:
            del kwargs["choices"]

        return name, path, args, kwargs

    def get_prep_value(self, value: Any) -> Optional[str]:
        """
        Prepare value for saving to database.

        Args:
            value: The value to prepare

        Returns:
            The prepared value
        """
        if value is None or value == "":
            return None
        return str(value)

    def to_python(self, value: Any) -> Optional[str]:
        """
        Convert value to Python representation.

        Args:
            value: The value to convert

        Returns:
            The Python representation of the value
        """
        if value is None or value == "":
            return None
        return str(value)

    def value_to_string(self, obj: Any) -> str:
        """
        Convert value to string for serialization.

        Args:
            obj: The model instance

        Returns:
            String representation of the value
        """
        value = self.value_from_object(obj)
        return self.get_prep_value(value) or ""
