# Jose Rodolfo Perez 16056

# used libs
import logging

import sys
import sleekxmpp

from sleekxmpp.exceptions import IqError, IqTimeout

# variables
USER = 'josrodjr'
HOST = '@alumchat.xyz'
PASSWORD = 'pepapls'

# puerto 5222
# jid es node@server/resource > josrodjr@alumchat.xyz

class myBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        # super(myBot, self).__init__(jid, password)
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # self.add_event_handler('sign_in', self.signin)
        self.add_event_handler("session_start", self.start)

        self.add_event_handler("register", self.register)

        self.add_event_handler('message', self.message)
        self.add_event_handler('message', self.recv_message)


    def start(self):
        print("SE INGRESA ACA1")
        self.send_presence()
        # self.get_roster()
# EXPERIMENTAL
        # self.disconnect()

        try:
            self.get_roster()
        except IqError as err:
            logging.error('There was an error getting the roster')
            logging.error(err.iq['error']['condition'])
            self.disconnect()
        except IqTimeout:
            logging.error('Server is taking too long to respond')
            self.disconnect()
    
    def register(self):
        # <iq type='get' id='reg1' to='shakespeare.lit'>
        # <query xmlns='jabber:iq:register'/>
        # </iq>
        print("SE INGRESA ACA")

        # resp = sleekxmpp.BaseXMPP.make_iq(self, iquery='jabber:iq:register')
        # resp = sleekxmpp.BaseXMPP.make_iq_set(self, sub='register')


        resp = self.Iq()
        resp['type'] = 'set'
        print(resp)
        resp['register']['username'] = self.boundjid.username
        resp['register']['password'] = self.password
        resp.send(now=True)
# EXPERIMENTAL
        # self.disconnect()

    def message(self, recipient, msg):
        self.message_info = msg
        self.recipient_msg = recipient
        # self.send_message(mto=self.recipient_msg, mbody=self.message_info)
        m = self.Message()
        m['type'] = "chat"
        m['from'] = USER+HOST
        m['to'] = self.recipient_msg
        m['body'] = self.message_info
        print("sending: ", m)
        m.send()
    
    def recv_message(self, msg):
        print(msg)
        # message.reply("The good ol ree").send()
        # if msg['type'] in ('chat', 'normal'):
        #     print("%s says: %s" % (msg['from'], msg['body']))

    def dissconect(self):
        self.disconnect(wait=True)


if __name__ == '__main__':
    # hardcode the info for testing

    xmpp = myBot(USER+HOST, PASSWORD)

    if xmpp.connect(("alumchat.xyz", 5222)):
        print("CONNECTED TO SERVER")
        xmpp.start()
        xmpp.register()
        xmpp.process(block=True)
        # xmpp.disconnect()
    else:
        print("noyeet")