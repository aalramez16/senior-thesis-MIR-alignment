# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 07:45:15 2019

@author: deser
"""

from music21 import converter, stream
#environment.set('midiPath', '/mnt/c/Users/deser/Documents/School/FA19/490X')


s = converter.parse('k279-2.krn')
filename = 'k279-2'

measure_length = len(s.getElementsByClass(stream.Part)[0].getElementsByClass(stream.Measure))
print(measure_length)

s_measure_files = []

for i in range(measure_length):
    filepath = filename + '/midi/' + filename + '_measure_' + str(i) + '.mid'
    s_measure_files.append(filepath)    # In the event that this variable may be useful
    
    s_measure_midi = s.measure(i).write('midi',filepath)   # This is where the files are being written
    