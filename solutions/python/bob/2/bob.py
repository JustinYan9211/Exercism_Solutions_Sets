"""Functions for forecasting what Bob will say."""


def response(hey_bob: str) -> str:
    s = hey_bob.strip()

    if s == "":
        return "Fine. Be that way!" 

    is_question = s.endswith("?")
    has_letters = any(ch.isalpha() for ch in s)
    is_upper = s.isupper()
    is_yelling = is_upper and has_letters
        
    if is_yelling and not is_question:
        return "Whoa, chill out!"
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    return "Whatever." 
    
        
    
        
    
