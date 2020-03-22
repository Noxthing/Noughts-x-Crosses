def daddys_function(name):
	if name == "Daddy":
		return "28/12/1974"
	elif name == "Luca":
		return "04/06/2006"
	elif name == "Christopher":
		return "23/01/2006"
	else:
		return "I don't know"
        
def C_function(number_str):
    """
    This function gives you the inverse of any of the three following numbers: "5","8" or "9"
    """
    if number_str == "5":
        return "0.2"
    elif number_str == "9":
        return "Approximately 0.111..."
        
    elif number_str == "8":
        return "0.125"
    else:
        return "Go ask someone else, I'm too lazy to tell you"
    
def C_function_2 (x):
	"""
    This function gives you the inverse of any number_str
    """
	return 1/x
