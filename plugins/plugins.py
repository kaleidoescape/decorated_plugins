import re

from decorators import register_plugin

@register_plugin(name='replace_tags')
def replace_tags(sentence):
    """
    Replace xml tags with a <TAG> token.

    >>> replace_tags("replace <xml> tags")
    'replace <TAG> tags'
    """
    return re.sub(r'</?\w*?>', '<TAG>', sentence)

@register_plugin(name='replace_urls')
def replace_urls(sentence):
    """
    Replace urls with a <URL> token.

    >>> replace_urls("replace example.com")
    'replace <URL>'
    """
    return re.sub(r'\w*?.(?:com|org)', '<URL>', sentence)
