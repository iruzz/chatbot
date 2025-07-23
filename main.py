from google import genai

api_key = "AIzaSyAJL1byUMOhrBXT7n7X6nEEea_BdhTuY1k"
client  = genai.Client(api_key=api_key)
chat  = client.chats.create(model="gemini-2.0-flash")

def chat_inference(prompt):
    response = chat.send_message(prompt)
    return response.text

# input_text = input("Chat: ")
# print(input_text)
# print(chat_inference(input_text))