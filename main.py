

from openai import OpenAI
import re

client = OpenAI(api_key="sk-proj-TDCpJrPrWro31Lk7TUCiT3BlbkFJ9p7rDBS6Vqi6dgENyt6B")

def chat_with(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
            
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with(user_input)
        response = re.sub(r'^\d+\.\s*', '', response, flags=re.MULTILINE)
        sentences = re.split(r'(?<=\.)\s+', response.strip())
        sentences = [sentence if sentence.endswith('.') else sentence + '.' for sentence in sentences]

        c=0
        for sentence in sentences:
            c = c+1
            response1 = client.images.generate(
                    model="dall-e-3",
                    prompt=sentence,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                    style="natural")
            image_url = response1.data[0].url
            print("Chatbot:Step",c,"-",sentence)
            print("Generated image URL: ",image_url)

             

