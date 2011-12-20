#!/usr/bin/env python
from __future__ import with_statement

from HTMLElement import HTMLElement
from attr_property import attr_property
from text_property import text_property

class HTMLOptionElement(HTMLElement):
    def __init__(self, doc, tag):
        HTMLElement.__init__(self, doc, tag)

    @property
    def form(self):
        raise NotImplementedError()

    defaultSelected = attr_property("selected", bool)
    text            = text_property(readonly = True)
    index           = attr_property("index", long, readonly = True)
    disabled        = attr_property("disabled", bool)
    label           = attr_property("label")
    selected        = False
    value           = attr_property("value")

