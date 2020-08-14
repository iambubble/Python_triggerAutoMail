import smtplib

smtpObj =smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('myusername','myp@ssw@rd')
smtpObj.sendmail('sender.mailid@exp.com', 'receiver.maillid@exp.com','mysubject')
smtpObj.quit()