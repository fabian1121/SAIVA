import smtplib
from email.message import EmailMessage
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import imghdr
import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import filedialog
from SpeakFunction import speak
from ListenFunction import *

username = "218fabian0050@dbit.in"
password = "Fabian@dbit"

attachments = []
def attachFile():
    filename = filedialog.askopenfilename()
    attachments.append(filename)

def sendEmail():
    try:
        #The mail addresses and password
        sender_address = username
        sender_pass = password
        receiver_address = []
        speak("Is there a single or multiple recipients for this Email?")
        com = TakeCommand().lower()
        if 'multiple' in com:
            speak("How many recipients?")
            num = input()
            for i in range(num):
                receiver_address.append(input("Enter Recipient " + i +" Email: "))
        else:
            receiver_address.append(input("Enter Recipient Email: "))
        
        #Setup the MIME
        message = EmailMessage()
        message['From'] = sender_address
        message['To'] = receiver_address
        speak("What is the subject of this Email")
        subject = TakeCommand()
        message['Subject'] = subject
        #The subject line
        #The body and the attachments for the mail
        speak("What is the body of this Email")
        mail_content = TakeCommand()
        message.set_content(mail_content)
        speak("Do you want to attach a file?")
        ans = TakeCommand().lower()
        if 'yes' in ans:
            speak("How many files do u want to attach?")
            attach = int(input())
            for i in range(attach):
                attachFile()
            for filename in attachments:
                filetype = filename.split('.')
                filetype = filetype[1]
                if filetype == 'JPG' or filetype == 'jpg' or filetype == 'PNG' or filetype == 'png' or filetype == 'JPEG' or filetype == 'jpeg':
                    with open(filename, 'rb') as f:
                        file_data = f.read()
                        file_type = imghdr.what(f.name)
                        file_name = f.name.split("/")[-1]
                    message.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
                else:
                    with open(filename, 'rb') as f:
                        file_data = f.read()
                        file_name = f.name.split("/")[-1]
                    message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        speak('Mail Sent')        
    except Exception as e:
        print(e)
        speak("Unable to send Email")
            

def readEmail():
    # account credentials

    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = int(messages[0])
    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                speak("Subject:"+ subject)
                speak("From:"+ From)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            speak(body)
                        elif "attachment" in content_disposition:
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        speak(body)
                if content_type == "text/html":
                    # if it's HTML, create a new HTML file and open it in browser
                    folder_name = clean(subject)
                    if not os.path.isdir(folder_name):
                        # make a folder for this email (named after the subject)
                        os.mkdir(folder_name)
                    filename = "index.html"
                    filepath = os.path.join(folder_name, filename)
                    # write the file
                    open(filepath, "w").write(body)
                    # open in the default browser
                    webbrowser.open(filepath)
                print("="*100)
    # close the connection and logout
    imap.close()
    imap.logout()

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

def emailOptions():
    speak("What do you want to do?")
    option = TakeCommand().lower()
    if 'compose' in option:
        sendEmail()
    elif 'read' in option:
        readEmail()

#emailOptions()