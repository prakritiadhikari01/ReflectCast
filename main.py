from reflectcast.input.process_input import save_reflection
from reflectcast.nlp.emotion_analysis import analyze_emotion
from reflectcast.nlp.generate_script import create_script
from reflectcast.audio.generate_audio import text_to_podcast

def run_reflectcast():
    user_input = input("🌙 What's on your mind tonight?\n\n")
    
    # Save reflection
    reflection_file = save_reflection(user_input)
    
    # Analyze emotion
    emotion = analyze_emotion(user_input)
    
    # Generate script
    script = create_script(user_input, emotion)
    
    # Generate audio
    audio_file = text_to_podcast(script, emotion)

    print(f"\n✅ Your podcast is ready at: {audio_file}")

if __name__ == "__main__":
    run_reflectcast()
