from reflectcast.input.process_input import save_reflection
from reflectcast.nlp.emotion_analysis import analyze_emotion
from reflectcast.nlp.generate_script import create_script
from reflectcast.audio.generate_audio import text_to_podcast
from reflectcast.audio.mix_audio import mix_voice_with_ambient
import os

def run_reflectcast():
    user_input = input("🌙 What's on your mind tonight?\n\n")
    
    # Save reflection
    reflection_file = save_reflection(user_input)
    
    # Analyze emotion
    emotion = analyze_emotion(user_input)
    
    # Generate script
    script = create_script(user_input, emotion)
    
    # Generate audio (voiceover)
    audio_file = text_to_podcast(script, emotion)

    # Define ambient track (choose based on mood or fixed)
    ambient_file = os.path.join("assets", "ambient", "rain.mp3")  # Example ambient sound
    
    # Define final mixed output path
    final_output_path = os.path.join("outputs", f"{emotion}_dreamy_mix.mp3")

    # Mix voice with ambient music
    final_audio = mix_voice_with_ambient(audio_file, ambient_file, output_path=final_output_path)

    print(f"\n✅ Your podcast with ambient music is ready at: {final_audio}")

if __name__ == "__main__":
    run_reflectcast()
