import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    # this function will return pydubs audio segment
    combined = AudioSegment.empty()
    for audio in audios:
        combined = combined+AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3('Train Announcement.mp3')
    # 1- Generate Kripya dhyan dijiye
    start = 00
    finish = 3500
    audioprocessed = audio[start:finish]
    audioprocessed.export("1_hindi.mp3", format="mp3")

    # 2- from

    # 3- Generate se aane vali
    start = 10600
    finish = 11500
    audioprocessed = audio[start:finish]
    audioprocessed.export("3_hindi.mp3", format="mp3")

    # 4- via city

    # 5- ke raste
    start = 8900
    finish = 9650
    audioprocessed = audio[start:finish]
    audioprocessed.export("5_hindi.mp3", format="mp3")

    # 6- train number and name
    # 7- platform number
    start = 11500
    finish = 12570
    audioprocessed = audio[start:finish]
    audioprocessed.export("7_hindi.mp3", format="mp3")
    # 8- platform number

    # 9- generate par aa rahi hai
    start = 13500
    finish = 15000
    audioprocessed = audio[start:finish]
    audioprocessed.export("9_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # generate 2- from city
        textToSpeech(item['From'], '2_hindi.mp3')

        # generate 4- via city
        textToSpeech(item['Via'], '4_hindi.mp3')

        # generate 6- train number and name
        textToSpeech(item['Train_number'] + "  " + item['Train_name'], '6_hindi.mp3')

        # generate 8- platform number
        textToSpeech(item['Platform'], '8_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 10)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['Train_number']}_{index+1}.mp3", format="mp3")


if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("Train Schedule.xlsx")
