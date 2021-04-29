from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
my_bot= ChatBot(
    name="HelpBot",
    read_only=true,
   logic_adapters= ['chatterbot.logic.MathematicalEvaluation',
          'chatterbot.logic.BestMatch']
    )



    small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
          'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
          'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']



          list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
          list_trainer.train(item)



          >>> print(my_bot.get_response("hi"))
how do you do?

>>> print(my_bot.get_response("i feel awesome today"))
excellent, glad to hear that.

>>> print(my_bot.get_response("what's your name?"))
i'm pybot. ask me a math question, please.

>>> print(my_bot.get_response("show me the pythagorean theorem"))
a squared plus b squared equals c squared.

>>> print(my_bot.get_response("do you know the law of cosines?"))
c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)


from chatterbot.trainers import ChatterBotCorpusTrainer

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')
print(my_bot.get_response("hi"))
print(my_bot.get_response("I am fine"))
print(my_bot.get_response("What's your name?"))
print(my_bot.get_response("Do you know the law of cosines?"))
print(my_bot.get_response("Show me the pythorean theorem"))


while True:
try:
    bot_input=input("you:")
    bot_response=bot.get_response(bot_input)
print(f"{my_bot.name}:{bot_response}")
except(KeyboardInterrupt,EOFError,SystemExit):
    break;
