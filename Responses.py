def responses(input_text):
    user_message = str(input_text).upper()

    if user_message in ("NRIC"):
        return ("Correct suffix")
    else : 
        return ("Try again mortal")
