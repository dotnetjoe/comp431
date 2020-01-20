from sys import stdin
import os

def checkMail(mail):
    if mail == "MAIL" or mail == "mail":
        return True
    else:
        return False

def checkFrom(fromInput):
    if fromInput == "FROM:" or fromInput == "from:":
        return True
    else:
        return False

def specialCharacters(str):
    for x in str:
        if (x == '<' or x == '>' or x=='(' or x == ')' or x =='[' or x == ']' or x == '\\' or x == '.' or x == ',' or x == ';' or x == ':' or x == '@' or x == " " or x == "\t" ):
            return False
    return True

def letters(domain):
    for x in domain:
        if x.isalpha() == False :
            return False
    return True

def numbers(domain):
    for x in domain:
        if x.isdigit() == False :
            return False
    return True

def checkDomain(domain):
    for characters in domain:
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
        if x != ' ' and x != '\t' and x != '\s':
            return string[index:]
        index += 1


def findLeft(string):
    return string.find("<")

def findRight(string):
    return string.find(">")


def mailCommands(token, string, status):
    if token == "start":
        if checkMail(string[:4]) and checkMail(string.split()[0]):
            if mailCommands("mail", string, status): # guarantees message is all okay
                return 1, string
            else:
                return status, ""



        elif string[:4] == "RCPT":

                if mailCommands("RCPT", string, status):
                    return 2, string
                else:
                    return status, ""

        elif string[:4] == "DATA":
            if status == 2 :
                if mailCommands("DATA", string, 3):
                    return 4, ""
                else:
                    return status, ""
            else:
                print ("503 Bad sequence of commands")
                return status, ""
        else:
            print("500 Syntax error: command unrecognized")
            return status, ""

    elif token == "mail":
        if checkMail(string[:4]) and checkMail(string.split()[0]):
            if mailCommands("from", whiteSpace(string[4:]), status):
                return True
            else:
                return False
        else:
            print("500 Syntax error: command unrecognized")
            return False

    elif token == "from":
        if string.find("from:") != -1 or string.find("FROM:") != -1:
            if status == 0 or status == 4:
                if mailCommands("reverse-path", whiteSpace(string[5:]), status):
                    return True
                else:
                    return False
            else:
                print ("503 Bad sequence of commands")
                return False
        else:
            print("500 Syntax error: command unrecognized")
            return False


    elif token == "RCPT":
        if string[:4] == "RCPT" and string.split()[0] == "RCPT":
            if mailCommands("to", whiteSpace(string[4:]), status):
                return True
            else:
                return False
        else:
            print("500 Syntax error: command unrecognized")
            return False

    elif token == "to":
        if string.find("TO:") != -1:
            if (status == 1 or status == 2):
                if mailCommands("forward-path", whiteSpace(string[3:]), status):
                    return True
                else:
                    return False
            else:
                print ("503 Bad sequence of commands")
                return False

        else:
            print("500 Syntax error: command unrecognized")
            return False

    elif token == "DATA":
        if string.split()[0] == "DATA" and string[:4] == "DATA":
            if mailCommands("CRLF", whiteSpace(string[4:]), status):
                return True
            else:
                return False
        else:
            print("500 Syntax error: command unrecognized")
            return False


    elif token == "whitespace":
        if mailCommands("SP", string, status):
            return True
        else:
            return False

    elif token == "reverse-path":
        if mailCommands("path", string, status):
            return True
        else:
            return False

    elif token == "forward-path":
        if mailCommands("path", string, status):
            return True
        else:
            return False

    elif token == "path":
        if string.find("<") != -1:
            if mailCommands("mailbox", string[1:], status):
                return True
            else:
                return False
        else:
            print ("501 Syntax error in parameters or arguments")
            return False


    elif token == "mailbox":
        if mailCommands("local-part", string, status):
            return True


    elif token == "local-part":
        if mailCommands("string", string, status):
            return True



    elif token == "string":
        if mailCommands("char", string, status):
            return True



    elif token == "char":
        atPos = string.find("@")
        if atPos != -1:
            if specialCharacters(string[:atPos]) == True:
                if mailCommands("domain", string[atPos+1:], status):
                    return True
                else:
                    return False
            else:
                print("501 Syntax error in parameters or arguments")
                return False
        else:
            print ("501 Syntax error in parameters or arguments")
            return False

    elif token == "domain":
        if mailCommands("element", string, status):
            return True

    elif token == "element":
        endPos = string.find(">")
        if endPos != -1:
            if checkDomain(string[:endPos]) == True:
                if mailCommands("CRLF", whiteSpace(string[endPos+1:]), status):
                    return True
                else:
                    return False
            else:
                print ("501 Syntax error in parameters or arguments")
                return False
        else:
            print ("501 Syntax error in parameters or arguments")
            return False

    elif token == "CRLF":
        if string == "\n" and status == 3:
            print ("503 Bad sequence of commands")
            return True
        elif string =="\n":
            print ("250 OK")
            return True
        else:
            print ("501 Syntax error in parameters or arguments")
            return False
    else:
        print("helpme")


def writeEmail(message):
    dataInput = ""
    totalMessage = ""
    while dataInput != ".\n" and dataInput != ".":
        dataInput = stdin.readline()
        if dataInput != ".\n":
            totalMessage += dataInput
        if len(dataInput) == 0:
            return False
        if dataInput == ".\n":
            print(dataInput + '250 OK')
        else:
            print(dataInput.rstrip("\n"))
    splitMessage = message.split("\n")
    sender = splitMessage[0][findLeft(splitMessage[0]):findRight(splitMessage[0])+1]
    for x in range(1, len(splitMessage)-1):
        fileName = "forward/" + splitMessage[x][findLeft(splitMessage[x])+1:findRight(splitMessage[x])]
        fileWriter = open((fileName), "a")

        fileWriter.write("From: " + sender + "\n")
        for y in range(1, len(splitMessage) - 1):
            receiver = splitMessage[y][findLeft(splitMessage[y]):findRight(splitMessage[y]) + 1]
            fileWriter.write("To: " + receiver+ "\n")
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
        state, tempMessage = mailCommands("start", input, state)
