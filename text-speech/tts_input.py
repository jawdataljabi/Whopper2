from tts import speak_text, get_voice_id


def main():
    """Main function that prompts for input and speaks text directly."""
    # Get voice ID at startup
    voice_id = get_voice_id(1)
    
    print("TTS ready. Enter text to speak (or 'exit' to quit)")
    
    while True:
        try:
            user_input = input("Enter text to send (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            
            if user_input.strip():
                print(f"Speaking: {user_input}")
                speak_text(user_input, voice_id=voice_id)
                print("Finished speaking")
                
        except KeyboardInterrupt:
            print("\nExiting.")
            break


if __name__ == "__main__":
    main()

