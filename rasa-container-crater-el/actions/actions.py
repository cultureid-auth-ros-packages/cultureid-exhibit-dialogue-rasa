# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from os import remove
from typing import Any, Text, Dict, List, Union
from urllib import response
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ReminderScheduled, FollowupAction, UserUttered
from rasa_sdk.forms import FormValidationAction, ValidationAction
from rasa_sdk.types import DomainDict


import random
import numpy as np


class ActivateExhibitForm(Action):
    def name(self) -> Text:
        return "action_iterate_form_exhibit"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        print("action_iterate_form_exhibit")

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        slot_iterate_count = tracker.slots.get("slot_iterate_count")

        slot_iterate_count = slot_iterate_count + 1

        if len(slot_list_exhibit_utters)==0:

            flag_exhibit_utters = "0"
            dispatcher.utter_message(response="utter_exhibit_finish")

            dispatcher.utter_message(response="utter_end_of_tour")
            dispatcher.utter_message(response="utter_say_goodbye")
            return [AllSlotsReset(), Restarted()]

            # return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_iterate_count", slot_iterate_count), SlotSet("slot_interested",None),  FollowupAction("form_exhibit")]

        # elif (slot_iterate_count >= 4) and (np.mod(slot_iterate_count,2)==0):
        elif (slot_iterate_count == 5):

            flag_exhibit_utters = "1"
            dispatcher.utter_message(response="utter_exhibit_enough")

            return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_iterate_count", slot_iterate_count), SlotSet("slot_interested",None),  FollowupAction("form_exhibit")]

        else:

            flag_exhibit_utters = "2"

            return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_iterate_count", slot_iterate_count), FollowupAction("action_listen")]



class AlreadyTold(Action):
    def name(self) -> Text:
        return "action_say_already_told"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        
        if (len(exhibit_utters)!=0):

            i = random.randint(0, len(exhibit_utters)-1 )	
            selected_utter=exhibit_utters[i]
            exhibit_utters.pop(i)

            slot_name = tracker.slots.get("slot_name")

            if slot_name == None:
                slot_name = ""

            dispatcher.utter_message(response="utter_say_already_told", name = slot_name)
            dispatcher.utter_message(response=selected_utter)
        
            return [SlotSet("slot_list_exhibit_utters",exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class Sayburial(Action):
    def name(self) -> Text:
        return "action_say_burial"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
    
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_burial")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            
        
        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]



class Saydepiction(Action):
    def name(self) -> Text:
        return "action_say_depiction"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
    
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_depiction")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            
        
        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]



class SayImportance(Action):
    def name(self) -> Text:
        return "action_say_importance"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_importance")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class SayMaking(Action):
    def name(self) -> Text:
        return "action_say_making"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_making")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            

        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]





class Sayfinding(Action):
    def name(self) -> Text:
        return "action_say_finding"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_finding")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]



class Saybelonging(Action):
    def name(self) -> Text:
        return "action_say_belonging"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter)  
        
            dispatcher.utter_message(response="utter_say_belonging")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            

        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class Sayuse(Action):
    def name(self) -> Text:
        return "action_say_use"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_use")
        else: 
        
            return [FollowupAction("action_say_already_told")]
            


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class SayCreation(Action):
    def name(self) -> Text:
        return "action_say_creation"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_creation")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class Saymaterial(Action):
    def name(self) -> Text:
        return "action_say_material"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter)
        
            dispatcher.utter_message(response="utter_say_material")

        else: 
        
            return [FollowupAction("action_say_already_told")]
            


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]





class Introduce(Action):
    def name(self) -> Text:
        return "action_introduce"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        dispatcher.utter_message(response="utter_introduce")
        return []


class SayBye(Action):
    def name(self) -> Text:
        return "action_say_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_name = tracker.slots.get("slot_name")

        if slot_name == None:
            slot_name = ""

        dispatcher.utter_message(response="utter_say_goodbye", name = slot_name)
        return [AllSlotsReset(),Restarted()]




class SayThanks(Action):
    def name(self) -> Text:
        return "action_say_thanks"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        dispatcher.utter_message(response="utter_say_thanks")
        return []

class SayThanksDeny(Action):
    def name(self) -> Text:
        return "action_say_thanks_deny"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        print('thanks')
        dispatcher.utter_message(response="utter_say_thanks_deny")
        # return [FollowupAction("action_reset_slots")]
        return []



class ValidateForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_user"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:


        updated_slots = domain_slots.copy()

        if tracker.slots.get("slot_adult") == True:
            updated_slots.remove("slot_favorite_subject")

        
        filled_slots = [x for x in updated_slots if tracker.slots.get(x)!=None] 
        

        if len(filled_slots)==len(updated_slots): 
            updated_slots=[] 


        return updated_slots




    def validate_slot_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print("validate_slot_name")

        if slot_value == None:
            slot_value = ""

        if slot_value=="":
            dispatcher.utter_message(response="utter_say_nice_to_meet_you", name = slot_value)

        else:
            if slot_value[-1]=="ς":
                slot_value = slot_value[:-1]
 
            if (slot_value[-1]=="ο"):
                
                list_slot_value = list(slot_value)
                list_slot_value[-1] = "ε"
                slot_value = ''.join(list_slot_value)
               
            elif (slot_value[-1]=="ό"):

                list_slot_value = list(slot_value)
                list_slot_value[-1] = "έ"
                slot_value = ''.join(list_slot_value)
                

            dispatcher.utter_message(response="utter_say_nice_to_meet_you", name = slot_value)

        return {"slot_name": slot_value}


    def validate_slot_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        print("validate_slot_age")
        
        

        

        try: 
            slot_value = int(slot_value)
        except:
            print("No number provided")
            dispatcher.utter_message(response="utter_say_my_age")
            return {"slot_age": 30, "slot_adult":True}

        if (slot_value <= 2):
            dispatcher.utter_message(response="utter_wrong_age", name="μείον χίλια")
        elif (slot_value >= 100):    
            dispatcher.utter_message(response="utter_wrong_age", name="χίλια")


        dispatcher.utter_message(response="utter_say_my_age")

        if slot_value == 3:
            grade="πηγαίνεις παιδικό σταθμό"
        elif slot_value == 4:
            grade="πηγαίνεις μικρά νήπια"
        elif slot_value == 5:
            grade="πηγαίνεις μεγάλα νήπια"
        elif slot_value == 6:
            grade="πηγαίνεις πρώτη δημοτικού"
        elif slot_value == 7:
            grade="πηγαίνεις δευτέρα δημοτικού"
        elif slot_value == 8:
            grade="πηγαίνεις τρίτη δημοτικού"
        elif slot_value == 9:
            grade="πηγαίνεις τετάρτη δημοτικού"
        elif slot_value == 10:
            grade="πηγαίνεις πέπμτη δημοτικού"
        elif slot_value == 11:
            grade="πηγαίνεις έκτη δημοτικού"
        elif slot_value == 12:
            grade="πηγαίνεις πρώτη γυμνασίου"
        elif slot_value == 13:
            grade="πηγαίνεις δευτέρα γυμνασίου"
        elif slot_value == 14:
            grade="πηγαίνεις τρίτη γυμνασίου"
        elif slot_value == 15:
            grade="πηγαίνεις πρώτη λυκείου"
        elif slot_value == 16:
            grade="πηγαίνεις δευτέρα λυκείου"
        elif slot_value == 17:
            grade="πηγαίνεις τρίτη λυκείου"
        elif slot_value>=18:
            grade="έχεις τελειώσει το σχολείο"

        if  (slot_value>=3):
            dispatcher.utter_message(response="utter_guess_class", grade=grade, age=str(slot_value))
       
        if (slot_value<18):               
            
            return {"slot_age": slot_value, "slot_adult":False}
        else:               
            
            return {"slot_age": slot_value, "slot_adult": True}



    def validate_slot_occupation(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:

            print("validate_slot_occupation")
           
            return {"slot_occupation": slot_value}




    def validate_slot_favorite_subject(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:

            print("validate_slot_favorite_subject")
            

            return {"slot_favorite_subject": slot_value}








class ActionSetSlotName(Action):
    def name(self):
        return "action_set_slot_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_name")
        
        
        

        if tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            latest_message = tracker.latest_message
            intent = latest_message["intent"].get("name")
            entities = latest_message["entities"]
            name_entities = [x.get("value") for x in entities if (x.get("entity")== "entity_name") or (x.get("entity")== "PERSON") ]

            if requested_slot=="slot_name":
                
                if (len(name_entities)>=1):
                    return [SlotSet("slot_name", name_entities[0])]


                rule_intents = tracker.slots.get("slot_rule_intents")
                if intent in rule_intents:
                    return []

                kratiras_intents = tracker.slots.get("slot_kratiras_intents")
                if intent in kratiras_intents:
                    return []
                if (intent=="intent_exhibit") or (intent=="intent_ask_current_exhibit"):
                    return []

                
                # text = latest_message["text"]
                return [SlotSet("slot_name", "")]


        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")

        if intent == "intent_name":

            entities = latest_message["entities"]
            name_entities = [x.get("value") for x in entities if (x.get("entity")== "entity_name") or (x.get("entity")== "PERSON") ]

            if (len(name_entities)>=1):
                return [SlotSet("slot_name", name_entities[0])]
        




class ActionSetSlotAge(Action):

    def name(self):
        return "action_set_slot_age"

    def run(self, dispatcher, tracker, domain):
        print("action_set_slot_age")
        
        


        if tracker.active_loop.get("name")=="form_user":
        
            requested_slot = tracker.slots.get("requested_slot")

            if requested_slot=="slot_age":

                latest_message = tracker.latest_message
                intent = latest_message["intent"].get("name")
                rule_intents = tracker.slots.get("slot_rule_intents")

                if intent in rule_intents:
                    return []

                kratiras_intents = tracker.slots.get("slot_kratiras_intents")
                if intent in kratiras_intents:
                    return []
                if (intent=="intent_exhibit") or (intent=="intent_ask_current_exhibit"):
                    return []


                if intent == "intent_age":

                    entities = latest_message["entities"]
                    age_entities = [x.get("value") for x in entities if x.get("entity")== "entity_age" ]
                    
                    if len(age_entities)>=1: 
                        return [SlotSet("slot_age", age_entities[0])]
                    else:
                        return [SlotSet("slot_age", "noentity")]
                
                elif intent == "intent_name":

                    return []

                else: 

                    text = latest_message["text"]
                    return [SlotSet("slot_age", "noentity")]




class ActionSetSlotOccupation(Action):
    def name(self):
        return "action_set_slot_occupation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_occupation")
                
        

        if tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot=="slot_occupation":
        
                latest_message = tracker.latest_message
                intent = latest_message["intent"].get("name")
                
                rule_intents = tracker.slots.get("slot_rule_intents")
                # rule_intents.remove("intent_exhibit")

                if intent in rule_intents:
                    return []

                # kratiras_intents = tracker.slots.get("slot_kratiras_intents")
                # if intent in kratiras_intents:
                #     return []

                text = latest_message["text"]
                return [SlotSet("slot_occupation", text)]







