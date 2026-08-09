''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package : 
# Import the sentiment_analyzer function from the package created:

from flask import Flask, render_template, request
from sentiment_analyzer import run_sentiment_analysis

#Initiate the flask app :
app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

@app.route("/sentimentAnalyzer", methods=["GET"])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # GET query parameter textToAnalyze
    # CALL sentiment_analyzer(textToAnalyze)
    text_to_analyze = request.args.get("textToAnalyze")
    response = run_sentiment_analysis(text_to_analyze)
    # IF response contains error:
    label = response['label']
    if label is None:
        # RETURN user-friendly error message string
        return "Invalid input! Try again."
    # ELSE: BUILD formatted sentence:
    else:
        # 'label': X,
        label = response['label']
        # 'negative': A,
        negative = response['negative']
        # 'neutral': B,
        neutral = response['neutral']
        # 'positive': C.”
        positive = response['positive']
        # RETURN formatted string to browser
        return(
            f"For the given statement, the system response is "
            f"'{label}' with negative score of {negative}, neutral score of {neutral}, and positive score of {positive}."
        )


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True, host="0.0.0.0", port=5000)
