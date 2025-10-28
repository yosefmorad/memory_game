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


def create_bord():
    a = create_card()

    matrix = []
    matrix.append(a)
    return matrix
print(create_bord()[0][3])



def start_game():
    x =[]
    for j in create_card():
        x.append([j][0][0])
    return x
print(start_game())

def plyer_choice():
    choice = input(int("enter num"))

    return choice

def show():
    choice = plyer_choice()
    return create_bord()[0][choice][1]

print()





