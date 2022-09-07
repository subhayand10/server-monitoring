import smtplib
from email.message import EmailMessage
import os

# Add your email and app password for this to work.

def email_alert(subject, body, to):

    msg = EmailMessage()
    msg.set_content(body)

    # UPDATE THESE LINES TO YOUR INFO
    gmail_user = 'subhayan.sd10@gmail.com'
    gmail_password = os.environ.get('PASS')
    msg['Subject'] = subject
    msg['From'] = "subhayan.sd10@gmail.com"
    msg['To'] = to


    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.quit()

if __name__ == '__main__':
    email_alert("Test","https://discord.gg/cAWW5qq","subhayan.sd10@gmail.com")