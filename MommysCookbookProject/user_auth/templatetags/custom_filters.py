from django import template

register = template.Library()


@register.filter
def placeholder(input_field, placeholder_text):
    input_field.field.widget.attrs["placeholder"] = placeholder_text
    return input_field


@register.filter
def add_custom_class(input_field, custom_class):
    input_field.field.widget.attrs["class"] = custom_class
    return input_field
