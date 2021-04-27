import glob
import os
from string import digits
from constants import DICTIONARY
from g2p_en import G2p
g2p = G2p()


def generate_transcripts_data():
    """
    Read transcript files and generate separate file for each line
    :return:
    """
    transcripts = glob.glob("data/transcripts/*.txt")

    for transcript in transcripts:
        lines = open(transcript).readlines()
        for line in lines:
            name, text = line.split(" ", 1)
            with open("data/label/{}.txt".format(name), "w") as writer:
                writer.write(text.strip().lower())


def get_phonemes_only(sentence):
    words = sentence.upper().split()

    phonemes_only = []
    for word in words:
        if word in DICTIONARY.keys():
            phonemes_only.append(DICTIONARY[word])
        else:
            predicted_phoneme = g2p(word)
            phonemes_only.append(" ".join(predicted_phoneme))

    phonemes_only_cleaned = []
    for ph in phonemes_only:
        p = ph.translate(str.maketrans('', '', digits))
        phonemes_only_cleaned.append(p)

    return phonemes_only_cleaned


def get_name_from_path(path):
    return os.path.splitext(os.path.basename(path))[0]


def generate_phoneme_file(path):
    name = os.path.splitext(os.path.basename(path))[0] + ".phonemes"
    lines = open(path, "r").readlines()
    phonemes = []
    for line in lines:
        start, end, ph = line.split(" ")
        phonemes.append(ph.strip())
    phonemes = " ".join(phonemes)
    with open("timit/label/{}".format(name), "w") as f:
        f.write(phonemes)


def generate_cmu_phoneme_file(path):
    name = os.path.splitext(os.path.basename(path))[0] + ".phonemes"
    lines = open(path, "r").readlines()
    cmu_phonemes = []
    for line in lines:
        cmu_phonemes = get_phonemes_only(line)
    cmu_phonemes = " ".join(cmu_phonemes).lower()
    with open("data/label/{}".format(name), "w") as f:
        f.write(cmu_phonemes)


def generate_word_file(path):
    name = os.path.splitext(os.path.basename(path))[0] + ".txt"
    lines = open(path, "r").readlines()
    words = []
    for line in lines:
        start, end, word = line.split(" ")
        words.append(word.strip())

    words = " ".join(words)
    with open("timit/label/{}".format(name), "w") as f:
        f.write(words)
