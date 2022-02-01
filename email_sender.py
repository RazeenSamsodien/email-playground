import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andre Neagoie'
email['to'] = 'razeensamsodien@gmail.com'
email['subject'] = 'You won a 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Patrick Bateman'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('razeensamsodien@gmail.com', 'deiztjkoqtrijuii')
    smtp.send_message(email)
    print('all good boss')