class ActionSetSlotFavoriteSubject(Action):
    def name(self):
        return "action_set_slot_favorite_subject"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_favorite_subject")
        

        if tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot=="slot_favorite_subject":
                
                latest_message = tracker.latest_message
                intent = latest_message["intent"].get("name")
                
                rule_intents = tracker.slots.get("slot_rule_intents")
                # rule_intents.remove("intent_exhibit")


                if intent in rule_intents:
                    return [] 

                # kratiras_intents = tracker.slots.get("slot_kratiras_intents")
                # if intent in kratiras_intents:
                #     return []


                text = latest_message["text"]
                return [SlotSet("slot_favorite_subject", text)]

               
















class ValidateFormExhibit(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_exhibit"


    def validate_slot_interested(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("validate_interested")

        proper_values = [True, False]
  
        if slot_value in proper_values:
            
            return {"slot_interested": slot_value}
       
        else:
            # dispatcher.utter_message(text=f"Επαναλαμβάνω")
            return {"slot_interested": None}







class ActionSetSlotInterested(Action):
    def name(self):
        return "action_set_slot_interested"

    def run(self, dispatcher, tracker, domain):

        print("set_interested")


        requested_slot = tracker.slots.get("requested_slot")
        tracker_name = tracker.active_loop.get("name")       
        flag_form = ( (tracker_name=="form_exhibit") and (requested_slot=="slot_interested"))
        
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        rule_intents = tracker.slots.get("slot_rule_intents")


        false_intents = ["intent_stop_tour", "intent_deny", "intent_goodbye"]
        true_intents = ["intent_affirm", "intent_whatever", "intent_exhibit"]
        kratiras_intents = tracker.slots.get("slot_kratiras_intents")
                
        if  flag_form:
            
            if (intent in true_intents) or (intent in kratiras_intents):
            
                return [SlotSet("slot_interested", True)]

            elif (intent in false_intents):
                
                return [SlotSet("slot_interested", False)]

            elif intent in rule_intents:
                return []
            
            else:
                
                return [SlotSet("slot_interested", True)]



        




        





class ResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_name = tracker.slots.get("slot_name")

        # dispatcher.utter_message(response="utter_reset_slots")
        
        dispatcher.utter_message(response="utter_say_goodbye", name = slot_name)

        return [AllSlotsReset(),Restarted()]







class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        
        print("action_fallback")
        fallback_count = tracker.slots.get("slot_fallback_count")
        fallback_count = fallback_count + 1
        
        print("nlu_fallback")
        print(fallback_count)

        events = tracker.events
        bot_events = [x for x in events if x["event"]=="bot"]
            
        

        if fallback_count==1: #simainei oti prwti fora den katalave
            
            dispatcher.utter_message(response="utter_fallback_1st_time") #+ na ξανακανει την ερωτηση
            # dispatcher.utter_message(response = "utter_say_capabilities")

            return [UserUtteranceReverted(), SlotSet("slot_fallback_count", fallback_count), FollowupAction("action_say_capabilities")]

        elif fallback_count==2: #simainei oti deuteri fora den katalave
            
            dispatcher.utter_message(response="utter_fallback_2nd_time") #+ na ξανακανει την ερωτηση
           
            exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")           

            if (len(exhibit_utters)!=0):

                i = random.randint(0, len(exhibit_utters)-1 )	
                selected_utter=exhibit_utters[i]
                exhibit_utters.pop(i)

                dispatcher.utter_message(response = "utter_say_following")
                dispatcher.utter_message(response=selected_utter)
            
                return [UserUtteranceReverted(),  SlotSet("slot_list_exhibit_utters",exhibit_utters), SlotSet("slot_fallback_count", fallback_count), FollowupAction("action_iterate_form_exhibit")]

            else:

                # dispatcher.utter_message(response="utter_exhibit_finish")
                slot_name = tracker.slots.get("slot_name")
                
                if slot_name == None:
                    slot_name = ""

                dispatcher.utter_message(response="utter_end_of_tour")
                dispatcher.utter_message(response="utter_say_goodbye", name = slot_name)
                
                return [AllSlotsReset(),Restarted()]


        elif fallback_count==3:

            slot_name = tracker.slots.get("slot_name")

            if slot_name == None:
                slot_name = ""

            dispatcher.utter_message(response="utter_fallback_3rd_time")
            dispatcher.utter_message(response="utter_say_goodbye", name = slot_name)

            return [AllSlotsReset(),Restarted()]





class ActionSetSlotFallback(Action):
    def name(self):
        return "action_set_slot_fallback_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        # latest_message = tracker.latest_message
        # intent = latest_message["intent"].get("name")
        

        # if intent != "nlu_fallback":

        #     fallback_count  = 0
        #     # print("not_nlu_fallback")
        #     # print(fallback_count)

        
        #     return [SlotSet("slot_fallback_count", fallback_count)]
        
        return []









class ActionReactToSilence(Action):
    

    def name(self) -> Text:
        return "action_react_to_silence"


    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        print("react_to_silence")
        silence_count = tracker.slots.get("slot_silence_count")
        silence_count = silence_count + 1

        requested_slot = tracker.slots.get("requested_slot")
        slot_exhibit = tracker.slots.get("slot_exhibit")
        
        slot_name = tracker.slots.get("slot_name")
        if slot_name == None:
            slot_name = ""

        if (requested_slot!=None):

            if (silence_count<3):
                # dispatcher.utter_message(response="utter_react_to_silence_1st", name=slot_name)

                events = tracker.events
                bot_events = [x for x in events if x["event"]=="bot"]
                bot_event = bot_events[-1]
                bot_response = bot_event["text"]
                dispatcher.utter_message(response="utter_repeat", name = slot_name)

                dispatcher.utter_message(text=bot_response)

                return [UserUtteranceReverted(),  SlotSet("slot_silence_count",silence_count)]  
            
            elif silence_count>=3:
                dispatcher.utter_message(response="utter_react_to_silence_final", name=slot_name)
                return [AllSlotsReset(),Restarted()]

        
        else:

            exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")           

            if (len(exhibit_utters)!=0) and (silence_count==1):
                
                
                # dispatcher.utter_message(response="utter_react_to_silence_1st", name=slot_name)

                dispatcher.utter_message(response="utter_silent_user_1")
                # dispatcher.utter_message(response="utter_say_capabilities")
                
                return [UserUtteranceReverted(),  SlotSet("slot_silence_count",silence_count),FollowupAction("action_say_capabilities")]
            

            elif (len(exhibit_utters)!=0) and (silence_count==2):

                # dispatcher.utter_message(response="utter_react_to_silence_1st", name=slot_name)

                dispatcher.utter_message(response="utter_silent_user_2", name=slot_name)
                
                i = random.randint(0, len(exhibit_utters)-1 )	
                selected_utter=exhibit_utters[i]
                exhibit_utters.pop(i)
                                
                dispatcher.utter_message(response=selected_utter)

                slot_iterate_count = tracker.slots.get("slot_iterate_count")  

                # if not ((slot_iterate_count + 1 >= 4) and (np.mod(slot_iterate_count + 1,2)==0)):
                if (not (slot_iterate_count + 1 == 5)) and (len(exhibit_utters)!=0):

                    # dispatcher.utter_message(response="utter_say_capabilities") 
                    return [UserUtteranceReverted(),  SlotSet("slot_silence_count",silence_count), SlotSet("slot_list_exhibit_utters",exhibit_utters), FollowupAction("action_say_capabilities")]


                return [UserUtteranceReverted(),  SlotSet("slot_silence_count",silence_count), SlotSet("slot_list_exhibit_utters",exhibit_utters), FollowupAction("action_iterate_form_exhibit")]
            
            elif (len(exhibit_utters)!=0) and (silence_count==3):
                dispatcher.utter_message(response="utter_react_to_silence_final", name=slot_name)
                return [AllSlotsReset(),Restarted()]

            elif (len(exhibit_utters)==0):

                dispatcher.utter_message(response="utter_end_of_tour")
                dispatcher.utter_message(response="utter_say_goodbye", name=slot_name)

                return [AllSlotsReset(), Restarted()]
            







class ActionSetSlotSilence(Action):
    def name(self):
        return "action_set_slot_silence_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_silence_count")
        # latest_message = tracker.latest_message
        # intent = latest_message["intent"].get("name")
        # silence_count = tracker.slots.get("slot_silence_count")

        # if intent != "intent_silence":
        #     silence_count  = 0

        #     return [SlotSet("slot_silence_count", silence_count)]

        return []
        

        
        




class ActionSayCurrentExhibit(Action):
    def name(self):
        return "action_say_current_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        dispatcher.utter_message(response="utter_say_current_exhibit")        
        return []



class ActionSayCapabilites(Action):
    def name(self):
        return "action_say_capabilities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_capabilities = tracker.slots.get("slot_capabilities")

        capability_sayings = exhibit_capabilities[0]
        capability_utters = exhibit_capabilities[1]

        indicies = []
        for utter in exhibit_utters:
            for i, capability_utter in enumerate(capability_utters):
                if utter in capability_utter:
                    indicies.append(i)
                    
        if len(indicies):
            random_choice = random.choice(indicies)	
        else:
            random_choice = random.randint(0,len(capability_sayings)-1)

        selected_capability = capability_sayings[random_choice]

        dispatcher.utter_message(text=selected_capability)   

        return [FollowupAction("action_listen")]





class ActionExhibitSelected(Action):
    def name(self):
        return "action_introduce_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_introduce_exhibit")
        dispatcher.utter_message(response="utter_introduce_exhibit") 

        return []


