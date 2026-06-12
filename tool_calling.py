from openai import OpenAI
import json

def create_task(title, owner=None, deadline=None):
    print("\nTASK CREATED")
    print(f"Title    : {title}")
    print(f"Owner    : {owner}")
    print(f"Deadline : {deadline}")

    return {
        "status": "success",
        "title": title,
        "owner": owner,
        "deadline": deadline
    }

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

meeting_notes = """
Project Sync Meeting

- John completed the login module.
- Sarah will start payment gateway integration next week.
- The team found a bug in the user profile page.
- Mike will investigate and provide a fix by Friday.
- Final testing is scheduled for June 30.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "create_task",
            "description": "Create a project task from meeting action items",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Task title"
                    },
                    "owner": {
                        "type": "string",
                        "description": "Person responsible"
                    },
                    "deadline": {
                        "type": "string",
                        "description": "Task deadline"
                    }
                },
                "required": ["title"]
            }
        }
    }
]
