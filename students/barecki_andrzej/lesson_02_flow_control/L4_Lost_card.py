# There was a set of cards with numbers from 1 to N. One of the card is now lost.
# Determine the number on that lost card given the numbers for the remaining cards.

# Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers
# in the range from 1 to N). Find and print the number on the lost card.

total_count_of_cards = int(input())

myList = [0] * total_count_of_cards
i = 0

while True:
    myList[int(input())-1] = 1
    i += 1
    if i == (total_count_of_cards - 1):
        break

for i in range(0, total_count_of_cards):
    if myList[i] == 0:
        result = (i + 1)

print(result)
