def create_card():
    cards = []
    for i in range(8):
        card = []
        card.append("X")

        card.append(i)
        card_ = card
        cards.append(card)
        cards.append(card_)

    return cards
print(create_card())
def create_bord():
    matrix = []
    for i in range(4):
        row = []
        for t in range(4):
            row.append("*")
        matrix.append(row)


    a = create_card()
    for j in range(4):
        for l in range(4):
            matrix[j][l] = a[j]





    return matrix
print(create_bord())
def Choosing_the_player():
    choice = input("choice_numbers")
    choice1 = input("choice mor numbers")

    return choice ,choice1



def start_game():
    create_bord()








