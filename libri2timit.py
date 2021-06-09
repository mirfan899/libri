import glob
from utils import get_name_from_path


def generate_timit_phoneme_files():
    phonemes_files = glob.glob("data/label/*.phonemes")
    for phoneme_file in phonemes_files:
        name = get_name_from_path(phoneme_file)
        text = open(phoneme_file).readlines()[0]
        # add h# as silence
        text = "h# " + text + " h#"
        phonemes = text.split()
        with open("data/label/{}.phn".format(name), "w") as f:
            for i, ph in enumerate(phonemes):
                f.write("{} {} {}\n".format(i, i+1, ph).lower())


def generate_timit_wrd_files():
    word_files = glob.glob("data/label/*.txt")
    for word_file in word_files:
        name = get_name_from_path(word_file)
        text = open(word_file).readlines()[0]
        words = text.split()
        with open("data/label/{}.wrd".format(name), "w") as f:
            for i, wrd in enumerate(words):
                f.write("{} {} {}\n".format(i, i + 1, wrd).lower())


if __name__ == "__main__":
    generate_timit_phoneme_files()
    generate_timit_wrd_files()
