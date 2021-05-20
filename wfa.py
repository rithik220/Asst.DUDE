
# Python program to 
# demonstrate creation of an
# assistant using wolf ram API
  
from dude import speak
import wolframalpha
  
# Taking input from user
question = input('Question: ')
  
# App id obtained by the above steps
app_id = 'J3KPU2-YHYVP56Y68'
  
# Instance of wolf ram alpha 
# client class
client = wolframalpha.Client(app_id)
  
# Stores the response from 
# wolf ram alpha
res = client.query(question)
  
# Includes only text from the response
answer = next(res.results).text
  
speak(answer)