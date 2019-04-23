import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("quinnmentalcounselor@gmail.com", "qwerty@123")
server.sendmail("quinnmentalcounselor@gmail.com","sandraanildas1995@gmail.com","this message is from "+person)
server.quit()