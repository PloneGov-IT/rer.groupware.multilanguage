# -*- coding: utf-8 -*-
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender, IOrderableSchemaExtender
from Products.Archetypes.atapi import StringField
from Products.Archetypes.Widget import LanguageWidget
from Products.ATContentTypes.interface.interfaces import IATContentType
from Products.Archetypes import PloneMessageFactory as _
from rer.groupware.multilanguage.interfaces import IRERGroupwareMultilanguageLayer
from rer.groupware.room.interfaces import IGroupRoom
from zope.component import adapts
from zope.interface import implements


class GroupwareStringField(ExtensionField, StringField):
    """Extension field for arguments"""


class GroupwareLanguageExtender(object):
    """
    Re-define language field and use a custom default method for all Content types
    """
    adapts(IATContentType)
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    layer = IRERGroupwareMultilanguageLayer

    fields = [GroupwareStringField(
                  'language',
                  accessor="Language",
                  schemata="categorization",
                  default_method='gpwDefaultLanguage',
                  vocabulary_factory='plone.app.vocabularies.SupportedContentLanguages',
                  widget=LanguageWidget(
                      label=_(u'label_language', default=u'Language'),
                      format="select",
                      ),
              ),
            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
            return original


class GroupwareRoomLanguageExtender(object):
    """
    For groupware rooms, move language field in default schemata
    """
    adapts(IGroupRoom)
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    layer = IRERGroupwareMultilanguageLayer

    fields = [GroupwareStringField(
                  'language',
                  accessor="Language",
                  schemata="default",
                  default_method='gpwDefaultLanguage',
                  vocabulary_factory='plone.app.vocabularies.SupportedContentLanguages',
                  widget=LanguageWidget(
                      label=_(u'label_language', default=u'Language'),
                      format="select",
                      ),
              ),
            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
            return original
