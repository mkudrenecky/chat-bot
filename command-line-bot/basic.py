from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from math_logic import MathLogicAdapter

chatbot = ChatBot("Botty", logic_adapters=["chatterbot.logic.MathematicalEvaluation",
        {'import_path': 'math_logic.MathLogicAdapter'},
        {'import_path': 'chatterbot.logic.BestMatch'}
        ])

CORPUS_FILE = 'company_x'
HARRIS_CORPUS = 'company_y'

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    CORPUS_FILE,
    HARRIS_CORPUS
)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 {chatbot.get_response(query)}")