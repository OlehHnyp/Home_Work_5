def areYouPlayingBanjo(name):
    """
    This function answers the question
    'Are you playing jango?'
    Input parameters: name
    Output: name + answer
    """

    answer_1 = " plays banjo"
    answer = " does not play banjo"    
    if name[0].lower() == 'r':
        answer = answer_1
    return f"{name}{answer}"




    