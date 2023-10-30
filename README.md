# automatic speech recognition with wav2vec2 

Use any wav2vec model with a microphone.

## Setup

```
pip install -r requirements.txt
```

Depending on linux distribution you might encounter an **error that portaudio was not found** when installing pyaudio. For Ubuntu you can solve that issue by installing the "portaudio19-dev" package.

```
sudo apt install portaudio19-dev
```

Finally you can test the speech recognition:
for basic speech recpgnition.
```
python wav2vec2_inference.py
```
or below comment for near real time speech recpgnition (applied voice activity detection to recognize voice, noice or silent)
```
python live_vad_asr.py
```
optional arguments:
`-dest` or `--destination_laguage` to specify translation destination language, default will be translate into english, you can specify into mandarin with value "zh-cn"

### Possible Issues:

* The code uses the systems default audio device. Please make sure that you set your systems default audio device correctly. 

* "*attempt to connect to server failed*" you can safely ignore this message from pyaudio. It just means, that pyaudio can't connect to the jack audio server. 


## Usage

You can use any **wav2vec2** model from the [huggingface model hub](https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&search=wav2vec2). Just set the model name, all files will be downloaded on first execution.

```python 
python live_vad_asr.py
```
