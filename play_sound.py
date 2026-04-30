import os

def play_sound():
    """Play the sound voice_note.wav file."""
    audio_file = 'voice_note.wav'

    if not os.path.exists(audio_file):
        print(f"Error: {audio_file} not found in the current directory.")
        return False

    try:
        import winsound
        winsound.PlaySound(audio_file, winsound.SND_FILENAME)
        print(f"Playing {audio_file}...")
        return True
    except Exception as e:
        print(f"Error playing sound: {e}")
        return False

if __name__ == '__main__':
    play_sound()
