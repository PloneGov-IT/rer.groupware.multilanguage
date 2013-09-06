from Products.PloneLanguageTool.interfaces import INegotiateLanguage
from Products.PloneLanguageTool.LanguageTool import NegotiateLanguage as NegotiateLanguageBase
from zope.interface import implements


class NegotiateLanguage(object):
    """
    Perform default language negotiation.
    If we are in portal_factory, get parent's language, otherwise use default negotiator"""
    implements(INegotiateLanguage)

    def __init__(self, site, request):
        """Setup the current language stuff."""
        base_negotiate = NegotiateLanguageBase(site, request)
        self.default_language = base_negotiate.default_language
        self.language_list = base_negotiate.language_list
        if "portal_factory" in request.path:
            fixed_path = reversed(request.path[request.path.index('portal_factory') + 1:])
            folder_path = "/".join(fixed_path)
            parent = site.unrestrictedTraverse(folder_path, None)
            if parent and hasattr(parent, 'getRawLanguage'):
                self.language = parent.getRawLanguage()
            else:
                self.language = base_negotiate.language
        else:
            self.language = base_negotiate.language
