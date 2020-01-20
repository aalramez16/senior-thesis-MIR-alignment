# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:49:25 2019

@author: Ali Al-Ramezi
"""

from __future__ import print_function
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import IPython.display as ipd


import librosa
import librosa.display
import soundfile as sf


#plt.figure(figsize=(14, 5))
#librosa.display.waveplot(audio, sr=sr)


x = ipd.Audio(r'c:/users/deser/documents/school/fa19/490x/k279-2.wav')
x

hop_size = 2205
audio,sr = librosa.load(r'c:/users/deser/documents/school/fa19/490x/k279-2.wav')
split_audio = librosa.effects.split(audio,hop_size/64)
len(split_audio)


cr_file = open(r'c:/users/deser/documents/school/fa19/490x/changerates.txt','r')

cr_txt = cr_file.read()

cr = cr_txt.split()


#rate_bucket = []
b_count = len(split_audio)
c_len = len(cr)
values = []
#print(c_len)
for i in range(0,b_count):
    #print(str(i) + ":\t" + str(cr[i*int(c_len/(b_count))]) + "\t" + str(split_audio[i]))
    values.append(cr[i*int((c_len/(b_count))/2)])

#print(len(cr))

rate_avg = []


new_audio = []
for i in range(len(split_audio)):
    for j in range(split_audio[i][0], split_audio[i][1]):
        if (j) % 1 == 0:
                new_audio.append(audio[j])
            #print(cr[i])
        

new_audio = np.asarray(new_audio)
type(new_audio)


fnames = []
samplerates = []
reloaded_segments = []
restitched_audio = []

for i in range(b_count): 
    audio_segment = []
    for j in range(split_audio[i][0], split_audio[i][1]):
        audio_segment.append(audio[j])
                                                     
    fname = 'c:/users/deser/documents/school/fa19/490x/snippet_dump/snip_' + str(i) + '.wav'
    open(fname, 'a').close()
    sf.write(fname,new_audio,sr)
    fnames.append(fname)
    new_sr=sr*float(values[i])
    
    sf.write(fnames[i], audio_segment, int(new_sr))
    reloaded_segments.append(librosa.load(fname)[0])
    samplerates.append(librosa.load(fname)[1])


for i in range(len(reloaded_segments)):
    for j in range(len(reloaded_segments[i])):
        restitched_audio.append(reloaded_segments[i][j])
        
len(restitched_audio)


open('c:/users/deser/documents/school/fa19/490x/transformed_audio.wav', 'a').close()
sf.write('c:/users/deser/documents/school/fa19/490x/transformed_audio.wav',restitched_audio,sr)