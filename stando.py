# used libs
import logging

import sys
import sleekxmpp

from sleekxmpp.exceptions import IqError, IqTimeout
from sleekxmpp import ElementBase

import xml.etree.ElementTree as xml

class Register(ElementBase):
    name = "message"
    namespace = "jabber:client"
    interfaces = set(('to', 'from', 'type', 'body'))