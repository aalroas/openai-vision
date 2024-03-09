from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Provide a concise response with only the total paid amount and tax amount formatted as {\"total\": 100, \"tax\": 10}"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://files.sikayetvar.com/complaint/2668/26682641/ticket-restaurant-edenred-gecerli-restaurantlar-odeme-kabul-etmiyor-4.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)