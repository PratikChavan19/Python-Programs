import smtplib

sender = "chavanpratik017@gmail.com"    # senders mail id
receiver = "nikamnivedita27@gmail.com" #receivers mail id
password = "szop dnom vwyr zwzy"    #password for log in

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)   # server address and port number
smtp_server.ehlo()  # setting protocol 

smtp_server.starttls()  #setting up TLS connection
smtp_server.ehlo() # encryption happens on calling starttls()

smtp_server.login(sender, password) # logging in

message = '''Zala code....
THANK YOU....'''

smtp_server.sendmail(sender, receiver, message)
print("Successfully the email is sent")

smtp_server.quit()