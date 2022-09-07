# PitchShiftingWithLibrosa

The Librosa library in Python is an indispensable tool in audio and music analysis. Librosa is particularly useful in finding trends or commonalities in large datasets of audio files through extraction of features such as pitch chroma and RMS, tempo and beat onset detection, and separation of percussive and harmonic instruments. Librosa includes methods for altering the pitch and speed of an audio file, which is useful in comparing files that have different keys or tempos.

This simple project utilizes Librosa’s pitch shift function to change the pitch of the audio file by a user-specified number of semitones (for reference, a change of one semitone would be equivalent to half a step, or moving every note to the adjacent piano key).

To use Librosa you must first install it and import it into your project.

The filename variable includes the file path of the audio file, which can be absolute or relative. Librosa has some example audio files that can be accessed using the Librosa example method, and these files can also be downloaded on the Librosa website.

The load method returns two variables, the time series (y) and the sample rate (sr), which is the number of samples per second. 

The pitch shift function takes in the time series, sample rate, and the number of steps or semitones to increase or decrease the pitch, which is denoted by a positive or negative integer, respectively. Note that the number of steps does not have to be an integer; because we are using float values it is possible to shift the pitch by a fraction of a semitone. In this project the bins per octave keeps its default value of twelve, but this parameter can be altered to divide the octave differently. The function returns a new time series, which we can use alongside the sample rate to write a new audio file using the SoundFile library.

Librosa’s pitch shifting method may seem simple on the surface, but this method actually uses time stretching and resampling under the hood to preserve the length of the audio file while changing the pitch. This is necessary because compressing any waveform in time increases its frequency, or in other words the pitch changes. This is why playing a record at a different speed will change the pitch of the song. Resampling can cause artifacts in the sound, and this is an area which is continuing to be improved in audio technology
