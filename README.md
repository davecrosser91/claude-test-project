# Claude Test Project

This project demonstrates how to use the Twilio API with Python.

## Twilio

Twilio is a cloud communications platform that provides programmable communication tools for making and receiving phone calls, sending and receiving text messages, and performing other communication functions using its web service APIs.

### What Twilio Can Be Used For

Twilio enables developers to integrate various communication features into their applications:

- **SMS Messaging**: Send and receive text messages programmatically
- **Voice Calls**: Make and receive phone calls with custom call flows
- **Video Communication**: Build video chat applications with Twilio Video
- **WhatsApp Integration**: Send and receive WhatsApp messages through the WhatsApp Business API
- **Email**: Send transactional and marketing emails via SendGrid (a Twilio company)
- **Two-Factor Authentication**: Implement secure 2FA and phone verification
- **Notifications**: Send alerts and notifications via SMS, voice, or push notifications
- **Contact Centers**: Build custom call centers and IVR systems
- **Chat Applications**: Create in-app messaging features

## Twilio API Information

The Twilio API is a RESTful API that allows developers to interact with Twilio's communication services. Key features include:

- **REST Architecture**: Simple HTTP requests for all operations
- **Authentication**: Secure API authentication using Account SID and Auth Token
- **SDKs Available**: Official libraries for Python, Node.js, PHP, Ruby, Java, C#, and more
- **Webhooks**: Real-time event notifications via HTTP callbacks
- **Test Credentials**: Free test mode for development without charges
- **Comprehensive Documentation**: Detailed API reference and code examples

### Getting Started with Twilio

1. Sign up for a free Twilio account at [twilio.com](https://www.twilio.com)
2. Get your Account SID and Auth Token from the Twilio Console
3. Obtain a Twilio phone number for sending/receiving communications

## Python Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installing Dependencies

To use Twilio with Python, you need to install the official Twilio Python SDK:

```bash
pip install twilio
```

Or, if you're using a `requirements.txt` file, add:

```
twilio
```

Then install with:

```bash
pip install -r requirements.txt
```

### Basic Python Usage Example

```python
from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send an SMS message
message = client.messages.create(
    body='Hello from Twilio!',
    from_='+1234567890',  # Your Twilio phone number
    to='+0987654321'      # Recipient's phone number
)

print(f"Message SID: {message.sid}")
```

### Environment Variables (Recommended)

For security, store your credentials as environment variables:

```bash
export TWILIO_ACCOUNT_SID='your_account_sid_here'
export TWILIO_AUTH_TOKEN='your_auth_token_here'
```

Then use them in your Python code:

```python
import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)
```

## Additional Resources

- [Twilio Documentation](https://www.twilio.com/docs)
- [Twilio Python SDK Documentation](https://www.twilio.com/docs/libraries/python)
- [Twilio API Reference](https://www.twilio.com/docs/api)
- [Twilio Python Quickstart](https://www.twilio.com/docs/sms/quickstart/python)

## Test Script

### Twilio Call Simulation (`test_twilio_call.py`)

This repository includes a test script that demonstrates how to:
- Connect to the Twilio API
- Initiate a phone call programmatically
- Play audio during the call using TwiML (Twilio Markup Language)

#### Running the Test Script

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your Twilio credentials:**
   ```bash
   export TWILIO_ACCOUNT_SID='your_account_sid_here'
   export TWILIO_AUTH_TOKEN='your_auth_token_here'
   ```

3. **Run the script:**
   ```bash
   python test_twilio_call.py <your_twilio_number> <destination_number>
   ```

   Example:
   ```bash
   python test_twilio_call.py +15551234567 +15559876543
   ```

   Or set environment variables and run without arguments:
   ```bash
   export TWILIO_PHONE_NUMBER='+15551234567'
   export TEST_PHONE_NUMBER='+15559876543'
   python test_twilio_call.py
   ```

#### What the Script Does

When executed, the test script will:
1. Connect to your Twilio account using the provided credentials
2. Initiate a phone call from your Twilio number to the destination number
3. During the call, it will:
   - Greet the recipient in German using text-to-speech
   - Play a sample MP3 audio file
   - Say goodbye in German
4. Display call details including the Call SID and status
5. Provide a link to view the call in the Twilio Console

#### Important Notes

- **Trial Accounts:** If using a Twilio trial account, you can only call verified phone numbers
- **Phone Number Format:** All phone numbers must be in E.164 format (e.g., +1234567890)
- **Costs:** Making calls will incur charges based on your Twilio pricing plan
- **Audio Files:** The script uses a sample audio file. You can modify the script to use your own audio files by changing the URL in the `create_twiml_audio_url()` function

#### Customizing the Audio

To use your own audio file, modify the `test_twilio_call.py` script:

```python
# Replace this line:
response.play("http://demo.twilio.com/docs/classic.mp3")

# With your own audio URL:
response.play("https://your-domain.com/your-audio-file.mp3")
```

Supported audio formats: MP3, WAV, GSM, μ-law

## License

This project is for demonstration purposes.
