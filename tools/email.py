import smtplib
from email.mime.text import MIMEText

class SenderEmail:
    
    def __init__(self, sender_email, password):
        self.sender = sender_email
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(sender_email, password)
        
    def send_template(self, template_path: str, to_email, subject = None):
        with open(template_path) as file:
            template = file.read()
            
        msg = MIMEText(template, 'html')
        msg['Subject'] = subject if subject else f'{self.sender}'
        msg['From'] = self.sender
        msg['To'] = to_email
        
        self.server.sendmail(self.sender, to_email, msg.as_string())
        
    def sends_templates(self, template_path: str, to_emails: list, subject = None):
        with open(template_path) as file:
            template = file.read()
           
        msg = MIMEText(template, 'html')
        msg['Subject'] = subject if subject else f'{self.sender}'
        msg['From'] = self.sender
        for email in to_emails:
            try:
                msg['To'] = email
                self.server.sendmail(self.sender, email, msg.as_string())
                
            except: ...
        
