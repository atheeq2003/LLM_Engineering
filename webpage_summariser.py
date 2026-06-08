from openai import OpenAI
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/117.0.0.0 Safari/537.36"
}


class Website:

    def __init__(self, url):

        self.url = url

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        self.title = (
            soup.title.string
            if soup.title
            else "No title found"
        )

        if soup.body:

            for irrelevant in soup.body(
                ["script", "style", "img", "input"]
            ):
                irrelevant.decompose()

            self.text = soup.body.get_text(
                separator="\n",
                strip=True
            )

        else:
            self.text = ""

        self.headings = [
            h.get_text(strip=True)
            for h in soup.find_all(
                ["h1", "h2", "h3"]
            )
        ]


webpage_content = Website(
    "https://github.com/atheeq2003"
)

user_message = f"""
Summarise the webpage content below.

Title:
{webpage_content.title}

Headings:
{chr(10).join(webpage_content.headings)}

Content:
{webpage_content.text[:10000]}
"""

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="gemma3:1b",
    messages=[
        {
            "role": "system",
            "content":
            """
            You are an expert summarization assistant.
            Produce a concise summary in bullet points.
            Focus on key information only.
            """
        },
        {
            "role": "user",
            "content": user_message
        }
    ]
)

print(response.choices[0].message.content)