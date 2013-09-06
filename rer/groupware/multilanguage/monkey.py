# -*- coding: utf-8 -*-
from Products.Archetypes import config
from Products.CMFCore.utils import getToolByName


def gpwDefaultLanguage(self):
    """Retrieve the default language"""
    parent = self.getFolderWhenPortalFactory()
    if hasattr(parent, 'getRawLanguage') and parent.getRawLanguage():
        return parent.getRawLanguage()
    tool = getToolByName(self, 'portal_languages', None)
    if tool is not None:
        return tool.getDefaultLanguage()
    return config.LANGUAGE_DEFAULT
