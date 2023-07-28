from django.core.exceptions import ValidationError


def validate_image_max_size_1_mb(image_object):
    if image_object.size > 1 * 1024 * 1024:
        raise ValidationError(f"The uploaded file exceeds the maximum allowed size of 1MB.")


def validate_image_max_size_5_mb(image_object):
    if image_object.size > 5 * 1024 * 1024:
        raise ValidationError(f"The uploaded file exceeds the maximum allowed size of 5MB.")







def validate_image_max_file_size(image_object, max_size):
    if image_object.size > max_size:
        max_size_in_mb = max_size / 1024
        raise ValidationError(f"The uploaded file exceeds the maximum allowed size of {max_size_in_mb:.1f}MB.")


class FileMaxSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size:
            max_size_in_mb = self.max_size / (1024 * 1024)
            raise ValidationError(f"The uploaded file exceeds the maximum allowed size of {max_size_in_mb:.1f}MB.")



def max_size_validator(max_size):
    def validate_image_size(value):
        if value.size > max_size:
            raise ValidationError(f"The maximum file size allowed is {max_size} bytes.")
    return validate_image_size


