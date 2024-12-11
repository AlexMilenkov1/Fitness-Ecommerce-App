from django import template

register = template.Library()


@register.filter
def star_rating(rating):
    MAX_RATING_STARS = 5

    full_stars = '<i class="fa fa-star"></i>' * rating
    empty_stars = '<i class="fa-regular fa-star"></i>' * (MAX_RATING_STARS - rating)

    return full_stars + empty_stars
