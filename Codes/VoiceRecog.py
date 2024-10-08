import pyaudio
import wave
import os
import pickle
from FeatExtract import *


def recognize():
   # Voice Authentication
   FORMAT = pyaudio.paInt16
   CHANNELS = 2
   RATE = 44100
   CHUNK = 1024
   RECORD_SECONDS = 3
   FILENAME = "./test.wav"

   audio = pyaudio.PyAudio()
  
   # start Recording
   stream = audio.open(format=FORMAT, channels=CHANNELS,
                   rate=RATE, input=True,
                   frames_per_buffer=CHUNK)

   print("recording...")
   frames = []

   for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
       data = stream.read(CHUNK)
       frames.append(data)
   print("finished recording")


   # stop Recording
   stream.stop_stream()
   stream.close()
   audio.terminate()

   # saving wav file 
   waveFile = wave.open(FILENAME, 'wb')
   waveFile.setnchannels(CHANNELS)
   waveFile.setsampwidth(audio.get_sample_size(FORMAT))
   waveFile.setframerate(RATE)
   waveFile.writeframes(b''.join(frames))
   waveFile.close()

   modelpath = "D:/Johann/BE Project/Scripts/gmm_models"

   gmm_files = [os.path.join(modelpath,fname) for fname in 
               os.listdir(modelpath) if fname.endswith('.gmm')]

   models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]

   speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
               in gmm_files]
 
   #read test file
   sr,audio = read(FILENAME)
   
   # extract mfcc features
   vector = extract_features(audio,sr)
   log_likelihood = np.zeros(len(models)) 

   #checking with each model one by one
   for i in range(len(models)):
       gmm = models[i]         
       scores = np.array(gmm.score(vector))
       log_likelihood[i] = scores.sum()

   pred = np.argmax(log_likelihood)
   identity = speakers[pred]
  
   # if voice not recognized than terminate the process
   if identity == 'unknown':
           print("Not Recognized! Try again...")
           return
   
   print( "Recognized as - ", identity)

recognize()