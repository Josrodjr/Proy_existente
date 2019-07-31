# Jose Rodolfo Perez 16056

# used libs
import logging

import sys
import sleekxmpp

from sleekxmpp.exceptions import IqError, IqTimeout

import xml.etree.ElementTree as xml

# variables
USER = 'josrodjr9'
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

        # self.add_event_handler('message', self.message)
        self.add_event_handler('message', self.recv_message)


    def start(self, event):
        print("SENDING PRESENCE")
        # SET RESPONSE TIMER LOW SO WE CAN DEBUG
        self.send_presence()
        self.get_roster()
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
    
    def register(self, iq):
        print("REGISTERING ACCOUNT")

        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            resp.send(now=True)
            logging.info("Account created for %s!" % self.boundjid)
        except IqError as e:
            logging.error("Could not register account: %s" %
                    e.iq['error']['text'])
            # We don't disconnect if the accound was already registered
            # self.disconnect()
        except IqTimeout:
            logging.error("No response from server.")
            self.disconnect()
# EXPERIMENTAL
        # self.disconnect()

    def delete_account(self):
        print("DELETING ACCOUNT")

        resp = self.Iq()
        resp['type'] = 'set'
        resp['from'] = self.boundjid.user
        resp['register'] = ' '
        resp['register']['remove'] = ' '

        try:
            resp.send(now=True)
            logging.info("Account deleted for %s!" % self.boundjid)
        except IqError as e:
            logging.error("Could not be deleted: %s" %
                    e.iq['error']['text'])
            # self.disconnect()
        except IqTimeout:
            logging.error("No response from server.")
            self.disconnect()
    # EXPERIMENTAL
            # self.disconnect()

    def message(self, recipient, msg):
        self.message_info = msg
        self.recipient_msg = recipient
        self.send_message(mto=self.recipient_msg, mbody=self.message_info)
    
    def recv_message(self, msg):
        print(str(msg['from']) + ": " + str(msg['subject']) + "\n")
        print(str(msg['body']) + "\n")

    def dissconect(self):
        self.disconnect(wait=True)


def print_menu():
    print("0: CONNECT TO SERVER")
    print("1: SEND MESSAGE")
    print("2: ELMINATE THIS ACCOUNT")
    print("3: CONTACTS")
    print("4: REGISTER USER AS FRIEND")
    print("5: JOIN GROUP CHAT")
    print("6: SET PRESENCE")
    print("7: DISCONNECT")
    print("8: SEND GRP MESSAGE")

if __name__ == '__main__':
    # hardcoded the info for testing 

    while (True):
        # print menu
        print_menu()
        print("Insert a number")
        option = input()
        try:
            # convert to int and start the switch  
            value=int(option)
            print("SELECTED OPTION: " + option)     
            
            if value == 0:
                # connect and register to server
                print("Enter a username: ")
                USER = input()
                print("Enter a password: ")
                PASSWORD = input()

                xmpp = myBot(USER+HOST, PASSWORD)

                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0004') # Data forms
                xmpp.register_plugin('xep_0066') # Out-of-band Data
                xmpp.register_plugin('xep_0077') # In-band Registration FORCED
                xmpp.register_plugin('xep_0199') # XMPP Ping
                xmpp.register_plugin('xep_0045') # Annotations

                if xmpp.connect(("alumchat.xyz", 5222)):
                    print("CONNECTED TO SERVER")
                    xmpp.process()
                    
                else:
                    print("COULD NOT CONNECT TO SERVER")

            elif value == 1:
                # send a message
                print("Para quien es el mensaje?: ")
                recipient = input()
                print("Texto del mensaje?: ")
                text = input()
                print("SENDING MESSAGE")
                xmpp.send_message(mto=recipient+HOST, mbody = text, mtype = 'chat')
            elif value == 2:
                # eliminate this account
                print("DELETING ACCOUNT")
                xmpp.delete_account()
                print("ACCOUNT DELETED")
                xmpp.disconnect()
            elif value == 3:
                # contacts
                print("SHOWING ALL CONTACTS")
                contacts = xmpp.client_roster
                print("Sus contactos son: " + "\n" + str(contacts))
            elif value == 4:
                # register user as friend
                print("Insert a username to add as friend")
                friend = input()
                print("Sending friend request")
                xmpp.send_presence(pto=friend, ptype='subscribe')
            elif value == 5:
                # join group chat
                print("Insert a room to join")
                room = input()
                print("Insert your nick")
                nick = input()
                print("Joining a chat")
                xmpp.plugin['xep_0045'].joinMUC(room, nick)
            elif value == 6:
                # set presence
                print("WORKING IN THIS IMPLEMENTATION")
                print("Insert a status")
                status = input()
                print("Changing status")
                xmpp.makePresence(pfrom=USER+HOST, pstatus=status)


                # esta malo


            elif value == 7:
                # disconnect
                print("Disconnecting")
                xmpp.disconnect()
            elif value == 8:
                # send grp messsage
                print("WORKING IN THIS IMPLEMENTATION")
            else:
                print("NOT VALID NUMBER, RETRY")

        except ValueError:
            print("INVALID TYPE, PLEASE INSERT AN INTEGER")
