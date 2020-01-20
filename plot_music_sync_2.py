# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 06:50:39 2019

@author: deser
"""

from __future__ import print_function
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import librosa
import librosa.display

a_1 = 'output2.wav'
a_2 = 'transformed_audio.wav'

x_1, fs = librosa.load(a_1)
x_2, fs = librosa.load(a_2)


n_fft = 4410
hop_size = 2205

x_1_chroma = librosa.feature.chroma_stft(y=x_1, sr=fs, tuning=0, norm=2, 
                            hop_length=hop_size, n_fft=n_fft)
x_2_chroma = librosa.feature.chroma_stft(y=x_2, sr=fs, tuning=0, norm=2, 
                            hop_length=hop_size, n_fft=n_fft)

'''
Waveforms
'''
plt.figure(figsize=(16, 4))
librosa.display.waveplot(x_1, sr=fs)
plt.title(a_1)
plt.tight_layout()

plt.figure(figsize=(16, 4))
librosa.display.waveplot(x_2, sr=fs)
plt.title(a_2)
plt.tight_layout()

'''
Chromagrams
'''
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


D, wp = librosa.sequence.dtw(X=x_1_chroma, Y=x_2_chroma, metric='cosine')
wp_s = np.asarray(wp) * hop_size / fs

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
librosa.display.specshow(D, x_axis='time', y_axis='time',
                         cmap='gray_r', hop_length=hop_size)
imax = ax.imshow(D, cmap=plt.get_cmap('gray_r'),
                 origin='lower', interpolation='nearest', aspect='auto')
ax.plot(wp_s[:, 1], wp_s[:, 0], marker='o', color='g')
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
arrows = 60
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

slopes = []
changerates = []
for i in range(len(wp_s)-1):
    if(wp_s[i][0] == 0 and wp_s[i][1] == 0):
        slopes.append(1)
    else:
        slopes.append(wp_s[i][0]/wp_s[i][1])
    changerates.append(1/slopes[i])    
librosa.effects.split(x_2,hop_size/64)
    
file = open('changerates.txt', 'w')
for changerate in changerates:
    data = (str(changerate) + '\n')
    file.write(data)
file.close()

def get_mean_slope():
    s1=0
    for s in slopes:
        if not (s == 11):
            s1 = s1 + s
    s1 = s1/len(slopes)
    print(s1)