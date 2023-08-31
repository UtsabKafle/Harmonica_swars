import pyaudio
import wave,time

def get(data_):
    p = pyaudio.PyAudio()


    stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024
                        )

    frames = []
    seconds = 1.5

    for i in range(300):
        data = stream.read(1024)
        frames.append(data)
        print(data)

    print('DONE')
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(f'temp/{data_}.wav','wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

time.sleep(5)
# get()