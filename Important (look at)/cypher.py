def NotCeasar(message,codeword):
    codeword = codeword.lower()
    message = message.lower()
    finalmessage=""
    while len(message) > len(codeword):
        codeword = codeword + codeword
        
    codeword = codeword[:len(message)]
    for x in range(len(message)):
        letter = ord(message[x])
        check = ord(codeword[x])-97
        if letter >= 97 and letter < 123:
            
            letter = letter + check
            if letter > 122:
                letter=letter-26
        letter = chr(letter)
        finalmessage = finalmessage+letter
        
    return finalmessage
    
def Ceasar(message,code):
    finalmessage=""
    message = message.lower()
    if code > 26:
        code = code%26
    for i in range(len(message)):
        letter = ord(message[i])
        if letter >=97 and letter <= 122:
            letter = letter + code
            if letter >122:
                letter=letter-26
        letter = chr(letter)
        finalmessage = finalmessage + letter
        
    return finalmessage
def AsciiConvert(code,mode):
    pass