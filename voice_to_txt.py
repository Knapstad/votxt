from pydub import  
import speech_recognition as sr
from os import path


AudioSegment.converter = "\\"
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")

sound = AudioSegment.from_mp3(AUDIO_FILE)

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

s = r.recognize_google(audio, language="no")

def process(filepath, chunksize=60000):
    #0: load mp3
    sound = AudioSegment.from_mp3(filepath)

    #1: split file into 60s chunks
    def divide_chunks(sound, chunksize):
        # looping till length l
        for i in range(0, len(sound), chunksize):
            yield sound[i:i + chunksize]
    chunks = list(divide_chunks(sound, chunksize))
    print(f"{len(chunks)} chunks of {chunksize/1000}s each")

    r = sr.Recognizer()
    #2: per chunk, save to wav, then read and run through recognize_google()
    string_index = {}
    for index,chunk in enumerate(chunks):
        #TODO io.BytesIO()
        chunk.export('test.wav', format='wav')
        with sr.AudioFile('test.wav') as source:
            audio = r.record(source)
        #s = r.recognize_google(audio, language="en-US") #, key=API_KEY) --- my key results in broken pipe
        
        print(s)
        string_index[index] = s
        break
    return string_index
