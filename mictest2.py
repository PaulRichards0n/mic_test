import sounddevice as sd
import wave

def record_audio(duration, filename, samplerate=44100):
    # Record audio for the given duration
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished")

    # Save the recorded audio to a file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    print(f"Audio saved to {filename}")

# Example usage
record_audio(duration=5, filename='test.wav')  # Records for 5 seconds and saves to test.wav