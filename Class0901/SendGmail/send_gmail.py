import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# Please go to "mypassword.py" to change your password
from mypassword import gmailPassword

gmailUser = 'andrewteng0627@gmail.com'
recipients = [gmailUser, 'angeldan0627@gmail.com', 'a0922737762@gmail.com']

# Send this script to all receivers
filename = "send_gmail.py"
with open(filename, "rb") as f:
    message = f.read()

msg = MIMEMultipart()
msg['From'] = gmailUser
msg['To'] = ", ".join(recipients)
msg['Subject'] = "My python email script!"
msg.attach(MIMEText(message))

# Establish a connection to the gmail esmtp server
mailServer = smtplib.SMTP('smtp.gmail.com', 587)
# Identify ourselves to esmtp gmail client (ESMTP (Extended SMTP) is more secure)
mailServer.ehlo()
# Secure our email with TLS (Transport Layer Security) encryption
mailServer.starttls()
# Re-identify ourselves as an encrypted connection
mailServer.ehlo()
# Login to the gmail services
mailServer.login(gmailUser, gmailPassword)
# Send your email!
mailServer.sendmail(gmailUser, recipients, msg.as_string())
mailServer.quit()
