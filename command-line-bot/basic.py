from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from math_logic import MathLogicAdapter

chatbot = ChatBot("Botty", logic_adapters=[
        {'import_path': 'math_logic.MathLogicAdapter'},
        {'import_path': 'chatterbot.logic.BestMatch'}
        ])

CORPUS_FILE = 'cayenta_corpus'
HARRIS_CORPUS = 'harris_computer_corpus'

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