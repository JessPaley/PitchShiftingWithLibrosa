# Changes the key by a user-specified number of semitones

import librosa
import soundfile


def main():
    filename = librosa.example("brahms")
    y, sr = librosa.load(filename)
    steps = float(input("Number of semitones to shift audio file: "))
    new_y = librosa.effects.pitch_shift(y, sr, steps)
    soundfile.write("pitchShifted.wav", new_y, sr,)


main()
