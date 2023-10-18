

host_mail = 'mohammedsanillm10@gmail.com'
host_pass = 'omhleissoskvcvix'
rec_mail = input("Enter The Recieving Mail ID")
subject = input("Enter Your Content To Be Sent")
msg = MIMEMultipart()
msg['From'] = host_mail
msg['To'] = rec_mail
msg['Subject'] = subject
msg.attach(MIMEText("...", 'plain'))
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(host_mail, host_pass)
text = msg.as_string()
server.sendmail(host_mail,rec_mail, text)
server.quit()





print("Email Has beeen sented succesfully")