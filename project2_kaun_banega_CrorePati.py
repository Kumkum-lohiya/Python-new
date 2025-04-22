import pyttsx3
questions = [
    ["What is the capital of India?",
     "Mumbai","Kolkata","New Dehli","Chennai",3],

    ["Who wrote the Indian national anthem JANA GANA MANA ?",
     "Bankim Chandra Chatterjee","Rabindranath Tagore","Mahatma Gandhi", "Sarojini Naidu",2],

    ["Which planet is known as the Red Planet?",
     "Earth","Mars","Jupiter","Venus",2],

    ["How many colors are there in the Indian National Flag?",
     2,3,4,5,2],

    ["Who is known as the “Missile Man of India”?",
     "Homi Bhabha","Dr. K. Sivan","A. P. J. Abdul Kalam","Vikram Sarabhai",3 ],

    ["Which is the smallest state in India by area?",
     "Goa","Sikkim","Tripura","Mizoram",1],

    ["Which Indian festival is also known as the FESTIVALS OF LIGHTS ?",
     "Holi","Diwali","Raksha Bandhan","Eid",2],

    [" What is the chemical symbol for Gold?",
     "Gd","Au","Ag","Go",2],

    ["Who was the first woman Prime Minister of India?",
     "Sonia Gandhi","Sarojini Naidu","Indira Gandhi","Pratibha Patil",3],

    ["In which year did India gain independence?",
     1945,1946,1947,1950,3],

    ["Who invented the telephone?",
     "Thomas Edison","Alexander Gram Bell","Nikola Tesla","Isaac Newton",2],

    ["What is the currency of Japan?",
     "Won","Renminbi","Ringgit","Yen",4],

    ["Who was the first Indian to go into space?",
     "Rakesh Sharma","Kalpana Chawla ","Sunita Williams","Vikram Sarabhai",1],

    ["In Hindu mythology, who is the wife of Lord Shiva?",
     "Saraswati","Sita","Lakshmi","Parvati",4]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000]
money = 0
for i in range(0,(len(questions))):
    question = questions[i]
    print(question[0])
    pyttsx3.speak(question[0])
    print(f'1.{question[1]}                             2.{question[2]}')
    print(f'3.{question[3]}                             4.{question[4]}')
    pyttsx3.speak(question[1])
    pyttsx3.speak(question[2])
    pyttsx3.speak(question[3])
    pyttsx3.speak(question[4])

    reply =int(input("Enter the correct Option"))
    if reply == question[-1]:
        print(f'\nYou won {levels[i]} Rupees\n')
        pyttsx3.speak(f'You Won {levels[i]} Rupees')
        if i == 4:
            money = 10000
        elif i == 8:
            money = 160000
        elif i == 14:
            money = 5000000
    else:
        print("\nWrong Answer !!\n ")
        pyttsx3.speak("Wrong Answer")
        break
print(f"Your take home money is {money}")
pyttsx3.speak(f'Your take home money is {money}3')


