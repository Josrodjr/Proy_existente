register(self):
        # <iq type='get' id='reg1' to='shakespeare.lit'>
        # <query xmlns='jabber:iq:register'/>
        # </iq>

        
        # resp = sleekxmpp.BaseXMPP.make_iq(self, iquery='jabber:iq:register')
        # resp = sleekxmpp.BaseXMPP.make_iq_set(self, sub='register')


        # resp = self.Iq()

        # make a xml
        # <iq to='marlowe.shakespeare.lit' type='set'>
        # <query xmlns='jabber:iq:register'>
        #     <username>juliet</username>
        #     <password>R0m30</password>
        # </query>
        # </iq>
        # root = xml.Element("query")
        username = xml.Element("username")
        username.text = 'josrodjr'
        password = xml.Element("password")
        password.text = 'pepapls'
        # root.append(username)
        # root.append(password)

        welp = sleekxmpp.stanza.Iq()        
        welp.append(username)
        welp.append(password)
        # welp.set_query('jabber:iq:register')

        welp['query']['username'] = username
        welp['query']['password'] = password

        welp['type'] = 'set'
        # welp['xmlns'] = 'jabber:iq:register'

        print(welp)

        # resp.append({'register', {'username': 'josrodjr', 'password': 'pepapls'}})
        # resp.append("<register <username= 'josrodjr'/> <password='pepapls' /> />")

        # resp['type'] = 'set'
        # resp['query xmls'] = 'jabber:iq:register'
        # print(resp)
        # resp['register']['username'] = self.boundjid.username
        # resp['register']['password'] = self.password

        # print(resp)
        # welp.send(now=True, timeout=self.response_timeout)