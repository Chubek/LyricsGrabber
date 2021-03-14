from pprint import pprint
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from mutagen.flac import FLAC
from mutagen.m4a import M4A
from util import convert
from get_duration import get_dur
from mutagen.id3 import ID3, USLT
from get_lyrics import get_lyrics
import re

dict_objct = {
    'm4a': M4A,
    'mp3': MP3,
    'flac': FLAC,
    'wav': WAVE
}

def set_length(path, objct, dur):
    aud = objct(path)

    aud.info.length = convert(dur)

    aud.save()

def outer_set_length(path):
    dur = get_dur(path)

    ext = path.split(".")[-1]

    set_length(path, dict_objct[ext], dur)


def set_lyrics(path):
    tags = ID3(path)

 
    lyrics = get_lyrics(tags['TIT2'].text[0], tags['TPE1'].text[0])

    fin_lyr = None
    
    for lyric in lyrics:
        if bool(re.match(tags['TIT2'].text[0], lyric[1]['song']['title'])):
            fin_lyr = lyric[0]

    tags[u"USLT"] = USLT(encoding=3, lang=u'eng', desc=u'desc', text=fin_lyr)

    tags.save()

