# DEFINE function sentiment_analyzer(text)
def run_sentiment_analysis():
# IF text is empty:
    #TODO 
    #RETURN error object indicating invalid input
    return()
    # CALL Watson NLP endpoint/library with text
    print("Watson has been called")
    # PARSE response to extract:
    score = watson_response
        # negative score
        if score == "negative":
            print("negative")
        # neutral score
        elif score == "neutral":
            print("neutral")
        # positive score
        elif score == "positive":
            print("positive")
        # dominant sentiment label

        # RETURN dictionary/object with parsed values

        # HANDLE network/API exceptions and return error object