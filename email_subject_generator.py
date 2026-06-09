from openai import OpenAI

system_prompt = "You are professional email reader, read the contents of the email and generate a subject for it. DO NOT put explanations. Just a single line subject must be the response"

email_content = """
Hi Team,

I hope you're doing well.

I wanted to provide a quick update on the project status. The initial development phase has been completed, and we are currently conducting testing to identify and resolve any remaining issues. So far, progress is on track, and we expect to meet the planned deadline.

Please let me know if you have any questions or if there are additional requirements that should be addressed during this phase.

Thank you for your continued support.

Best regards,

Alex Morgan
Project Coordinator

"""

messages = [
    {
        "role": "system", "content": system_prompt
    },
    {
        "role": "user", "content": f"""Here is my email content: {email_content}"""
    },
]

openai = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = openai.chat.completions.create(model="gemma3:1b", messages=messages)

print(response.choices[0].message.content)