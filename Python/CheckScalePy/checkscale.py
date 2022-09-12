import music21

score = music21.converter.parse('untitled.mid')
key = score.analyze('key')
print(key.tonic.name, key.mode)