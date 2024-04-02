import csv
import smtplib
import re
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class EnquiryBot:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.services = {
            "1": {"name": "Control Panels", "overview": "Our control panels are designed to meet the highest standards of quality and reliability."},
            "2": {"name": "Consultancy Services", "overview": "Our consultancy services provide expert guidance and support for your projects."},
            "3": {"name": "Other Products", "overview": "We offer a variety of other products to meet your specific needs."}
        }
        self.customer_file = "customer_details.csv"  # File to store customer details
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.receiver_email = os.getenv('RECIPIENT_EMAIL')
        self.email_password = os.getenv('EMAIL_PASSWORD')

    def greet_customer(self):
        print("Welcome to our Enquiry Bot service! How can I assist you today?")

    def get_user_details(self):
        name = input("May I have your name? ")
        number = self.get_valid_phone_number()
        email = self.get_valid_email()
        return name, number, email

    def get_valid_phone_number(self):
        while True:
            number = input("Can you please provide your phone number? ")
            if re.match(r'^\d{10}$', number):
                return number
            else:
                print("Invalid phone number format. Please enter a 10-digit phone number.")

    def get_valid_email(self):
        while True:
            email = input("What is your email address? ")
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return email
            else:
                print("Invalid email address format. Please enter a valid email address.")

    def ask_purpose(self):
        print("What is the purpose of your inquiry?")
        for key, value in self.services.items():
            print(f"{key}. {value['name']}")
        choice = input("Enter the number corresponding to your purpose: ")
        return choice

    def display_products(self, purpose):
        if purpose in self.services:
            print(f"Available {self.services[purpose]['name']}:")
            print(self.services[purpose]['overview'])
        else:
            print("Invalid purpose selected.")

    def ask_requirements(self):
        choice = input("Enter the number corresponding to the desired product or customization: ")
        return choice

    def retrieve_information(self, product_choice):
        if product_choice in self.services:
            return self.services[product_choice]['overview']
        else:
            return "Invalid product choice."

    def store_customer_details(self, name, number, email):
        with open(self.customer_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, number, email])

    def send_email(self, name, number, email, query):
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.receiver_email
        message['Subject'] = 'Customer Query'

        body = f"Name: {name}\nNumber: {number}\nEmail: {email}\nQuery: {query}"
        message.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.email_password)
                server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print("Your query has been emailed to our team.")
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")

    def start(self):
        self.greet_customer()

        name, number, email = self.get_user_details()

        purpose_choice = self.ask_purpose()
        self.display_products(purpose_choice)

        product_choice = self.ask_requirements()
        information = self.retrieve_information(product_choice)

        print("\nThank you for your inquiry, {}! Here is the information you requested:\n{}".format(name, information))

        # Store customer details
        self.store_customer_details(name, number, email)

        # Send email with customer query
        query = f"Purpose: {purpose_choice}, Product: {product_choice}"
        self.send_email(name, number, email, query)


if __name__ == "__main__":
    chatbot = EnquiryBot()
    chatbot.start()
