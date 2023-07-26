from django.core.exceptions import ValidationError


def validate_image_max_file_size(image_object, max_size):
    if image_object.size > max_size:
        max_size_in_mb = max_size / 1024
        raise ValidationError(f"The uploaded file exceeds the maximum allowed size of {max_size_in_mb:.1f}MB.")

