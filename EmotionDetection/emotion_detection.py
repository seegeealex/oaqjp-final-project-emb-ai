import requests
import json
from pprint import pprint

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    
    reply_text = response.text
    reply_json = json.loads(reply_text)
    emotions = reply_json['emotionPredictions'][0]['emotion']

    max_emotion_score = -1000
    max_emotion = ""
    emotion_scores = {}    
    for emotion in emotions.keys():
        score = emotions[emotion]
        emotion_scores[emotion] = score
        if score > max_emotion_score:
            max_emotion_score = score
            max_emotion = emotion
    emotion_scores["dominant_emotion"] = max_emotion

    return emotion_scores
