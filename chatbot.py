import pywhatkit


model=[None]*5
model= {'You may not know, but over 8 million tons of plastic enter the oceans every year, harming marine life and creating giant garbage patches.',
            'You may not know, but over 8 million tons of plastic enter the oceans every year, harming marine life and creating giant garbage patches.',
            'You may not know, but women make up less than 25% of the workforce in technology fields worldwide, highlighting a major gender gap in this industry'
            'You may not know, but wildfires are increasing by about 30% each year due to climate change, threatening forests, wildlife, and communities across the world.'
            'You may not know, but 9 out of 10 people worldwide breathe polluted air, which is responsible for over 7 million deaths annually'}


day = 7
def watsapp_message_bot(phone, id):
 price_str=model[0]['price']
 price = float(price_str)
 output="News for today: " + model[day%5] 
 pywhatkit.sendwhatmsg(phone, output , 15,8, 15, True, 2)
 pywhatkit.sendwhatmsg_to_group(id, output, 17, 6)
                                  #L4fK8yUKkaWLe1WM49AMqi
phone_number=input("Enter phone number")
group_id=input("enter group_id") 
watsapp_message_bot(phone_number, group_id)
