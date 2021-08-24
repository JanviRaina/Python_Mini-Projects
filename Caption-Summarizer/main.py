from pytube import YouTube
import transformers
import os, sys
import glob
import re
import argparse
 
inp_url=input("Enter input URL \n")
myVideo=YouTube(inp_url)
print(" Title : "+ myVideo.title)
print("\n")
caption=myVideo.captions.get_by_language_code('a.en')
cap=caption.generate_srt_captions()
 
f = open("Captions.txt", "a")
f.write(cap)
f.close()
 
text=""
srts = glob.glob("Captions.txt")
for srt in srts:
    with open(srt, encoding="utf8",mode="r") as r:
        c = r.readlines()
        fulltime = re.compile(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")
        indexre = re.compile(r"\d+\n")
        c = [s for s in c if not re.findall(fulltime, s) and not re.findall(indexre,s) and not s == "\n"]
        # text = '\n'.join(c)
        text =' '.join(c)
        text.strip()
    with open(srt, encoding="utf8",mode="w") as w:
        w.write(text)
 
context =text
summ_model = transformers.pipeline("summarization")
qa_model = transformers.pipeline("question-answering")
 
def get_summary(context, model = summ_model):
    return model(context)[0]['summary_text']
 
print('Summary: \n', get_summary(context))
 
 
# https://www.youtube.com/watch?v=Z565J4Vx9D4&ab_channel=Hopster
