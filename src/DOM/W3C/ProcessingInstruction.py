#!/usr/bin/env python
from __future__ import with_statement

from DOMException import DOMException
from Node import Node
from Events import *


class ProcessingInstruction(Node):
    def __init__(self, doc, target, data):
        self._target = target
        self.data    = data

    @property
    def target(self):
        return self._target

    @property
    def nodeName(self):
        return self._target

    @property
    def nodeType(self):
        return Node.PROCESSING_INSTRUCTION_NODE

    def getNodeValue(self):
        return self.data

    def setNodeValue(self, data):
        self.data = data

    nodeValue = property(getNodeValue, setNodeValue)

