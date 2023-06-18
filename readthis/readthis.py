#!/usr/bin/env python3

from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play as pydub_play
import argparse
import sys, os
import concurrent.futures
import pkg_resources


DATA_PATH = pkg_resources.resource_filename('readthis', 'data/')

MAX_GTTS_INPUT = 300 # Max bytes (found 5000 online)
MAX_GTTS_RQTS = 1000 # Max requests *per minutes* (found 1000 online)

def play_audio(mp3_fp):

    audio_segment = AudioSegment.from_file(mp3_fp, format='mp3')
    pydub_play(audio_segment)

def get_audio(text, lang):

    tts = gTTS(text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

def read_text(fragments, lang):

    mp3_fp = get_audio(fragments[0], args.lang)
    if len(fragments) == 1:
        play_audio(mp3_fp)

    for i in range(1, min(MAX_GTTS_RQTS, len(fragments))):

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(play_audio, mp3_fp)
            mp3_fp = get_audio(fragments[i], args.lang)

def handle_limits(text):

    fragments = []
    i = 0
    d = '.'
    
    for token in text.split(d):
        if len(fragments) == 0:
            fragments.append(token)
            continue
        if len(fragments[i]) + len(token) < MAX_GTTS_INPUT:
            fragments[i] += d + token
        else:
            i += 1
            fragments.append(token)
    return fragments

def main():

    default_text = os.path.join(DATA_PATH, 'default_text.txt')

    parser = argparse.ArgumentParser(description='reads a text using google API')
    parser.add_argument(
        '--lang', '-l', metavar='LANG', default='en',
        help='Choose language to use for reading.'
    )
    parser.add_argument(
        'text', metavar='FILE', nargs='?', default=default_text,
        help='File to read, or - for stdin'
    )
    args = parser.parse_args()

    text = ''
    # Get input from file or stdin
    if args.text == '-':
        text = sys.stdin.read()
    else:
        with open(args.text) as f:
            text = f.read()

    fragments = handle_limits(text)
    read_text(fragments, args.lang)

if __name__ == '__main__':
    main()