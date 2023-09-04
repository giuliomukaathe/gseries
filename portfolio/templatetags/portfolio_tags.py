from django import template

register = template.Library()

@register.filter
def get_unique_categories(portfolio_items):
    categories = set(item.category for item in portfolio_items)
    return categories
