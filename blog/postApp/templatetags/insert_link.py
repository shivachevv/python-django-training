import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

url_pattern = re.compile(r'(https?://[^\s]+)')


@register.filter(name='insert_link')
def insert_link(value):

    def replace_with_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank">{url}</a>'

    return mark_safe(re.sub(url_pattern, replace_with_link, value))