class ActionSubmitFormUser(Action):
    def name(self):
        return "action_submit_form_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        print("action_submit_form_user")
        dispatcher.utter_message(response="utter_introduction_to_tour")

        return []


class ActionSubmitFormExhibit(Action):
    def name(self):
        return "action_submit_form_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_submit_form_exhibit")
        slot_interested = tracker.slots.get("slot_interested")
        slot_name = tracker.slots.get("slot_name")
        if slot_name == None:
            slot_name = ""

        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name") 
        kratiras_intents = tracker.slots.get("slot_kratiras_intents")
        flag_exhibit_utters = tracker.slots.get("flag_exhibit_utters")
        
        if (intent in kratiras_intents) and (flag_exhibit_utters!="2"): #an rwtise kati autos kai den eimast stin prwti fora
        
            action = "action_say_" + intent[7:]     
            return [SlotSet("slot_name",slot_name), FollowupAction(action)]


        flag_exhibit_utters = tracker.slots.get("flag_exhibit_utters")

        if (slot_interested == False):

            
            if flag_exhibit_utters != "2":
                dispatcher.utter_message(response="utter_end_of_tour")

            dispatcher.utter_message(response="utter_say_goodbye", name = slot_name)
            return [AllSlotsReset(), Restarted()]

        elif (slot_interested == True):
            
            exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")

            if (flag_exhibit_utters=="0"): #an einai 0 simainei oti den exoun minei alla opote tou leei rwta me esi

                dispatcher.utter_message(response="utter_say_ask_me", name=slot_name)            
                return [SlotSet("slot_name",slot_name)]

            elif (flag_exhibit_utters=="1"): # an einai 1 simainei ton rwtise an thelei na sinexisei opote leei stin tixi kati
                
                i = random.randint(0, len(exhibit_utters)-1 )	
                selected_utter=exhibit_utters[i]
                exhibit_utters.pop(i)

                dispatcher.utter_message(response = "utter_exhibit_not_changed", name=slot_name)
                dispatcher.utter_message(response=selected_utter)
            
                return [SlotSet("slot_name",slot_name), SlotSet("slot_list_exhibit_utters", exhibit_utters), FollowupAction("action_iterate_form_exhibit")]


            else: #an einai dio simainei rwtise prwti fora opote tha pei capabilities

                dispatcher.utter_message(response="utter_introduce_exhibit")

                # dispatcher.utter_message(response="utter_say_capabilities")            
                return [SlotSet("slot_name",slot_name), FollowupAction("action_say_capabilities")]


        


