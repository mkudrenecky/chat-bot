from chatterbot import ChatBot

# Create a global instance of the ChatBot
chatbot = ChatBot(
    'MyChatBot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        {'import_path': 'chatbot.logic_adapters.math_logic.MathLogicAdapter'},
        'chatterbot.logic.BestMatch'
    ]
)

