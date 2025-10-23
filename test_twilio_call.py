#!/usr/bin/env python3
"""
Twilio Call Test Script
========================

This script demonstrates how to:
1. Connect to the Twilio API
2. Initiate a phone call
3. Play audio during the call using TwiML

Requirements:
- twilio Python package
- Valid Twilio Account SID and Auth Token
- A Twilio phone number
- A verified destination phone number (for trial accounts)
"""

import os
import sys
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse


def create_twiml_audio_url():
    """
    Creates a TwiML response that plays audio during a call.

    Returns:
        str: TwiML XML string for playing audio
    """
    response = VoiceResponse()

    # Greet the caller
    response.say(
        "Hallo! Dies ist ein Test-Anruf von Twilio.",
        language="de-DE",
        voice="Polly.Hans"
    )

    # Play a sample audio file
    # You can use your own MP3/WAV URL or Twilio's sample audio
    response.play("http://demo.twilio.com/docs/classic.mp3")

    # Add another message
    response.say(
        "Das war eine Audio-Demonstration. Auf Wiedersehen!",
        language="de-DE",
        voice="Polly.Hans"
    )

    return str(response)


def make_test_call(to_number, from_number, twiml_url=None):
    """
    Initiates a test call using Twilio API.

    Args:
        to_number (str): Destination phone number (E.164 format: +1234567890)
        from_number (str): Your Twilio phone number (E.164 format)
        twiml_url (str, optional): URL that returns TwiML instructions

    Returns:
        Call object with call details
    """
    # Get credentials from environment variables
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    if not account_sid or not auth_token:
        raise ValueError(
            "Missing Twilio credentials. Please set:\n"
            "  TWILIO_ACCOUNT_SID\n"
            "  TWILIO_AUTH_TOKEN"
        )

    # Create Twilio client
    client = Client(account_sid, auth_token)

    # If no TwiML URL provided, use inline TwiML
    if twiml_url:
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url=twiml_url
        )
    else:
        # Use inline TwiML
        twiml = create_twiml_audio_url()
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml=twiml
        )

    return call


def simulate_call_with_status_check(to_number, from_number):
    """
    Simulates a call and checks its status.

    Args:
        to_number (str): Destination phone number
        from_number (str): Your Twilio phone number
    """
    print("=" * 60)
    print("Twilio Call Simulation Test")
    print("=" * 60)
    print(f"\nInitiating call...")
    print(f"  From: {from_number}")
    print(f"  To:   {to_number}")

    try:
        # Make the call
        call = make_test_call(to_number, from_number)

        print(f"\n✓ Call initiated successfully!")
        print(f"  Call SID:    {call.sid}")
        print(f"  Status:      {call.status}")
        print(f"  Direction:   {call.direction}")

        # Get account SID for constructing console URL
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        console_url = f"https://console.twilio.com/us1/monitor/logs/call/{call.sid}"

        print(f"\n  View in Console: {console_url}")

        print("\nThe call will:")
        print("  1. Greet the recipient in German")
        print("  2. Play a sample audio file")
        print("  3. Say goodbye in German")

        print("\n" + "=" * 60)
        print("Test completed successfully!")
        print("=" * 60)

        return call

    except Exception as e:
        print(f"\n✗ Error making call: {str(e)}")
        sys.exit(1)


def main():
    """
    Main function to run the test script.
    """
    print("\n" + "=" * 60)
    print("Twilio Call Test Script")
    print("=" * 60)

    # Check for environment variables
    if not os.environ.get('TWILIO_ACCOUNT_SID'):
        print("\n⚠️  Missing TWILIO_ACCOUNT_SID environment variable")
        print("\nPlease set your Twilio credentials:")
        print("  export TWILIO_ACCOUNT_SID='your_account_sid'")
        print("  export TWILIO_AUTH_TOKEN='your_auth_token'")
        sys.exit(1)

    if not os.environ.get('TWILIO_AUTH_TOKEN'):
        print("\n⚠️  Missing TWILIO_AUTH_TOKEN environment variable")
        sys.exit(1)

    # Get phone numbers from command line or environment
    from_number = os.environ.get('TWILIO_PHONE_NUMBER')
    to_number = os.environ.get('TEST_PHONE_NUMBER')

    if len(sys.argv) >= 3:
        from_number = sys.argv[1]
        to_number = sys.argv[2]

    if not from_number or not to_number:
        print("\nUsage:")
        print("  python test_twilio_call.py <from_number> <to_number>")
        print("\nOr set environment variables:")
        print("  export TWILIO_PHONE_NUMBER='+1234567890'")
        print("  export TEST_PHONE_NUMBER='+0987654321'")
        print("\nExample:")
        print("  python test_twilio_call.py +1234567890 +0987654321")
        sys.exit(1)

    # Validate phone number format
    if not from_number.startswith('+') or not to_number.startswith('+'):
        print("\n⚠️  Phone numbers must be in E.164 format (e.g., +1234567890)")
        sys.exit(1)

    # Run the call simulation
    simulate_call_with_status_check(to_number, from_number)


if __name__ == "__main__":
    main()
