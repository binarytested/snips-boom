#!/usr/bin/env python2
from hermes_python.hermes import Hermes

globalvalue = "global"

def test_code(hermes, intent_message):
    globalvalue = "eureka"
    INTENT_FILTER = ["multip:test_end_session"]
    sentence = "continue session"
    hermes.publish_continue_session(intent_message.session_id, sentence, INTENT_FILTER)
    #print('Intent {}'.format(intent_message.intent))

    #for (slot_value, slot) in intent_message.slots.items():
    #    print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))

    #hermes.publish_end_session(intent_message.session_id, 'Ending session')
    #print("*** EUREKA ***")
    #hermes.publish_end_session(intent_message.session_id, sentence)
     
   
def test_end_session(hermes, intent_message):   
    hermes.publish_end_session(intent_message.session_id, globalvalue)

    
    
with Hermes('raspberrypi.local:1883') as h:
    h.subscribe_intent("multip:test_code", test_code).start()
