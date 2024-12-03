''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector', methods=['GET'])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and runs sentiment analysis
        over it using emotion_detector() function. The output returned shows a set of emotions 
        with its score and the dominant emotion
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze', '')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Check the dominant emotion
    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is <b> {response['dominant_emotion']} </b>."
    )

    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Return the index page
    return render_template('index.html')

if __name__ == "__main__":
    # Run the app
    app.run(host='0.0.0.0', port=5000)
