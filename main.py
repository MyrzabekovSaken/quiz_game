questions = ["This football team won World Cup 2022?\n a. Argentina\n b. France \n c. Croatia\n Your answer is: ", 
             "This football team won in Champions League 2021/2022?\n a. Liverpool\n b. PSG\n c. Real Madrid\n Your answer is: ",
             "This runner broken world record in Berlin 2022 year?\n a. Mo Farah\n b. Eliud Kipchoge\n c. Kenenise Bekele\n Your answer is: ",
             "She is a won 'Indian Wells Masters' in 2023 year?\n a. Sabalenka Aryna\n b. Swiatek Iga\n c. Rybakina Elena\n Your answer is: ", 
             "He is a spanish professional tennis player who have a record in Grand Slam men's single titles?\n a. Rafael Nadal\n b. Novak Djokovic\n c. Carlos Alcaraz\n Your answer is: "]

right_answers = ["a", "c", "b", "c", "a"]

def run_test(questions: list[str], right_answers: list[str]):
    """функция принимает на вход список вопросов и список правильных ответов
    с помощью функции input() спрашивает у пользователя ответ на каждый вопрос
    возвращает количество правильных ответов
    """
    
    score = 0
    i = 0

    while i < len(questions):

        each_question = input(questions[i])
        
        if each_question == right_answers[i]:
            score += 1
            print("Correct\n You score now is", score,"\n")
        else:
            print("Incorrect\n You score now is", score,"\n")
        
        i += 1

    print("Finally you score is", score)

    
run_test(questions, right_answers)
