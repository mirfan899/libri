### LibriSpeech Data generation for Phoneme recognition
This repository contains the librispeech subset of dev-clean.

## Download data
Download the librispeech dataset and place it in this directory

## Feature data
Now create `data` directory and 3 nested directory i.e. `transcripts`, `label`, `wav`

## Prepare Librispeech data
run 
```shell
prep_dev.py
```
to extract the 10 seconds audio from LibriSpeech directory and use it for phoneme recognition.

After that use `libri2timit.py` for data supported by phoneme.

## Get duration of audios
```shell script
ffprobe -i audio -show_format | sed -n 's/duration=//p'

# convert flac to wav with 256 bitrate
cd data/wav
for file in *.flac; do
    filename=$(basename -- "$file")
    name="${filename%.*}"
    ffmpeg -i "$file" -ab 256 "$(basename "$name").wav"
done

rm *.flac
```


Move  wrd and phn files to wav as it is used in CTC_pytorch project
```shell script
mv data/label/*.wrd data/wav/
mv data/label/*.phn data/wav/
```


