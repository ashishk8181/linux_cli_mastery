import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='format_lesson')
def format_lesson(text):
    """Format lesson content with inline code and bold text"""
    # Replace `code` with styled inline code
    text = re.sub(
        r'`([^`]+)`',
        r'<code class="bg-slate-900/50 px-2 py-0.5 rounded text-green-400">\1</code>',
        text
    )
    # Replace **bold** with white bold text
    text = re.sub(
        r'\*\*([^*]+)\*\*',
        r'<strong class="text-white">\1</strong>',
        text
    )
    return mark_safe(text)