class ActionRepeat(Action):
    

    def name(self) -> Text:
        return "action_repeat"


    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:


        events = tracker.events
        bot_events = [x for x in events if x["event"]=="bot"]
        bot_event = bot_events[-1]
        bot_response = bot_event["text"]

        # dispatcher.utter_message(response="utter_repeat")
        dispatcher.utter_message(text=bot_response)

        return [UserUtteranceReverted()]




class ActionSetListUtters(Action):
    def name(self):
        return "action_set_slot_list_exhibit_utters"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        return []   




class ActionStopTour(Action):
    def name(self):
        return "action_stop_tour"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        slot_name = tracker.slots.get("slot_name")

        dispatcher.utter_message(response = "utter_say_goodbye", name = slot_name)
        return [AllSlotsReset(),Restarted()] 


class ActionSetFlagExhibitUtters(Action):
    def name(self):
        return "action_set_flag_exhibit_utters"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return [] 
        

class ActionSetSlotAdult(Action):
    def name(self):
        return "action_set_slot_adult"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return [] 


class ActionSetSlotRuleIntents(Action):
    def name(self):
        return "action_set_slot_rule_intents"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return [] 


class ActionSetSlotkratirasIntents(Action):
    def name(self):
        return "action_set_slot_kratiras_intents"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return []


