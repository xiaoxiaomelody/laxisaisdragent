import json
import openai

openai.api_key = "import your own api key" #here I imported my secret API key

def load_emails(file_path="emails.json"):
    """this function loads mock emails from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)
    
def extract_name(email_address):
    """
    Extract a human-readable name from the sender's email.
    Example: "jane.doe@example.com" -> "Jane Doe"
    """
    name_part = email_address.split("@")[0]
    name_parts = name_part.replace(".", " ").replace("_", " ").split()
    return " ".join([part.capitalize() for part in name_parts])

def classify_email(subject, body):
    """
    This function classifies the email into general categories and return the category name. 
    """
    prompt = f"""
    Classify this email into one of these categories:
    - Inquiry, meaning asking questions, implying concerns, and seeking more information
    - Meeting Request, meaning proposing time availabilities, or sending a meeting invite, calendar, or link
    - Follow-Up, meaning offering more information on a topic, or expressing appreciation and seeking next conversation 
    - Objection, meaning implying not interested or offering rejection
    - Other, which is unrelevant to business or workplace context and falls out of the four scopes listed above

    Subject: {subject}
    Body: {body}

    Respond with only the category name.
    """
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message["content"].strip()

def generate_reply(intent, subject, body, sender_name):
    """
    This function generates reply in a polite manner accoridng to sender's intent.
    """
    prompt = f"""
    You are a helpful, professional AI email assistant. You help respond to inbound emails, 
    follow-up threads, and ongoing conversations in a natural, human-like way.
    
    Write a reply to the following email:

    Intent: {intent}
    Subject: {subject}
    Body: {body}

    Rules:
    1. Always starts with: "Hi {sender_name},"
    2. Always has the first sentence: "Thank you for your email."
    3. After that, generate a personalized and relevant reply based on the intent and body.
    4. Keep tone polite, professional, and natural.
    5. Write at most 4 sentences
    6. End with: "Best regards, John"
    """
    respond = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return respond.choices[0].message["content"].strip()
 
if __name__ == "__main__":
    emails = load_emails()

    for email in emails:
        sender_name = extract_name(email["sender"])
        intent = classify_email(email["subject"], email["body"])
        reply = generate_reply(intent, email["subject"], email["body"], sender_name)

        print(f"--- Email from {email['sender']} ---")
        print(f"Intent: {intent}")
        print(f"Draft Reply:\n{reply}\n")
