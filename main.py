import nltk
from nltk.chat.util import Chat, reflections
from gtts import gTTS
import os


pairs = [
    [
        r"(?:Hello|Hi|Hey|Greetings)(.*)",
        ["Hello! How can I help you today?", "Hi there! How are you feeling today?"]
    ],
    [
        r"(.*) feel(.*)",
        ["I understand. Can you tell me more about your feelings?", "I'm here to listen. What's on your mind?"]
    ],
    [
        r"(.*)(good|well|peaceful)(.*)",
        ["I'm glad to hear that you're feeling peaceful!", "That's wonderful. Peaceful feelings are the best."]
    ],
    [
        r"(.*)(sad|down|anxious)(.*)",
        ["I'm sorry to hear that you're feeling this way. Would you like to talk about it?", "I'm here to support you."]
    ],
    [
        r"(.*)(thank you|thanks)(.*)",
        ["You're welcome! If you have more to share or need assistance, feel free to ask.", "You're welcome. Take care."]
    ],
    [
        r"(bye|goodbye|exit|quit)",
        ["Goodbye. Take care of yourself!", "Goodbye. I'm here whenever you need me."]
    ],
]


chatbot = Chat(pairs, reflections)

while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
    
    
    tts = gTTS(response, lang='en')
    tts.save("bot_response.mp3")
    
  
    os.system("mpg321 bot_response.mp3")
