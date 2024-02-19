from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from .chatbot_instance import chatbot

def train_chatbot(chatbot):
    # Paths to the training corpora
    CORPUS_FILES = [
        'chatbot/corpora/company_y.yml',
        'chatbot/corpora/company_x.yml'
    ]

    # Create a trainer and train the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    for corpus_file in CORPUS_FILES:
        trainer.train(corpus_file)

    
    
