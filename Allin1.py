def add(x,y):
    sum=x+y
    print(sum)

def sub(x,y):
    sub=x-y
    print(sub)    

def mul(x,y):
     mul=x*y
     print(mul)   

def div(x,y):
       div=x/y
       print(div)  

###########################################################################################################################################################       

def cal(w,h):
    h2 = h/100  
    print("Your HEight In Meters Is ; ", h2)
    h3=h2*h2
    bmi=w/h3
    return bmi

def bmi_value(bmi):
    if bmi<=18.5:
        print("You Are Underweight")
    elif bmi >=18 and bmi <=24.9:
        print("You Are Normal Weight")

    elif 29.9<=bmi and bmi <=29.9:
        print("You Are Overweight")
    else:
        print("OBESE")    

####################################################################################################################################################

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def email_sender(receiver,subject,content,image):

    host_mail = 'mohammedsanillm10@gmail.com'
    host_pass = 'omhleissoskvcvix'
    rec_mail = receiver

    msg = MIMEMultipart()
    msg['From'] = host_mail
    msg['To'] = rec_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    with open(image, 'rb') as image_file:
        image_data = image_file.read()
        image = MIMEImage(image_data, name='Photo.jpg')
        msg.attach(image)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(host_mail, host_pass)
    text = msg.as_string()
    server.sendmail(host_mail,rec_mail, text)
    server.quit()
    print("The Email Has Been Sent  Succssfully")

print("Welcome to Email Sender")

#####################################################################################################################################################################

import qrcode
def qr(data,color,bg,filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=0,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color,back_color=bg)
    img.save(f"{filename}.png")
    print("QR Successfully created")


c = True
while c==True:
    print("Welcome To My 4 in 1 App")
    option=input("What DO You Want This Program To Do??\n1.Calculator\n2.BMI Checker\n3.Email Sender\n4.QR Generator\nEnter Your Option :")
    print("You Have Choosed Option :",option)

    if option=='1':

        print("Thi Is Calculator")

        x = float(input("Enter 1st number:"))
        y = float(input("Enter 2nd number:"))

        print("Choose an option: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        option =int(input("Choose an option:"))

        if option == 1:
            add(x,y)
        elif option == 2:
            sub(x,y)
        elif option == 3:
            mul(x,y)

        elif option == 4:
            div(x,y)    
        else:
            print("OK")   
            
    if option == '2':

        w=float(input("Enter You Weight(in KG)"))
        h=float(input("Enter your height(in CM)"))
        bmi= cal(w,h)
        print(bmi)
        bmi_value(bmi)

    if option == '3':
        con = 'no' #initialisation

        while con=='no': #condition
            receiver = input("Enter The Reciever's Mail ID")
            subject = input("Enter The Subject")
            content = input("What Do You Wanna Say?")
            image = input("Enter Image Path")
            print("Confirm Details :")
            print("Reciever's Mail :",receiver)
            print("Subject : ",subject)
            print("Content : ",content)

            confirm = input("Send ??\nType: 'yes'/'no'")
            if confirm== 'yes' :
                email_sender(receiver,subject,content,image)
                break #breaks while loop
            elif confirm== 'no':
                con = 'no' #again gets into loop
            else:
                con='no'
                
    if option == '4':
        
        data = input("Enter The Content To Put Inside Qr")   
        color = input("Enter The color for Qr")
        bg = input("Enter the color for bg")
        filename = input("Enter the name for the Qr")
        qr(data,color,bg,filename)       

    else:
          
        other=input("Do you want to Try again?\nYes or No")  
        if other ==  'yes':
            c = True
        else:
            c = False    