# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:27:45 2019

@author: deser
"""

import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display

import music21
from music21 import *
import os
import numpy as np

s_measure_files = ['k279-2/midi/k279-2_measure_0.mid', 'k279-2/midi/k279-2_measure_1.mid', 'k279-2/midi/k279-2_measure_2.mid', 'k279-2/midi/k279-2_measure_3.mid', 'k279-2/midi/k279-2_measure_4.mid', 'k279-2/midi/k279-2_measure_5.mid', 'k279-2/midi/k279-2_measure_6.mid', 'k279-2/midi/k279-2_measure_7.mid', 'k279-2/midi/k279-2_measure_8.mid', 'k279-2/midi/k279-2_measure_9.mid', 'k279-2/midi/k279-2_measure_10.mid', 'k279-2/midi/k279-2_measure_11.mid', 'k279-2/midi/k279-2_measure_12.mid', 'k279-2/midi/k279-2_measure_13.mid', 'k279-2/midi/k279-2_measure_14.mid', 'k279-2/midi/k279-2_measure_15.mid', 'k279-2/midi/k279-2_measure_16.mid', 'k279-2/midi/k279-2_measure_17.mid', 'k279-2/midi/k279-2_measure_18.mid', 'k279-2/midi/k279-2_measure_19.mid', 'k279-2/midi/k279-2_measure_20.mid', 'k279-2/midi/k279-2_measure_21.mid', 'k279-2/midi/k279-2_measure_22.mid', 'k279-2/midi/k279-2_measure_23.mid', 'k279-2/midi/k279-2_measure_24.mid', 'k279-2/midi/k279-2_measure_25.mid', 'k279-2/midi/k279-2_measure_26.mid', 'k279-2/midi/k279-2_measure_27.mid', 'k279-2/midi/k279-2_measure_28.mid', 'k279-2/midi/k279-2_measure_29.mid', 'k279-2/midi/k279-2_measure_30.mid', 'k279-2/midi/k279-2_measure_31.mid', 'k279-2/midi/k279-2_measure_32.mid', 'k279-2/midi/k279-2_measure_33.mid', 'k279-2/midi/k279-2_measure_34.mid', 'k279-2/midi/k279-2_measure_35.mid', 'k279-2/midi/k279-2_measure_36.mid', 'k279-2/midi/k279-2_measure_37.mid', 'k279-2/midi/k279-2_measure_38.mid', 'k279-2/midi/k279-2_measure_39.mid', 'k279-2/midi/k279-2_measure_40.mid', 'k279-2/midi/k279-2_measure_41.mid', 'k279-2/midi/k279-2_measure_42.mid', 'k279-2/midi/k279-2_measure_43.mid', 'k279-2/midi/k279-2_measure_44.mid', 'k279-2/midi/k279-2_measure_45.mid', 'k279-2/midi/k279-2_measure_46.mid', 'k279-2/midi/k279-2_measure_47.mid', 'k279-2/midi/k279-2_measure_48.mid', 'k279-2/midi/k279-2_measure_49.mid', 'k279-2/midi/k279-2_measure_50.mid', 'k279-2/midi/k279-2_measure_51.mid', 'k279-2/midi/k279-2_measure_52.mid', 'k279-2/midi/k279-2_measure_53.mid', 'k279-2/midi/k279-2_measure_54.mid', 'k279-2/midi/k279-2_measure_55.mid', 'k279-2/midi/k279-2_measure_56.mid', 'k279-2/midi/k279-2_measure_57.mid', 'k279-2/midi/k279-2_measure_58.mid', 'k279-2/midi/k279-2_measure_59.mid', 'k279-2/midi/k279-2_measure_60.mid', 'k279-2/midi/k279-2_measure_61.mid', 'k279-2/midi/k279-2_measure_62.mid', 'k279-2/midi/k279-2_measure_63.mid', 'k279-2/midi/k279-2_measure_64.mid', 'k279-2/midi/k279-2_measure_65.mid', 'k279-2/midi/k279-2_measure_66.mid', 'k279-2/midi/k279-2_measure_67.mid', 'k279-2/midi/k279-2_measure_68.mid', 'k279-2/midi/k279-2_measure_69.mid', 'k279-2/midi/k279-2_measure_70.mid', 'k279-2/midi/k279-2_measure_71.mid', 'k279-2/midi/k279-2_measure_72.mid', 'k279-2/midi/k279-2_measure_73.mid', 'k279-2/midi/k279-2_measure_74.mid', 'k279-2/midi/k279-2_measure_75.mid']
wav_measure_files = []
#import fluidsynth
from midi2audio import FluidSynth

environment.set('midiPath', '/mnt/c/Users/deser/Documents/School/FA19/490X')
fs = FluidSynth()

for i in range(len(s_measure_files)):
    filename = 'k279-2/wav/k279-2_measure_' + str(i) + '.wav'
    wav_measure_files.append(filename)
    srcpath = '/mnt/c/Users/deser/Documents/School/FA19/490X/'
    s_wav = fs.midi_to_audio((srcpath+s_measure_files[i]), (srcpath+filename))


