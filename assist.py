import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound

class Assitant:
    startAudioText='Hello Boss'
    startAudioFileName='init.mp3'

    def __init__(self):
        if not os.path.exists(self.startAudioFileName) :
            self.get_speech(text=self.startAudioText,filename=self.startAudioFileName)
        self.playSound(filename=self.startAudioFileName)

    def get_speech(self,text,filename):
        tts= gTTS(text)
        print("Retrieved Audio")
        tts.save(filename)
    
    def playSound(self,filename):
        playsound(filename)

def recognize_speech(recognizer, audio):
    try:
        response=recognizer.recognize_houndify(audio,client_id="dorLHNUz-YldWjZ3ZCZZLQ==",client_key="jVUWQrd7Qn6h0T16nKi-1SPZMQLNWu3ZJHI9LjSkmk_Hp6n5JPiQGAxcjGsdm5_hpTAzrJWVclHdZ8vPoAwJVA==")
        print('Response: {}'.format(response))
    except sr.RequestError:
        print("Service unreachable........")
    except sr.UnknownValueError:
        # Speech WTF    
        print("Speech Unrecognizable......")

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
ai = Assitant()

try:
    while True:

        # Get Speech 
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Listening..........")
            temp = r.listen(source)
            print("Heard you.......")
            recognize_speech(recognizer=r,audio=temp)

        # Reply 
except KeyboardInterrupt:
    print("Exiting....")
    pass




