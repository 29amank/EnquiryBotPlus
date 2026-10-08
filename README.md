# EnquiryBotPlus

A simple Python command-line enquiry bot. It asks for a customer's name, phone number, email address, and enquiry type; records the contact details in a local CSV; and sends the enquiry by SMTP email.

> **Status:** Small demonstration project. It has not been independently tested or reviewed for production use. Treat captured contact details as personal data.

## Requirements

- Python 3
- Network and SMTP access to the configured email service
- `python-dotenv` (see `requirements.txt`)

## Local setup

```bash
git clone https://github.com/29amank/EnquiryBotPlus.git
cd EnquiryBotPlus
python -m venv .venv
```

Activate the virtual environment:

- **Windows PowerShell:** `.venv\Scripts\Activate.ps1`
- **Linux/macOS:** `source .venv/bin/activate`

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and provide real values:

```dotenv
SENDER_EMAIL=your-sender@example.com
RECIPIENT_EMAIL=your-recipient@example.com
EMAIL_PASSWORD=your-email-service-app-credential
```

The current implementation uses `smtp.gmail.com` on port 587 (STARTTLS). For Gmail, an appropriate app-specific password or other supported SMTP authentication method may be required depending on account policies.

Run:

```bash
python enquiry_bot.py
```

## What the program does

1. Offers a short list of product or service enquiry categories.
2. Collects the visitor's name, ten-digit phone number, and email address.
3. Appends contact details to a local `customer_details.csv` file.
4. Tries to send the enquiry to the configured recipient by email.

## Data and configuration safety

- `.env` and `customer_details.csv` are ignored by Git through `.gitignore`; **do not commit real customer records or credentials**.
- Restrict local access to the CSV file, get suitable consent to collect/share data, and define retention/deletion procedures before real use.
- `.gitignore` only prevents *future untracked* files being added by default. If credentials or customer records were previously committed, remove them from history as appropriate and rotate exposed credentials.
- This project has no current automated test suite; SMTP delivery, input handling, privacy, and error handling need further review before deployment.

## Repository maintenance

The repository contains the source file `enquiry_bot.py`, the dependency manifest, and a safe environment template. Add tests and improve configuration validation before expanding the application.

## License

**No license file is currently included.** Do not assume a license has been granted; the repository owner should select and add one if distribution or reuse is intended.
