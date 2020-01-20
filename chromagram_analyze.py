# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:35:49 2019

@author: deser
"""

from __future__ import print_function

import matplotlib

import scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display

import music21
from music21 import *
import os
import numpy as np


#s = converter.parse("K279-1.krn")
#s.show()


#x, sr = librosa.load("output.wav")
#ipd.Audio(x, rate=sr)

#fmin = librosa.midi_to_hz(24)
#hop_length = 512
#C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=84, hop_length=hop_length)

#logC = librosa.amplitude_to_db(numpy.abs(C))
#plt.figure(figsize=(15, 5))
#librosa.display.specshow(logC, sr=sr, x_axis='time', y_axis='cqt_hz', fmin=fmin, cmap='inferno')

#chromagram = librosa.feature.chroma_cens(x, sr=sr, hop_length=hop_length)
#plt.figure(figsize=(15, 5))
#librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='gray')

#for i in range(len(chromagram)):
    #print(chromagram[i])
    
#Initialize Audio Files
x_1, fs = librosa.load('output2.wav')
print(x_1)
plt.figure(figsize=(16, 4))
librosa.display.waveplot(x_1, sr=fs)
plt.title('Midi Audio $X_1$')
plt.tight_layout()
print("fs1:",fs)
#x_2, fs = librosa.load('K239-1.m4a')
x_2, fs = librosa.load('k279-2.m4a')
plt.figure(figsize=(16, 4))
librosa.display.waveplot(x_2, sr=fs)
plt.title('Recorded Audio $X_2$')
plt.tight_layout()
print("fs2:",fs)
#Extract Chroma Features
n_fft = 4410
hop_size = 2205

x_1_chroma = librosa.feature.chroma_stft(y=x_1, sr=fs, tuning=0, norm=2,
                                         hop_length=hop_size, n_fft=n_fft)
x_2_chroma = librosa.feature.chroma_stft(y=x_2, sr=fs, tuning=0, norm=2,
                                         hop_length=hop_size, n_fft=n_fft)

plt.figure(figsize=(16, 8))
plt.subplot(2, 1, 1)
plt.title('Chroma Representation of $X_1$')
librosa.display.specshow(x_1_chroma, x_axis='time',
                         y_axis='chroma', cmap='gray_r', hop_length=hop_size)
plt.colorbar()
plt.subplot(2, 1, 2)
plt.title('Chroma Representation of $X_2$')
librosa.display.specshow(x_2_chroma, x_axis='time',
                         y_axis='chroma', cmap='gray_r', hop_length=hop_size)
plt.colorbar()
plt.tight_layout()

#Align Chroma Sequences
D, wp = librosa.sequence.dtw(X=x_1_chroma, Y=x_2_chroma, metric='cosine')
wp_s = np.asarray(wp) * hop_size / fs

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
librosa.display.specshow(D, x_axis='time', y_axis='time',
                         cmap='gray_r', hop_length=hop_size)
imax = ax.imshow(D, cmap=plt.get_cmap('gray_r'),
                 origin='lower', interpolation='nearest', aspect='auto')
ax.plot(wp_s[:, 1], wp_s[:, 0], marker='o', color='r')
plt.title('Warping Path on Acc. Cost Matrix $D$')
plt.colorbar()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 8))

# Plot x_1
librosa.display.waveplot(x_1, sr=fs, ax=ax1)
ax1.set(title='Midi Audio $X_1$')

# Plot x_2
librosa.display.waveplot(x_2, sr=fs, ax=ax2)
ax2.set(title='Recorded Audio $X_2$')

plt.tight_layout()

trans_figure = fig.transFigure.inverted()
lines = []
arrows = 30
points_idx = np.int16(np.round(np.linspace(0, wp.shape[0] - 1, arrows)))

# for tp1, tp2 in zip((wp[points_idx, 0]) * hop_size, (wp[points_idx, 1]) * hop_size):
for tp1, tp2 in wp[points_idx] * hop_size / fs:
    # get position on axis for a given index-pair
    coord1 = trans_figure.transform(ax1.transData.transform([tp1, 0]))
    coord2 = trans_figure.transform(ax2.transData.transform([tp2, 0]))

    # draw a line
    line = matplotlib.lines.Line2D((coord1[0], coord2[0]),
                                   (coord1[1], coord2[1]),
                                   transform=fig.transFigure,
                                   color='r')
    lines.append(line)

fig.lines = lines
plt.tight_layout()