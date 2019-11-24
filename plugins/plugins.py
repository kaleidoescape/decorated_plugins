import re
from abc import ABC, abstractmethod

from decorators import register_plugin

class Plugin(ABC):
    @abstractmethod
    def __call__(self, input: str) -> str:
        pass

@register_plugin(name='replace_tags')
class ReplaceTags(Plugin):
    def __call__(self, sentence):
        """
        Replace xml tags with a <TAG> token.

        >>> replace_tags("replace <xml> tags")
        'replace <TAG> tags'
        """
        return re.sub(r'</?\w*?>', '<TAG>', sentence)

@register_plugin(name='replace_urls')
class ReplaceUrls(Plugin):
    def __call__(self, sentence):
        """
        Replace urls with a <URL> token.

        >>> replace_urls("replace example.com")
        'replace <URL>'
        """
        return re.sub(r'\w*?.(?:com|org)', '<URL>', sentence)
