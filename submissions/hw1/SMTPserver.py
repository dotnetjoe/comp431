from sys import stdin
import os

def letters(domain):
    # check for letters
    for x in domain:
        if x.isalpha() == False :
            return False
    return True

def numbers(domain): 
    # check for numbers
    for x in domain:
        if x.isdigit() == False :
            return False
    return True

def specialCharacters(str):
    # check for special characters
    for x in str:
        if (x == '<' or x == '>' or x == '(' or x == ')' or x == '[' or x == ']' or x == '\\' or 
            x == '.' or x == ',' or x == ';' or x == ':' or x == '@' or x == '"' or x == ' ' ):
            # every speacial character contained in a MAIL RCT or DATA
            return False
    return True

def parseMail(mail):
    if mail == "MAIL":
        return True
    else:
        return False

def parseFrom(fromInput):
    if fromInput == "FROM:":
        return True
    else:
        return False

def parseDomain(domain):
    for characters in domain:
        # check for incorrect characters like whitespace
        if characters == " " or characters =="\t":
            return False
    splitElements = domain.split(".")
    for x in splitElements:
        if x == '':
            return False
        if letters(x[0]) == False:
            return False
        else:
            for y in x:
                if letters(y) == False and numbers(y) == False:
                    return False
    return True

def whiteSpace(string):
    index = 0
    for x in string:
        # check spaces, tabs, and whitespace characters
        if x != ' ' and x != '\t' and x != '\s':
            return string[index:]
        index += 1


def getL(string):
    # left angle bracket to split email
    return string.find("<")

def getR(string):
    # right angle bracket to split email
    return string.find(">")

def okay():
    print("250 OK",end="\r\n")
    
def startMailWith():
    print("354 Start mail input; end with . on a line by itself",end="\r\n")
    
def synErrComm():
    print("500 Syntax error: command unrecognized",end="\r\n")

def synErrPar():
    print("501 Syntax error in parameters or arguments",end="\r\n")
    
def badSeq():
    print("503 Bad sequence of commands",end="\r\n")
    

def mailComms(key, string, status):
    if key == "start":
        if parseMail(string[:4]) and parseMail(string.split()[0]):
            if mailComms("mail", string, status): 
                # check to see if message is valid and parsable
                return 1, string
            else:
                return status, ""
                
        elif string[:4] == "RCPT":
                if mailComms("RCPT", string, status):
                    return 2, string
                else:
                    return status, ""

        elif string[:4] == "DATA":
            if status == 2:
                if mailComms("DATA", string, 3):
                    return 4, ""
                else:
                    return status, ""
            else:
                badSeq()
                return status, ""
        else:
            synErrComm()
            return status, ""

    elif key == "mail":
        if parseMail(string[:4]) and parseMail(string.split()[0]):
            if mailComms("from", whiteSpace(string[4:]), status):
                return True
            else:
                return False
        else:
            synErrComm()
            return False

    elif key == "from":
        if string.find("from:") != -1 or string.find("FROM:") != -1:
            if status == 0 or status == 4:
                if mailComms("reverse-path", whiteSpace(string[5:]), status):
                    return True
                else:
                    return False
            else:
                badSeq()
                return False
        else:
            synErrComm()
            return False

    elif key == "RCPT":
        if string[:4] == "RCPT" and string.split()[0] == "RCPT":
            if mailComms("to", whiteSpace(string[4:]), status):
                return True
            else:
                return False
        else:
            synErrComm()
            return False

    elif key == "to":
        if string.find("TO:") != -1:
            if (status == 1 or status == 2):
                if mailComms("forward-path", whiteSpace(string[3:]), status):
                    return True
                else:
                    return False
            else:
                badSeq()
                return False

        else:
            synErrComm()
            return False

    elif key == "DATA":
        if string.split()[0] == "DATA" and string[:4] == "DATA":
            if mailComms("CRLF", whiteSpace(string[4:]), status):
                return True
            else:
                return False
        else:
            synErrComm()
            return False

    elif key == "char":
        atIndex = string.find("@")
        if atIndex != -1:
            if specialCharacters(string[:atIndex]) == True:
                if mailComms("domain", string[atIndex+1:], status):
                    return True
                else:
                    return False
            else:
                synErrPar()
                return False
        else:
            synErrPar()
            return False

    elif key == "string":
        if mailComms("char", string, status):
            return True

    elif key == "whitespace":
        if mailComms("SP", string, status):
            return True
        else:
            return False

    elif key == "path":
        if string.find("<") != -1:
            if mailComms("mailbox", string[1:], status):
                return True
            else:
                return False
        else:
            synErrPar()
            return False

    elif key == "forward-path":
        if mailComms("path", string, status):
            return True
        else:
            return False

    elif key == "reverse-path":
        if mailComms("path", string, status):
            return True
        else:
            return False

    elif key == "domain":
        if mailComms("element", string, status):
            return True

    elif key == "mailbox":
        if mailComms("local-part", string, status):
            return True

    elif key == "local-part":
        if mailComms("string", string, status):
            return True

    elif key == "element":
        endIndex = string.find(">")
        if endIndex != -1:
            if parseDomain(string[:endIndex]) == True:
                if mailComms("CRLF", whiteSpace(string[endIndex+1:]), status):
                    return True
                else:
                    return False
            else:
                synErrPar()
                return False
        else:
            synErrPar()
            return False

    elif key == "CRLF":
        if string == "\r\n" and status == 3:
            startMailWith()
            return True
        elif string =="\r\n":
            okay()
            return True
        else:
            synErrPar()
            return False
    else:
        print("I CANT DO THIS :(!!!!!!")


def writeEmail(message):
    dataInput = ""
    totalMessage = ""
    
    while dataInput != ".\r\n" and dataInput != ".":
        dataInput = stdin.readline()
        if dataInput != ".\r\n":
            totalMessage += dataInput
        if len(dataInput) == 0:
            return False
        if dataInput == ".\r\n":
            print(dataInput + '250 OK',end="\r\n")
        else:
            print(dataInput.rstrip("\n"))

    splitMessage = message.split("\n")
    sender = splitMessage[0][getL(splitMessage[0]):getR(splitMessage[0])+1]
    
    for x in range(1, len(splitMessage)-1):
        fileName = "forward/" + splitMessage[x][getL(splitMessage[x])+1:getR(splitMessage[x])]
        fileWriter = open((fileName), "a")

        fileWriter.write("FROM: " + sender + "\r\n")
        for y in range(1, len(splitMessage) - 1):
            receiver = splitMessage[y][getL(splitMessage[y]):getR(splitMessage[y]) + 1]
            fileWriter.write("TO: " + receiver + "\r\n")
        fileWriter.write(totalMessage)
    return True


input = ""
fullMessage = ""
tempMessage = ""
state = 0

while input != " ":
    fullMessage += tempMessage
    if state == 4:
        writeEmail(fullMessage)
        state = 0
        fullMessage = ""
    input = stdin.readline()

    if len(input)==0:
        break
    else:
        test = input.find("\n")
        if test != -1:
            print (input[:test])
        else:
            print(input.rstrip())
        state, tempMessage = mailComms("start", input, state)
