# Jose Rodolfo Perez 16056

# used libs
import sys
import sleekxmpp

# variables
USER = 'mencho'
HOST = '@alumchat.xyz'
PASSWORD = 'pepapls2'

# puerto 5222
# jid es node@server/resource > josrodjr@alumchat.xyz

class myBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        # super(myBot, self).__init__(jid, password)
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # self.add_event_handler('sign_in', self.signin)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler('message', self.message)
        self.add_event_handler('message', self.recv_message)

    def start(self, event):
        self.send_presence()
        self.get_roster()
    

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
        # print(message)
        # message.reply("The good ol ree").send()
        if msg['type'] in ('chat', 'normal'):
            print("%s says: %s" % (msg['from'], msg['body']))

    def dissconect(self):
        self.disconnect(wait=True)

if __name__ == '__main__':
    # hardcode the info for testing

    xmpp = myBot(USER+HOST, PASSWORD)

    if xmpp.connect(("alumchat.xyz", 5222)):
        print("CONNECTED TO SERVER")
        xmpp.message('josrodjr@alumchat.xyz', "REEEEEEEEEEEEEEEEEEEE")
        xmpp.process()
        # xmpp.disconnect()
    else:
        print("noyeet")