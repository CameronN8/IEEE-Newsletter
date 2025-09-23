import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(subject, body, to_emails):
    # Your Gmail credentials
    from_email = "___@clemson.edu"
    password = "___"

    to_emails_str = ", ".join(to_emails)


    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_emails_str
    msg['Subject'] = subject

    # Attach the HTML body
    msg.attach(MIMEText(body, 'html'))

    try:
        # Establish a connection with Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(from_email, password)  # Log in to Gmail

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
subject = "Test HTML Email"
body = """
<html>
  <body>
    <h1>Hello, World!</h1>
    <p>This is a test email with <strong>HTML content</strong>.</p>
    <p>Enjoy sending HTML emails using Python!</p>
  </body>
</html>
"""
to_email = ["recipient1@clemson.edu", "recipient2@clemson.edu"]

send_html_email(subject, body, to_email)
