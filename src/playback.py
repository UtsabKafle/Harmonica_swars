import pyaudio
import wave
import sys



def play(data_):
    CHUNK = 1024

    wf = wave.open(f"temp/{data_}.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    print('i got here')
    stream.stop_stream()
    stream.close()

    p.terminate()
    print('here playback')
    return 'hehe'

play('utsab')