# vertecken.py

def verstecken(s,   # text (string)
               n=1    # number of random capital letters (int)
               ):
    """ the function encript the given text "s"

        s should be a text in string format,
        n is a integer number.
        the function returns the encripted text
        J. Reyes 04.06.2018
    """
    from random import randint

    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newS = ""
    s=s.upper()

    for l in s:
        newS += l
        for x in range(n):
            newS += ABC[randint(0, len(ABC)-1)]
    return newS

