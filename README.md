# EnquiryBotPlus

EnquiryBotPlus is a Python-based bot that assists users in making inquiries about various products or services. It collects user details, prompts them for the purpose of their inquiry, displays available products/services, and sends the inquiry via email to a designated recipient.

## Features

- Collects user details including name, phone number, and email address.
- Allows users to select the purpose of their inquiry from a list of available options.
- Displays information about available products/services based on user selection.
- Sends the inquiry details via email to a designated recipient.

## Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the project root directory.
   - Add the following variables to the `.env` file:
     ```
     SENDER_EMAIL=<your_sender_email>
     RECIPIENT_EMAIL=<your_recipient_email>
     EMAIL_PASSWORD=<your_email_password>
     ```

4. Run the EnquiryBot:

   ```bash
   python enquiry_bot.py
   ```

5. Follow the on-screen prompts to interact with the EnquiryBot.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to use this content by copying and pasting it into your README.md file in your project repository.
