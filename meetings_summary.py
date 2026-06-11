from openai import OpenAI

system_prompt = """
You are a professional project assistant.
Read the meeting notes and extract:
1. A short meeting summary
2. Action items
3. Owners (if mentioned)
4. Deadlines (if mentioned)

Return only the formatted output.
"""

meeting_notes = """
Project Sync Meeting

- John completed the login module.
- Sarah will start payment gateway integration next week.
- The team found a bug in the user profile page.
- Mike will investigate and provide a fix by Friday.
- Final testing is scheduled for June 30.
"""

messages = [
    {"role": "system", "content": system_prompt},
    {
        "role": "user",
        "content": f"Here are the meeting notes:\n\n{meeting_notes}"
    }
]

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="gemma3:cloud",
    messages=messages
)

print(response.choices[0].message.content)