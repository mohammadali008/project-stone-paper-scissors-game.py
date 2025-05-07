####-I.N.O.G ---Game-Project-Stone/Paper "MohammadAli"
import random 
import turtle as tl

# --- Define Main Functions ---
def DrawCircle():
    tl.circle(50)

def DrawRectangle():
    for _ in range(2):
        tl.forward(150)
        tl.left(90)
        tl.forward(80)
        tl.left(90)

def DrawCross():
    for i in range(2):
        for i in range(2):
            tl.forward(100)
            tl.right(144)

def TurtleSetting(content, x=0, y=0):
    tl.clear()
    tl.pensize(5)
    tl.speed('slow')  
    tl.fillcolor('blue')
    tl.penup()
    tl.goto(x, y)
    tl.pendown()
    tl.begin_fill()
    content()
    tl.end_fill()

# --- Game Play ---
shapes = {
    "stone": DrawCircle,
    "paper": DrawRectangle,
    "scissors": DrawCross
}

win_rules = {
    "stone": "scissors",
    "scissors": "paper",
    "paper": "stone"
}

end_point = 2
user_score = 0
bot_score = 0

while user_score < end_point and bot_score < end_point:
    user_choice = tl.textinput('Game', 'Enter one option: stone, paper, or scissors:')
    if user_choice not in shapes:
        tl.textinput('Error', 'Invalid choice. Press OK to try again.')
        continue

    bot_choice = random.choice(list(shapes.keys()))
    TurtleSetting(shapes[bot_choice], x=0, y=0)

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif win_rules[user_choice] == bot_choice:
        user_score += 1
        result = "You win this round!"
    else:
        bot_score += 1
        result = "Bot wins this round!"

    tl.textinput('Result', f'You chose {user_choice}, bot chose {bot_choice}.\n{result}\nScore: You {user_score} - Bot {bot_score}')

tl.textinput('Game Over', f'Final Score: You {user_score} - Bot {bot_score}')
tl.done()
