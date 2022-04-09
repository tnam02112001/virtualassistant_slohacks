# SLO Hacks 2022 - Virtual Assistant Workshop

# Development Environment Set Up

## Install Python Thrid-Party Packages
Our project requires other Python packages that can be installed using pip. These packages can be automacially collected and installed by calling
`pip install -r requirements.txt`. You can also install each package seperately by following these intrusctions:

| Package Name | Install |
| --- | --- |
|pyttsx3| `pip install pyttsx3`|
|wikipedia| `pip install wikipedia`|
|GoogleNews| `pip install GoogleNews`|
|SpeechRecognition| `pip install SpeechRecognition==3.1.3`|

## Install PyAudio Package
PyAudio is a cross-platform audio input/output stream library. We will use this library to get input from microphone, and send output to speakers. Please follows this instruction to install PyAudio according to your opearating system.

### Windows OS
#### 1 - Install pipwin
This package can be installed by using `pip install pipwin`

#### 2 - Install PyAudio with pipwin
This package can be installed by using `pipwin install pyaudio`

### Mac OS
#### 1 - Installing xcode
xcode can be installed from Apple App Store. If you have already done so, please skip this step.
After installing xcode, you may want to restart your computer to fully complete the installation.

#### 2 - Installing portaudio
This package can be installed by using 
```
brew remove portaudio
brew install portaudio
```

#### 2 - Installing PyAudio with pipwin
This package can be installed by using `pip install pyaudio`


