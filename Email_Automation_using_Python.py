# Import the 'pandas' library and alias it as 'pd'
import pandas as pd

# Read data from a CSV file named 'file_name.csv' and store it in the 'data' DataFrame
data = pd.read_csv( "#file_name.csv" )

# Display the 'data' DataFrame
data

# Function to send an email
def send_mail(email):

  # Email content
  email_content="""<p>
  Write the content here.
  </p>"""

  # Sender's email address and password (Note: Avoid storing sensitive information directly in code)
  sender_address="#your_email"
  sender_password = "#email_password"

  # Receiver's email address
  receiver_address = email

  # Create a message object
  message = MIMEMultipart()

  # Set sender, receiver, and subject
  message["From"] = "#Your_name <#your_email>"
  message["To"] = receiver_address
  message["Subject"] = "#Write the subject of the mail"

  # Attach the email content as HTML
  message.attach (MIMEText (email_content, "html"))

  # Connect to the SMTP server and send the email
  session = smtplib.SMTP("smtp.gmail.com", 587)
  session.starttls()
  session.login(sender_address, sender_password)
  text = message.as_string()
  session.sendmail("#Your_email" +str(sender_address), receiver_address, text)

  # Close the SMTP session and print a confirmation message
  session.quit()
  print("Mail sent to", receiver_address)

# Import necessary libraries for sending emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Assuming 'data' is a DataFrame containing recipient information

# Iterate through each row in the 'data' DataFrame
for i in data.iterrows():

  # Extract the email address from the current row
  email=i[1]["Email"]

  # Print the email address (for debugging or monitoring purposes)
  print(email)

  # Call a function to send an email to the extracted email address
  send_mail(email)
