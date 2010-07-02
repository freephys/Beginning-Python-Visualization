def word_line_count(s):
    """Returns the number of words and the numbers of lines in a string."""
    
    return (len(s.split()), len(s.splitlines()))
