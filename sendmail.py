import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login("quinnmentalcounselor", "qwerty@123")
server.sendmail("quinnmentalcounselor@gmail.com","koolsand1995@gmail.com","User is having suicidal thoughts")
server.quit()