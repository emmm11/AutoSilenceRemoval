from pydub import AudioSegment


def find_initial_silence(sound, silence_threshold=-50.0, chunk_duration=5):
   
    trim_ms = 0 
    while sound[trim_ms:trim_ms+chunk_duration].dBFS < silence_threshold:
        trim_ms += chunk_duration
    return trim_ms

if __name__ == '__main__':

    sound = AudioSegment.from_file('audio_with_silence.mp4', format="mp4")

    start_trim = find_initial_silence(sound)
    end_trim = find_initial_silence(sound.reverse())

    duration = len(sound)
    trimmed_sound = sound[start_trim:duration-end_trim]
    trimmed_sound.export('audio_without_silence.mp4', format="mp4")