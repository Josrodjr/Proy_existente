# Jose Rodolfo Perez 16056

# used libs
import sys
import sleekxmpp

# variables
USER = 'josrodjr'
HOST = '@alumchat.xyz'
PASSWORD = 'pepapls'

# puerto 5222
# jid es node@server/resource > josrodjr@alumchat.xyz

class myBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        super(myBot, self).__init__(jid, password)

        self.add_event_handler('sign_in', self.signin)
        self.add_event_handler('out_message', self.out_message)
        self.add_event_handler('message', self.message)

    def signin(self, event):
        self.send_presence()
        self.get_roster()
    

    def out_message(self, recipient, message):
        self.message_info = message
        self.recipient_msg = recipient
        self.send_message(mto=self.recipient_msg, mbody=self.message_info)

    
    def message(self, message):
        print(message)
        message.reply("The good ol ree").send()

    def dissconect(self):
        self.disconnect(wait=True)

if __name__ == '__main__':
    # hardcode the info for testing

    xmpp = myBot(USER+HOST, PASSWORD)

    if xmpp.connect(address=HOST):
        print("yeet")
        # xmpp.out_message('amiguito'+HOST, 'REEEEEEEEEEEEEEEEEEEE')
        xmpp.process()
        # xmpp.disconnect()
    else:
        print("noyeet")