# -*- coding: utf-8 -*-
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender, IOrderableSchemaExtender
from Products.Archetypes.atapi import StringField
from Products.Archetypes.Widget import LanguageWidget
from Products.ATContentTypes.interface.interfaces import IATContentType
from Products.Archetypes import PloneMessageFactory as _
from rer.groupware.multilanguage.interfaces import IRERGroupwareMultilanguageLayer
from zope.component import adapts
from zope.interface import implements


class GroupwareStringField(ExtensionField, StringField):
    """Extension field for arguments"""


class GroupwareLanguageExtender(object):

    adapts(IATContentType)

    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    layer = IRERGroupwareMultilanguageLayer

    fields = [GroupwareStringField(
                  'language',
                  accessor="Language",
                  schemata="categorization",
                  default_method='gpwDefaultLanguage',
                  vocabulary='languages',
                  widget=LanguageWidget(
                      label=_(u'label_language', default=u'Language'),
                      ),
              ),
            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
            return original
