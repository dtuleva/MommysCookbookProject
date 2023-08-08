from django import template

register = template.Library()


@register.filter
def rating_stars(value):
    full_stars = int(value)
    half_star = value - full_stars >= 0.5

    stars = []
    for i in range(5):
        if i < full_stars:
            stars.append('fa-solid fa-star')
        elif i == full_stars and half_star:
            stars.append('fa-regular fa-star-half-stroke')
        else:
            stars.append('fa-regular fa-star')

    return stars