"""Functions for forecasting what Bob will say."""


def response(hey_bob: str) -> str:
    s = hey_bob.strip()

    if s == "":
        return "Fine. Be that way!" 
    if s.isupper() and not s.endswith("?") and any(ch.isalpha() for ch in s):
        return "Whoa, chill out!"
    if s.isupper() and s.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if s.endswith("?"):
        return "Sure."
    return "Whatever." 
    
        
    
        
    
