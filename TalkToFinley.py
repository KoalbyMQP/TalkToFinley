from dotenv import load_dotenv
from openai import OpenAI

import speech_recognition as sr

import pyttsx3
 
r = sr.Recognizer() 

# feed text to openai
load_dotenv()  # take environment variables from .env.
client = OpenAI()

# initialize TTS
engine = pyttsx3.init()
# set female voice
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

# step 1: listen for question and convert speech to text
with sr.Microphone() as src:

    # wait to adjust
    print("Adjusting for ambient noise...")
    r.adjust_for_ambient_noise(src, duration=0.2)

    print("Listening for speech")
    #listens for the user's input 
    audio2 = r.listen(src)

    print("Converting to text...")
    # Using google to recognize audio
    spokenText = r.recognize_google(audio2)

    print(spokenText)
    
# step 2: feed question to openai
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a humanoid robot named Finley, designed to assist humans with factual questions about U.S. History. Please keep your answers brief, only a few sentences maximum."},
    {"role": "user", "content": spokenText}
  ]
)

print(completion.choices[0].message.content)

# step 3: speak openai's response using TTS

engine.say(completion.choices[0].message.content)
engine.runAndWait()