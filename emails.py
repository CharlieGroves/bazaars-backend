# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from hashlib import new
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email='ctrg04@gmail.com',
#     to_emails='charlie.groves@coopersschool.com',
#     subject='Test email for online shop',
#     html_content='<strong>Test of HTML tags inside of email</strong>')
# try:
#     sg = SendGridAPIClient("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")
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

def sendRecommendationEmail(email, recommendation, percentage):
    percentage = int(percentage)
    new_price = recommendation["recomms"][0]["values"]["itemPrice"]*(1 - (percentage/100))
    message = Mail(
        from_email='ctrg04@gmail.com',
        to_emails=email,
        subject='A special offer just for YOU',
        html_content="<h1>{title}</h1><img src={image}/><br/><h3>For just <s>£{oldPrice}</s> £{price} - {percentage}% off!</h3>".format(
            title = recommendation["recomms"][0]["values"]["itemName"], 
            oldPrice = recommendation["recomms"][0]["values"]["itemPrice"] , 
            price = int(new_price), percentage=percentage, 
            image = recommendation["recomms"][0]["values"]["itemImageURL"]))

    sg = SendGridAPIClient("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")
    sg.send(message)