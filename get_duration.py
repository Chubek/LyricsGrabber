from pydub import AudioSegment

def open_audio(path):
    ext = path.split(".")[-1]

    try:
        aud = AudioSegment.from_file("never_gonna_give_you_up.mp4", ext)
    except:
        raise Exception(f"Could not open file {path} with extension {ext}.")

    return aud

def get_dur(path):
    aud = open_audio(path)

    return aud.duration_seconds