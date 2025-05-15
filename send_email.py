import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "rtlhpqyhqvkojdzw"
SENDER = "manishkumaryadav2177@gmail.com"
RECEIVER = "manishkumaryadav2177@gmail.com"
  # Use an app password if using Gmail

def send_email(image_paths):
    email_message = EmailMessage()
    email_message["Subject"] = "Captured Images"
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content("Motion detected. See attached images.")

    for image_path in image_paths:  # Loop over each file path
        with open(image_path, "rb") as file:
            content = file.read()
            file_type = imghdr.what(file.name)
            file_name = file.name
        email_message.add_attachment(content, maintype="image", subtype=file_type, filename=file_name)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(SENDER, PASSWORD)
        smtp.send_message(email_message)
