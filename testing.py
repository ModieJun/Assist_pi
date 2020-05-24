# %%
import speech_recognition as sr
from gtts import gTTS

# %%
r=sr.Recognizer()
google= sr.AudioFile("./googleaudio.wav")
    
# %%
# print(sr.Microphone.list_microphone_names())

# %%
mic = sr.Microphone(device_index=1)

try:
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(mic)
            print("Start Speaking..........")   
            temp = r.listen(source,phrase_time_limit=2)
            print("Done Recording")

            print("\nSample Width: \t {} \n".format(temp.sample_width))

        print("Requesting Recognition....")
        try:
            response=r.recognize_houndify(temp,client_id="dorLHNUz-YldWjZ3ZCZZLQ==",client_key="jVUWQrd7Qn6h0T16nKi-1SPZMQLNWu3ZJHI9LjSkmk_Hp6n5JPiQGAxcjGsdm5_hpTAzrJWVclHdZ8vPoAwJVA==")
            print('Response: {}'.format(response))
            
        except sr.RequestError:
            print("Service unreachable........")
        except sr.UnknownValueError:
            # Speech WTF    
            print("Speech Unrecognizable......")
except KeyboardInterrupt:
    print("Exiting....")
    pass