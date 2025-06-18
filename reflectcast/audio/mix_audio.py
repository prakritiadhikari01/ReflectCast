from pydub import AudioSegment
import os

def mix_voice_with_ambient(voice_path: str, ambient_path: str, output_path: str = "outputs/final_mix.mp3", music_volume_dB: float = -18.0):
    # Load voice and ambient
    voice = AudioSegment.from_file(voice_path)
    ambient = AudioSegment.from_file(ambient_path)

    # Loop ambient if it's shorter than the voice
    if len(ambient) < len(voice):
        loops_needed = int(len(voice) / len(ambient)) + 1
        ambient = ambient * loops_needed

    # Trim ambient to match voice length
    ambient = ambient[:len(voice)]

    # Lower ambient volume to sit beneath the voice
    ambient = ambient - abs(music_volume_dB)

    # Mix both tracks
    combined = voice.overlay(ambient)

    # Export
    combined.export(output_path, format="mp3")
    return output_path
