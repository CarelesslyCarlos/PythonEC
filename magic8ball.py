"""Write a Magic 8-Ball in python. Your program will consist of a series of if, elif, and one else statement.
Magic 8-Ball has 9 possible answers:
1. "Yes - definitely!"
2. "It is decidedly so."
3. "Without a doubt."
4. "Reply hazy, try again."
5. "Ask again later."
6. "Better not tell you now."
7. "My sources say no."
8. "Outlook not so good."
9. "Very doubtful."
"""

# To generate a random number between 1-9
import random

# To take user input.
name = input("What is your name? ")
question = input("What is your question? ")
answer = ""

# Generate a random number 1-9
random_num = random.randint(1, 9)

# YOUR CODE HERE
if random_num == 1:
    answer = 'Yes - definitely!'
elif random_num == 2:
    answer = 'It is decidedly so.'
elif random_num == 3:
    answer = 'Without a doubt.'
elif random_num == 4:
    answer = 'Reply hazy, try again.'
elif random_num == 5:
    answer = 'Ask again later.'
elif random_num == 6:
    answer = 'Better not tell you now.'
elif random_num == 7:
    answer = 'My sources say no.'
elif random_num == 8:
    answer = 'Outlook not so good.'
else:
    answer = 'Very Doubtful'


print(name + " asks: " + question)
print("Magic 8-ball's answer: " + answer)