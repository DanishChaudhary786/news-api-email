import smtplib, ssl

host = "smtp.gmail.com"
port = 465
sender_email = "danish.twilio@gmail.com"
sender_pass = "afmbdbtjakbmymeb"
context = ssl.create_default_context()
def sending_email(receiver_email, receiver_message):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, sender_pass)
        server.sendmail(sender_email, receiver_email, receiver_message)
        print("email sent")
