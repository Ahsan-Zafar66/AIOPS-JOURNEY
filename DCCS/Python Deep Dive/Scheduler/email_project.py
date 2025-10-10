# MIME: multipurpose internet mail extensions

import smtplib
# for message
from email.mime.multipart import MIMEMultipart

# for text
from email.mime.text import MIMEText

# for files attachment
from email.mime.base import MIMEBase

# for image or logo
from email.mime.image import MIMEImage

# for security
from email import encoders

import schedule

import time






# sceduling an email to send ata a specific time







def email_send():
    file_path = r"D:\AIOPS\DCCS\Python Deep Dive\Email Module\myattachment.txt"

    # initiating mimemultipart
    msg_mime = MIMEMultipart()


    # my mail on google
    my_mail = "ahsanzafar0501@gmail.com"

    # mail to which message will be send
    to_mail = "ahsanzafarqau@gmail.com"
    # my app password set in my google account
    my_pswd = "kvwiqfvfpdatvvrn"

    # setting mail subject
    msg_mime["SUBJECT"] = "Mail Using Email Module"

    # sending mail
    msg_mime["From"] = my_mail

    # recieving mail
    msg_mime["To"] = to_mail

    # send me back this mail
    msg_mime["Cc"] = my_mail

    # attaching image as logo in the text
    # text_body = """"
    # <html> </b> <p> Hi! this mail is sending theough MIME at 11:19pm 
    # <img src= "cid:<alogo>"
    # </b> </p> </html>
    # """

    text_body = """
    <html>
    <body>
    <p>Hi! This mail is being sent through MIME at 11:19 PM.</p>
    <img src="cid:alogo" style="width:300px; height:auto;" />
    </body>
    </html>
    """


    # attaching text
    msg_mime.attach(MIMEText(text_body,"html"))


    # attaching my logo
    logo_path = r"D:\AIOPS\DCCS\Python Deep Dive\Email Module\Ahsan Zafar (1)_page-0001.jpg"
    logo_file = open(logo_path,"rb")
    msgIMAGE = MIMEImage(logo_file.read())
    msgIMAGE.add_header("Content-ID","<alogo>")
    msg_mime.attach(msgIMAGE)



    # attachment of files 

    # open the file using rb
    attachment = open(file_path,"rb")

    # initiate the mimebase with maintype and subtype
    part = MIMEBase("application","octet-stream")

    # set the payload of the content of the file to send
    part.set_payload((attachment).read())

    # attach encoders for security
    encoders.encode_base64(part)

    # add the header as it needs to be aatached and give file path
    part.add_header("Content-Disposition",f"attachment; filename={file_path}")

    # now attach the processed part mimebase with the message
    msg_mime.attach(part)

    # smtp mail of google.com
    connection = smtplib.SMTP("smtp.gmail.com",587)

    # starting transport layer , TLS: transport layer security
    connection.starttls()




    # logging in the account
    connection.login(user=my_mail,password=my_pswd)

    # senign the message
    connection.send_message(msg_mime)

    # closing the connection
    connection.close()




    # scheduling above function to run every friday at 3 pm
friday= schedule.every().friday.at("17:13:00").do(email_send)

# now we need to call the schedule inside a while loop with a true condition
while True:
    schedule.run_pending()
    time.sleep(1)
    False

