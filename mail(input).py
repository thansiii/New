import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def email_sender(receiver,subject,content):

    host_mail = 'mohammedsanillm10@gmail.com'
    host_pass = 'omhleissoskvcvix'
    rec_mail = receiver

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
    print("The Email Has Been Sent Succssfully")

print("Welcome to Email Sender")

con = 'no'

while con=='no':
    receiver = input("Enter The Reciever's Mail ID")
    subject = input("Enter The Subject")
    content = input("What Do You Wanna Say?")

    print("Confirm Details :")
    print("Reciever's Mail :",receiver)
    print("Subject : ",subject)
    print("Content : ",content)

    confirm = input("Send ??\nType: 'yes'/'no'")
    if confirm== 'yes' :
        email_sender(receiver,subject,content)
        break #breaks while loop
    elif confirm== 'no':
        con = 'no' #again gets into loop
    else:
        con='no'
            