from gtts import gTTS
from io import BytesIO
from playsound import playsound

mp3_fp=BytesIO()
filename="temp.mp3"

tts = gTTS("hello jack")
print("Retreived Audio")
tts.save(filename)

print("Audio playing now ")
playsound(filename)
print("Audio end..........")
