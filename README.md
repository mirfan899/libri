### LibriSpeech Data generation for Phoneme recognition
This repository contains the librispeech subset of dev-clean.


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

