'''Emotion detection app for final project of IBM Developing AI
Applications with Python and Flask course.'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_desc():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response is None or response["dominant_emotion"] is None:
        reply_text = "Invalid text! Please try again!"
    else:
        reply_text = "For the given statement, the system response is "
        reply_text += f"'anger': {response['anger']}, "
        reply_text += f"'disgust': {response['disgust']}, "
        reply_text += f"'fear': {response['fear']}, "
        reply_text += f"'joy': {response['joy']} and "
        reply_text += f"'sadness': {response['sadness']}."
        reply_text += f" The dominant emotion is {response['dominant_emotion']}."

    return reply_text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