class ActionSetSlotIterate(Action):
    def name(self):
        return "action_set_slot_iterate_count"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return []


class ActionSetSlotCapabilities(Action):
    def name(self):
        return "action_set_slot_capabilities"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return []


class ActionValidateAction(Action):
    def name(self):
        return "action_validate_intents"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("validate_intents")

        kratiras_intents = tracker.slots.get("slot_kratiras_intents")

        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name") 

        # if (intent in kratiras_intents) or (intent=="intent_exhibit") or (intent=="intent_affirm"):

        slot_interested = tracker.slots.get("slot_interested")
        
        if  (slot_interested==None): 
                        
            bot_response = "Στον ελεύθερό μου χρόνο στέκομαι εδώ και δίνω πληροφορίες για τον Κρατήρα του Δερβενίου στους επισκέπτες μας."
            dispatcher.utter_message(text=bot_response)
            return [FollowupAction("form_exhibit")]               
        else:

            return []


class ActionSayExhibit(Action):
    def name(self):
        return "action_say_exhibit"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_say_exhibit")

        exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        
        if len(exhibit_utters):

            i = random.randint(0, len(exhibit_utters)-1 )	
            selected_utter=exhibit_utters[i]
            exhibit_utters.pop(i)
                            
            dispatcher.utter_message(response=selected_utter)

            return [SlotSet("slot_list_exhibit_utters",exhibit_utters), FollowupAction("action_iterate_form_exhibit")]
        
        else:
            
            slot_name = tracker.slots.get("slot_name")
            if slot_name == None:
                slot_name = ""

            dispatcher.utter_message(response="utter_end_of_tour")
            dispatcher.utter_message(response="utter_say_goodbye", name=slot_name)

            return [AllSlotsReset(),Restarted()]
        
        