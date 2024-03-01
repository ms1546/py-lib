from mido import Message, MidiFile, MidiTrack

B3 = 59
C4 = 60
Cs4 = 61
D4 = 62
E4 = 64
F4 = 65
fs4 = 66
G4 = 67
A4 = 69
B4 = 71
C5 = 72
D5 = 74

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))

notes = [C4, G4, F4, E4, Cs4, D4, A4, A4, B3, B4, A4, G4, fs4, G4, C5, C5, D5, C5, B4, A4, G4, F4, E4, D4, A4, A4, B3, B3, C4]  # C4, D4, E4, F4, G4, A4, B4, C5
for note in notes:
    track.append(Message('note_on', note=note, velocity=64, time=240))
    track.append(Message('note_off', note=note, velocity=64, time=480))

mid.save('./simple_melody.mid')
