import librosa
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def calculate_midi_from_frequencies(frequencies):
    b=np.log2(440.0)
    dk=[]
    for i in frequencies:
        if i<=60:
            i = 60.4
        try:
            a = mysva(i)
        except Exception as e:
            pass
        dk.append(a)
    return dk
def mysva(frequency):
    svara_mapping = {
        "Sa": (0, 240),
        "Re": (240, 254.27),
        "Re2":(254,269.39),
        "Ga": (269, 285),
        "Ga2":(285,302.38),
        "Ma": (302, 339),
        "Pa": (339, 359.6),
        "Dha": (359, 403),
        "Ni": (403, 453),
        "SaHigh": (453, 480)
    }
    for svara, (low, high) in svara_mapping.items():
        if low <= frequency <= high:
            return svara
    
    return str(frequency)

def get_svara(data_):
    # Load audio file
    audio_file = f'temp/{data_}.wav'
    y, sr = librosa.load(audio_file)

    # Perform pitch tracking
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    # Get the dominant pitch for each time frame
    dominant_pitches = np.argmax(magnitudes, axis=0)
    dominant_frequencies = pitches[dominant_pitches, np.arange(pitches.shape[1])]

    # Convert frequencies to MIDI notes
    midi_notes = calculate_midi_from_frequencies(dominant_frequencies)



    # Print the svara notations
    # for svara in svara_notations:
    #     time.sleep(0.5)
    #     print(svara)

    # print(svara_notations[0:20])
    ctr={}
    for i in range(len(midi_notes)):
        if round(dominant_frequencies[i]) not in ctr.keys():
            ctr[round(dominant_frequencies[i])] = 1
        else:
            ctr[round(dominant_frequencies[i])] += 1
        print(midi_notes[i],end=" -- ")
        try:
            print(dominant_frequencies[i])
        except:
            continue
    print(ctr)
    vl = list(ctr.values())
    vl.sort()
    print(vl)
# get_svara()