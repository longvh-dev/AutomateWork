
# Sending Personalized Emails
def send_personalized_email(sender_info, recipients, subject, body):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_info.email, sender_info.password)
    for recipient_email in recipients:
        message = MIMEMultipart()
        message['From'] = sender_info.email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(sender_info.email, recipient_email, message.as_string())
    server.quit()


# Emailing File Attachments
def send_email_with_attachment(sender_info, recipient_email, subject, body, file_path):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    from email.mime.text import MIMEText

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_info.email, sender_info.password)

    message = MIMEMultipart()
    message['From'] = sender_info.email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with open(file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {file_path}")
        message.attach(part)
        server.sendmail(sender_info.email, recipient_email, message.as_string())
    server.quit()


# Automatic Email Reminder
def send_reminder_email(sender_info, recipient_email, subject, body, reminder_date):
    import smtplib
    from email.mime.text import MIMEText
    from datetime import datetime

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_info.email, sender_info.password)
    now = datetime.now()
    reminder_date = datetime.strptime(reminder_date, '%Y-%m-%d')

    if now.date() != reminder_date.date():
        message = MIMEText(body, 'plain')
        message['From'] = sender_info.email
        message['To'] = recipient_email
        message['Subject'] = subject
        server.sendmail(sender_info.email, recipient_email, message.as_string())

    server.quit()
