''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : 
# Import the sentiment_analyzer function from the package created:

import flask, render_template, request
from sentiment_analyzer import sentiment_analysis

#Initiate the flask app :
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Forget any user_id
    session.clear()

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    user_id = session["user_id"]
    return render_template("index.html")

@app.route("/sentimentAnalyzer", methods=["GET"])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # GET query parameter textToAnalyze
    if request.method == "GET":
        # CALL sentiment_analyzer(textToAnalyze)
        sentiment_analysis
    # IF response contains error:
    
    # RETURN user-friendly error message string
    # ELSE:
    else:
        print("error")
    # BUILD formatted sentence:
    # “For the given statement, the system response is

    # 'label': X,
    # 'negative': A,
    # 'neutral': B,
    # 'positive': C.”
    # RETURN formatted string to browser


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True, host="0.0.0.0", port=5000)
