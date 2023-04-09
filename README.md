# GPTSense - ChatGPT Classifier

Daniel Ke (Front end)

Michael Xu (Front end)

Zhiyuan Li (Back end, AI)

Aiden Lundberg (Pitch, idea)


## Dependencies
```
git clone git@github.com:FakeZhiyuanLi/GPTSense.git
cd GPTSense
pip install requirements.txt
```

## About
Tensorflow text classification model trained on 32,000 examples of OpenAI GPT-3.5-Turbo API and 10,000 examples of human responses scraped from blogs

## Run code
```
flask run
```
![empty text](https://i.imgur.com/eV3CWv8.png)

Enter text into input area (works best between 5-30 lines)

Click submit

![with text](https://i.imgur.com/H5ZxQDg.png)
Result shows between 0-100% chance of chatGPT response


Percentages above 60% are likely chatGPT, can be false positive at times
Percentages abobe 90% are most likely chatGPT, can also be false positive

![history](https://i.imgur.com/9bi2V06.png)
Scroll down for a history of past checks

Click on the box to copy the response


## Credits
Questions database: https://github.com/xinyadu/nqg


## Debug
### Error installing dependencies
This is likely the fault of tensorflow-macos and tensorflow-metal, these are macos specific versions of Tensorflow and do not exist on windows

Solution: delete these modules from requirements.txt and run ``` pip install tensorflow ``` 
