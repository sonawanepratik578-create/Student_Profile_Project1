from gtts import gTTS
from playsound import playsound
import os

lyrics = """पंखा चालू केल्यावर हवा येते, पंखा चालू केल्यावर हवा येते माझ्या भावा, आणि तू सोबत नसल्यावर तुझी आठवण येते माझ्या भावा. भुसावळ शहर me."
"""



tts = gTTS(text=lyrics, lang='hi')
tts.save("song.mp3")

playsound("song.mp3")
os.remove("song.mp3")