import glob
import os
import subprocess
from utils import get_name_from_path, get_phonemes_only, generate_transcripts_data


def generate_timit_data():
    """
    Reads the LibriSpeech dev-clean datasets and copies the audios(duration 10s or less) and copies the transcripts for
    further processing.
    :return:
    """
    root = 'LibriSpeech'

    for subdir, dirs, files in os.walk(root):
        for file in files:
            if "txt" in file:
                os.system("mv {} ./data/transcripts/".format(os.path.join(subdir, file)))
            elif "flac" in file:
                duration = subprocess.check_output("ffprobe -i {} -show_format | sed -n 's/duration=//p'".format(os.path.join(subdir, file)), shell=True)
                name = os.path.splitext(file)[0]
                # convert flac to wav with 256 bitrate
                if float(duration.decode()) <= 10.0:
                    os.system("ffmpeg -i {} -ab 256 ./data/wav/{}.wav".format(os.path.join(subdir, file), name))


def generate_clean_data():
    """
    generate label files and remove unnecessary transcripts
    :return:
    """
    labels = glob.glob("data/label/*.txt")
    wavs = glob.glob("data/wav/*.wav")

    labels = [os.path.splitext(os.path.basename(x))[0] for x in labels]
    wavs = [os.path.splitext(os.path.basename(x))[0] for x in wavs]
    to_remove = [x for x in labels if x not in wavs]
    for r in to_remove:
        os.system("rm data/label/{}.txt".format(r))


def generate_phoneme_files():
    transcripts = glob.glob("data/label/*.txt")
    for transcript in transcripts:
        name = get_name_from_path(transcript)
        text = open(transcript).readlines()[0]
        phonemes = get_phonemes_only(text)
        with open("data/label/{}.phonemes".format(name), "w") as f:
            f.write(" ".join(phonemes).lower())


if __name__ == "__main__":
    generate_timit_data()
    generate_transcripts_data()
    generate_clean_data()
    generate_phoneme_files()
