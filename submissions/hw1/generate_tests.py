# 1) Example well-formed sequence (from assignment writeup)
with open("in1.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

with open("out1.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 2) Another simple well-formed sequence with different email addresses
with open("in2.txt", "w") as f:
    f.write(
        "MAIL FROM: <email1@gmail.com>\r\n"
        "RCPT TO: <firstname_lastname@gmail.com>\r\n"
        "DATA\r\n"
        "message body\r\n"
        ".\r\n"
    )

with open("out2.txt", "w") as f:
    f.write(
        "MAIL FROM: <email1@gmail.com>\r\n"
        "250 OK\r\n"
        "RCPT TO: <firstname_lastname@gmail.com>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "message body\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 3) Two well-formed emails in one sequence
with open("in3.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL FROM: <email1@gmail.com>\r\n"
        "RCPT TO: <firstname_lastname@gmail.com>\r\n"
        "DATA\r\n"
        "message body\r\n"
        ".\r\n"
    )

with open("out3.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
        "MAIL FROM: <email1@gmail.com>\r\n"
        "250 OK\r\n"
        "RCPT TO: <firstname_lastname@gmail.com>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "message body\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 4) First 500 error example (from assignment writeup)
with open("in4.txt", "w") as f:
    f.write("MAILFROM: <jasleen@cs.unc.edu>\r\n")

with open("out4.txt", "w") as f:
    f.write(
        "MAILFROM: <jasleen@cs.unc.edu>\r\n"
        "500 Syntax error: command unrecognized\r\n"
    )

# 5) Second 500 error example (from assignment writeup)
with open("in5.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO : < ivysat@cs.unc.edu>\r\n"
    )


with open("out5.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT TO : < ivysat@cs.unc.edu>\r\n"
        "500 Syntax error: command unrecognized\r\n"
    )

# 6) First 501 error example (from assignment writeup)
with open("in6.txt", "w") as f:
    f.write("MAIL   FROM: <jasleen @cs.unc.edu>\r\n")

with open("out6.txt", "w") as f:
    f.write(
        "MAIL   FROM: <jasleen @cs.unc.edu>\r\n"
        "501 Syntax error in parameters or arguments\r\n"
    )

# 7) Second 501 error example (from assignment writeup)
with open("in7.txt", "w") as f:
    f.write("MAIL FROM: < ivysat@cs.unc.edu\r\n")

with open("out7.txt", "w") as f:
    f.write(
        "MAIL FROM: < ivysat@cs.unc.edu\r\n"
        "501 Syntax error in parameters or arguments\r\n"
    )

# 8) 500 error taking precedence over 501 errors (from assignment writeup)
with open("in8.txt", "w") as f:
    f.write("MAILFROM: <jasleen @cs.unc.edu>\r\n")

with open("out8.txt", "w") as f:
    f.write(
        "MAILFROM: <jasleen @cs.unc.edu>\r\n"
        "500 Syntax error: command unrecognized\r\n"
    )

# 9) 503 error taking precedence over 501 errors
with open("in9.txt", "w") as f:
    f.write("RCPT TO: <smithfdcs.unc.edu>\r\n")

with open("out9.txt", "w") as f:
    f.write(
        "RCPT TO: <smithfdcs.unc.edu>\r\n"
        "503 Bad sequence of commands\r\n"
    )

# 10) Simple 503 error with DATA coming before RCPT TO
with open("in10.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "DATA\r\n"
    )

with open("out10.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "503 Bad sequence of commands\r\n"
    )

# 11) Example with sequence continuing after a 500 error
with open("in11.txt", "w") as f:
    f.write(
        "MAILFROM: <jasleen@cs.unc.edu>\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

with open("out11.txt", "w") as f:
    f.write(
        "MAILFROM: <jasleen@cs.unc.edu>\r\n"
        "500 Syntax error: command unrecognized\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 12) Example with sequence continuing after a 501 error
with open("in12.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

with open("out12.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT TO: <smithfd@cs.unc.edu\r\n"
        "501 Syntax error in parameters or arguments\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 13) Example with sequence continuing after a 503 error
with open("in13.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "DATA\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

with open("out13.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "503 Bad sequence of commands\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 14) Example with multiple spaces and tabs in SMTP commands
with open("in14.txt", "w") as f:
    f.write(
        "MAIL   FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT	TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

with open("out14.txt", "w") as f:
    f.write(
        "MAIL   FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT	TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# 15) Ill-formed sequence where EOF is reached before end of data
with open("in15.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
    )

with open("out15.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "250 OK\r\n"
        "DATA\r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
    )

# 16) Well-formed sequence with spaces and tabs after SMTP commands
with open("in16.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>  \r\n"
        "RCPT TO: <smithfd@cs.unc.edu>	\r\n"
        "DATA  \r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

with open("out16.txt", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>  \r\n"
        "250 OK\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>	\r\n"
        "250 OK\r\n"
        "DATA  \r\n"
        "354 Start mail input; end with . on a line by itself\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "250 OK\r\n"
    )

# expected contents of forward/<smithfd@cs.unc.edu>
with open("<smithfd@cs.unc.edu>", "w") as f:
    f.write(
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL   FROM: <jasleen@cs.unc.edu>\r\n"
        "RCPT	TO: <smithfd@cs.unc.edu>\r\n"
        "DATA\r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
        "MAIL FROM: <jasleen@cs.unc.edu>  \r\n"
        "RCPT TO: <smithfd@cs.unc.edu>	\r\n"
        "DATA  \r\n"
        "Hey Don, do you really think we should use SMTP as a class\r\n"
        "project in COMP 431 this year? The smart students are going to\r\n"
        "figure out automated ways to use this project to send\r\n"
        "anonymous SPAM to the world!\r\n"
        ".\r\n"
    )

# expected contents of forward/<firstname_lastname@gmail.com>
with open("<firstname_lastname@gmail.com>", "w") as f:
    f.write(
        "MAIL FROM: <email1@gmail.com>\r\n"
        "RCPT TO: <firstname_lastname@gmail.com>\r\n"
        "DATA\r\n"
        "message body\r\n"
        ".\r\n"
        "MAIL FROM: <email1@gmail.com>\r\n"
        "RCPT TO: <firstname_lastname@gmail.com>\r\n"
        "DATA\r\n"
        "message body\r\n"
        ".\r\n"
    )

