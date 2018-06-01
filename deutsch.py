#deutsch.py

def deutsch(s):
    def h(text, buchstabe):
        text.upper()
        anzahl = text.count(buchstabe)
        relativeHaeufigkeit = float(anzahl)*100/len(text)
        return relativeHaeufigkeit

    if (4<h(s,"a")<9) and (14<h(s,"e")<20) and (h(s,"y")<1):
                                                return True
    else:
                                                return False


text = input("Text: ")
if deutsch(text):
    print("vermulich deutsch")
else:
    print("vermutlich nicht deutsch")
                                                
