#we are using PJSUA Module- which has PJSIP Stack. (pjsip.org)
#the client is conatins all the predefined classes present in PJSIP stack
#Account config class is modified according our use.
#this code contains registration and call establishment code.


import sys

import pjsua as pj

import threading

# logging information
def callback_log(level, str, len):

    print str,



# it fetches the events from the call.

class Mycallcallback(pj.callcallback):

    def __init__(self, call=None):

        pj.CallCallback.__init__(self, call)


# status message for the call


    def on_state(self):

        print "Call is ", self.call.info().state_text,

        print "last code =", self.call.info().last_code,

        print "(" + self.call.info().last_reason + ")"



    # media change info fetched here

    def on_media_state(self):

        global lib

        if self.call.info().media_state == pj.MediaState.ACTIVE:



            calling_slot = self.call.info().configure_slot

            lib.configure_conn(calling_slot, 0)

            lib.configure_conn(0, calling_slot)

            print "Hi there, I can talk!"



class Account_cbk(pj.AccountCallback):

    def __init__(self, account):

        pj.AccountCallback.__init__(self, account)


# how to run

if len(sys.argv) != 2:

    print 'Usage: <prog_name>.py <dst-URI>'

    sys.exit(1)



try:

    # lib establishment

    library = pj.Lib()



    # instatiate the lib and associated classes for sip call

    library.init(log_cfg = pj.LogConfig(step=3, callback=callback_log))

    transport_config = pj.TransportConfig()

    transport_config.port = 5060

    transport_config.bound_addr = "192.168.16.142"

    transport = lib.create_transport(pj.TransportType.UDP,transport_config)

    # lib start

    lib.start()

    lib.set_null_snd_dev()


    #Account setup


    account_config = pj.AccountConfig(domain = '192.168.16.138', username = '2010', password = 'root', display = 'Hrishi', registrar = 'sip:192.168.16.138:5060', proxy = 'sip:192.168.16.138:5060')

    account_config.id = "sip:2010"

    account_config.reg_uri = "sip:192.168.16.138:5060"


    account_cb = Account_cb(account)

    account.set_callback(account_cb)



    print '\n'

    print 'Registration successful, status=', account.info().reg_status, '(' + account.info().reg_reason + ')'


    Makecall = account.make_call(sys.argv[1], MyCallCallback())


    print 'to exit press enter'

    input = sys.stdin.readline().rstrip('\r\n')



    # destroying the lib after call completed

    lib.destroy()

    lib = None


# error check
except pj.Error, e:

    print 'Exception: ' + str(e)

    lib.destroy()

    lib = None

    sys.exit(1)
