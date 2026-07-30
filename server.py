''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : 
# Import the sentiment_analyzer function from the package created:

import flask, render_template
from sentiment_analyzer import sentiment_analyzer

#Initiate the flask app :
app = Flask('sentiment_analyzer')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # GET query parameter textToAnalyze
    # CALL sentiment_analyzer(textToAnalyze)
    # IF response contains error:
    # RETURN user-friendly error message string
    # ELSE:
    # BUILD formatted sentence:
    # “For the given statement, the system response is
    # 'label': X,
    # 'negative': A,
    # 'neutral': B,
    # 'positive': C.”
    # RETURN formatted string to browser

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
