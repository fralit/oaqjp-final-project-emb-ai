'''This module use for detecting emotion
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''This function is used to detect emotion. Input is an argument text_to_analyze. 
    It returns text attribute of the response object as received from the Emotion Detection function.
    '''
    # Chekc empty input
    if not text_to_analyse:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=10000)
    # Check response status
    print(f"@linh: response: {response}")
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key= lambda x: emotions[x])
        emotions['dominant_emotion'] = dominant_emotion

        if dominant_emotion is None:
            return {'error': 'Invalid text! Please try again!'}

        return emotions
    else:
        return {'error': f'Error: Received status code {response.status_code}, Message: {response.text}'}
