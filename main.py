import os
from groq import Groq
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
import json

def clean_json_output(text):
    text = text.strip()

    # remove ```json ``` or ``` if present
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)

def analyze_lead(lead):
    try:
        user_prompt = f"""
        Lead Details:
        Name: {lead['name']}
        Email: {lead['email']}
        Message: {lead['message']}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        print("API Error:", e)
        return None

def take_action(result):

    if not result:
        print("No valid result to act on")
        return
    
    score = result["lead_score"]

    if score == "High":
        print("ACTION: Send immediate sales email")
    elif score == "Medium":
        print("ACTION: Add to email nurture sequence")
    else:
        print("ACTION: Mark as spam / ignore") 

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

if __name__ == "__main__":
    
    with open("sample_data.json", "r") as f:
        sample_leads = json.load(f)

    for lead in sample_leads:
        print("\n" + "="*40)
        print("NEW LEAD")
        print("="*40)
        print(lead)

        raw_result = analyze_lead(lead)
        if raw_result:
            parsed_result = clean_json_output(raw_result)
        else:
            parsed_result = None

        priority = "🔥 HIGH PRIORITY" if parsed_result["lead_score"] == "High" else "Normal"
        print(f"Priority: {priority}")

        print("\n AI ANALYSIS")
        print(parsed_result)

take_action(parsed_result)        