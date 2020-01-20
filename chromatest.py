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


#import fluidsynth
from midi2audio import FluidSynth

environment.set('midiPath', '/mnt/c/Users/deser/Documents/School/FA19/490X')

s = converter.parse('k279-2.krn')
s.show('midi')

s_midi = s.write('midi','k279-2.mid')

#fp = s.write('midi', fp = r'C:\Users\deser\Documents\School\Project Proposal')

fs = FluidSynth()

s_wav = fs.midi_to_audio('k279-2.mid', 'output2.wav')

#x, sr = librosa.load('output2.wav')
#ipd.Audio(x, rate=sr)

#ipd.Audio(x, rate=sr)
#librosa.load('C:\Users\deser\Documents\School\Project Proposal\s_midi.mid')