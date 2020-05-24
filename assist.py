import speech_recognition as sr
import os
from datetime import datetime
from gtts import gTTS
from playsound import playsound

class Assitant:
    startAudioText='Hello Boss'
    startAudioFileName='init'

    def __init__(self):
        if not os.path.exists(self.startAudioFileName+".mp3") :
            self.get_speech(text=self.startAudioText,filename=self.startAudioFileName)
        self.playSound(filename=self.startAudioFileName)

    def get_speech(self,text,filename='temp'):
        tts= gTTS(text)
        print("Retrieved Audio")
        tts.save(filename+".mp3")
    
    def playSound(self,filename='temp'):
        playsound(filename+".mp3")
    
    def get_time(self):
        now = datetime.now()
        text="The time is {}:{} {}"
        meridian=""
        if now.hour>=12:
            meridian='pm'
        else:
            meridian='am'
        
        if now.minute<10:
            minute= '0' + str(now.minute) # add 0 infront of single digit 
        else:
            minute =str(now.minute) # add minute 
        text = text.format(now.hour, minute,meridian)
        print("Debug:  " ,text)

        self.get_speech(text=text,filename="temp")
        self.playSound()



def recognize_speech(recognizer, audio):
    # return text of audio 
    try:
        print("Processing..........")
        response=recognizer.recognize_houndify(audio,client_id="dorLHNUz-YldWjZ3ZCZZLQ==",client_key="jVUWQrd7Qn6h0T16nKi-1SPZMQLNWu3ZJHI9LjSkmk_Hp6n5JPiQGAxcjGsdm5_hpTAzrJWVclHdZ8vPoAwJVA==")
        return response

    except sr.RequestError as e:
        print("Service unreachable........: \t " , e )
    except sr.UnknownValueError:
        # Speech WTF    
        print("Speech cannot be understood by the service ......")



def wakeWord(text):
    words=["hey slave","okay slave"]
    text = text.lower()

    for phrase in words:
        if phrase in text:
            # Wake word found
            return True
    # Wake word not found 
    return False

def record_audio(recognizer,mic):
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening......")
        temp=recognizer.listen(source)
    return temp



r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
ai = Assitant()


try:
    while True:

        # Get Speech
        audio = record_audio(recognizer=r,mic=mic)
        audio_text=recognize_speech(recognizer=r,audio=audio)


        if wakeWord(audio_text):
            ai.playSound(filename=ai.startAudioFileName)
        elif ("time" in audio_text):
            ai.get_time()
        else:
             ai.get_speech(text="i am listening",filename="temp")   
             ai.playSound(filename="temp")
        # Reply 

        
except KeyboardInterrupt:
    print("Exiting....")
    pass




