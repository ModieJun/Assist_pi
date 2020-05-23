# %%
import speech_recognition as sr

# %%
r=sr.Recognizer()
google= sr.AudioFile("./googleaudio.wav")

# %%
# print(sr.Microphone.list_microphone_names())

# %%
mic = sr.Microphone(device_index=1)
with mic as source:
    r.adjust_for_ambient_noise(mic)
    print("Start Speaking..........")   
    temp = r.listen(source,phrase_time_limit=2)
    print("Done Recording")


print("Requesting Recognition....")
try:
    response=r.recognize_houndify(temp,client_id="dorLHNUz-YldWjZ3ZCZZLQ==",client_key="jVUWQrd7Qn6h0T16nKi-1SPZMQLNWu3ZJHI9LjSkmk_Hp6n5JPiQGAxcjGsdm5_hpTAzrJWVclHdZ8vPoAwJVA==")
    print('Response: {}'.format(response))
except sr.RequestError:
    print("Service unreachable........")
except sr.UnknownValueError:
    # Speech WTF    
    print("Speech Unrecognizable......")
    