from pydub import AudioSegment
from pydub.playback import play
sound = AudioSegment.from_file('YT_Track 5.wav', format="wav")

octaves = -0.5

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

hipitch_sound = hipitch_sound.set_frame_rate(44100)

play(hipitch_sound)

