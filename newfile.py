from tkinter import *
from PIL import ImageTk, Image
from random import choice

root = Tk()
root.title("Blackjack")
root.iconbitmap("jack_icon.ico")

game_frame = LabelFrame(root, width=100, height=500, bg="red4", padx=30, pady=40)
game_frame.pack(padx=10, pady=10)
money_point = 500
money_bet = 0
playercolumn_pos = 2
botcolumn_pos = 2

# Lists
deck_cards = [
                "CAce.png", "C2.png", "C3.png", "C4.png", "C5.png", "C6.png", "C7.png",
                "C8.png", "C9.png", "C10.png", "CJack.png", "CQueen.png", "CKing.png",

                "DAce.png", "D2.png", "D3.png", "D4.png", "D5.png", "D6.png", "D7.png",
                "D8.png", "D9.png", "D10.png", "DJack.png", "DQueen.png", "DKing.png",
                
                "HAce.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png", "H7.png",
                "H8.png", "H9.png", "H10.png", "HJack.png", "HQueen.png", "HKing.png",
                
                "SAce.png", "S2.png", "S3.png", "S4.png", "S5.png", "S6.png", "S7.png",
                "S8.png", "S9.png", "S10.png", "SJack.png", "SQueen.png", "SKing.png"
              ]

card_values = [
    
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10

              ]


bot_cards = []
botcards_value = []
playercards_value = []

# game starts as this function is called
def firstplay_cards():
    global end_stay, bot_cards, money_input, money_bet, deck_cards, card_values, playercards_value, botcards_value
    entry = money_input.get()
    money_bet= int(entry)
    if entry == "Bet first before playing":
        money_input = Entry(game_frame, bg="red4")
        money_input.grid(column=2, row=6, padx=5, pady=5)
        money_input.insert(0, "Delete Text, Place Bet")

    elif entry == "Delete Text, Place Bet":
        money_input = Entry(game_frame, bg="red4")
        money_input.grid(column=2, row=6, padx=5, pady=5)
        money_input.insert(0, "Bet first before playing")

    else:
        # player cards
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP0 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP0.image = img_typed
        unlucky_cardP0.grid(column=0, row=4, rowspan=2)

        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP1 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP1.image = img_typed
        unlucky_cardP1.grid(column=1, row=4, rowspan=2)

        # bot cards
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        bot_cards.append(random_card)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB0 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB0.image = img_typed
        unlucky_cardB0.grid(column=0, row=0, rowspan=2)

        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        bot_cards.append(random_card)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB1 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB1.image = img_typed
        unlucky_cardB1.grid(column=1, row=0, rowspan=2)

        if sum(playercards_value) == 21 or sum(botcards_value) ==21 :  # game ends
            end_stay()
            
        else: 
            play_button = Button(game_frame, text="Play", state="disable", command=firstplay_cards)
            play_button.grid(column=4, row=7, padx=5, pady=5)
            
            stay_button = Button(game_frame, text="Stay", state="active", command=end_stay)
            stay_button.grid(column=0, row=6, padx=5, pady=5)

            money_input = Entry(game_frame, state="disable")
            money_input.grid(column=2, row=6, padx=5, pady=5)


            hit_button = Button(game_frame, text="Hit", state="active", command=overall_hit)
            hit_button.grid(column=4, row=6, padx=5, pady=5)

# player getting card and saving position for forget later and used for over_all hit
def player_hit():
    global botcolumn_pos, playercolumn_pos, bot_cards, money_input, \
           money_bet, deck_cards, card_values, playercards_value, botcards_value

    if playercolumn_pos == 2:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP2 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP2.image = img_typed
        unlucky_cardP2.grid(column=2, row=4, rowspan=2)
        playercolumn_pos += 1

    elif playercolumn_pos == 3:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP3 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP3.image = img_typed
        unlucky_cardP3.grid(column=3, row=4, rowspan=2)
        playercolumn_pos += 1
        
    elif playercolumn_pos == 4:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP4 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP4.image = img_typed
        unlucky_cardP4.grid(column=4, row=4, rowspan=2)
        playercolumn_pos += 1

    elif playercolumn_pos == 5:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP5 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP5.image = img_typed
        unlucky_cardP5.grid(column=5, row=4, rowspan=2)
        playercolumn_pos += 1
        
    else:
        pass

# bot is same as player but cards face down same as player
def bot_hit():
    global botcolumn_pos, playercolumn_pos, bot_cards, money_input, \
           money_bet, deck_cards, card_values, playercards_value, botcards_value

    if botcolumn_pos == 2:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        bot_cards.append(random_card)
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB2 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB2.image = img_typed
        unlucky_cardB2.grid(column=2, row=0, rowspan=2)
        botcolumn_pos += 1

    elif botcolumn_pos == 3:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        bot_cards.append(random_card)
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB3 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB3.image = img_typed
        unlucky_cardB3.grid(column=3, row=0, rowspan=2)
        botcolumn_pos += 1
        
    elif botcolumn_pos == 4:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        bot_cards.append(random_card)
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB4 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB4.image = img_typed
        unlucky_cardB4.grid(column=4, row=0, rowspan=2)
        botcolumn_pos += 1

    elif botcolumn_pos == 5:
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        bot_cards.append(random_card)
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB5 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB5.image = img_typed
        unlucky_cardB5.grid(column=5, row=0, rowspan=2)
        botcolumn_pos += 1

# clicking hit, opens the bot command and only gives play one hit
def overall_hit():
    global bot_hit, player_hit, end_stay, botcards_value

    for i in range(3):
        if sum(botcards_value) == 21:
            break
        else:
            if sum(botcards_value) <= 14:
                decision = ["yes", "yes", "yes", "yes", "yes", "yes", "yes","no", "no", "no"]
                pick = choice(decision)
                if pick == "yes":
                    bot_hit()
                    if sum(botcards_value) >= 21:
                        break
                    
            elif 18 >= sum(botcards_value) >= 15:
                decision = ["yes", "yes", "yes", "no", "no", "no", "no", "no", "no", "no"]
                pick = choice(decision)
                if pick == "yes":
                    bot_hit()
                    if sum(botcards_value) >= 21:
                        break
                else:
                    break
            else:
                break
            
    
    player_hit()
    if sum(playercards_value) == 21:
        end_stay()
    elif sum(playercards_value) >= 21:
        end_stay()

def end_stay():
    global botcolumn_pos, playercolumn_pos, bot_cards, money_input, money_bet,\
           deck_cards, card_values, playercards_value, botcards_value, money_point,\
           game_frame
           
    # makes sure bot gets its turn before concluding, else the bot has already decided
    if playercolumn_pos == 2:
        for i in range(3):
            if sum(botcards_value) == 21:
                break
            else:
                if sum(botcards_value) <= 14:
                    decision = ["yes", "yes", "yes", "yes", "yes", "yes", "yes","yes", "no", "no"]
                    pick = choice(decision)
                    if pick == "yes":
                        bot_hit()
                        if sum(botcards_value) >= 21:
                            break
                        
                elif 18 >= sum(botcards_value) >= 15:
                    decision = ["yes", "yes", "yes", "no", "no", "no", "no", "no", "no", "no"]
                    pick = choice(decision)
                    if pick == "yes":
                        bot_hit()
                        if sum(botcards_value) >= 21:
                            break
                    else:
                        break
                else:
                    break
    


    print(bot_cards)
# bot cards face up/ reveal
    for i in range(len(bot_cards)):
        img_open = Image.open("playingcards/" + str(bot_cards[i]))
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB4 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB4.image = img_typed
        unlucky_cardB4.grid(column=i, row=0, rowspan=2)
        
    
# list of rules on who wins or not    
    if sum(playercards_value) == 21:
        joker_card.grid_forget()
        open_jokerq = Image.open("win.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
        money_point += money_bet
        
    if sum(botcards_value) == 21:
        joker_card.grid_forget()
        open_jokerq = Image.open("lose.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
        money_point -= money_bet
                         
    elif sum(botcards_value) > 21 and sum(playercards_value) > 21:
        joker_card.grid_forget()
        open_jokerq = Image.open("tie.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
            
    elif sum(botcards_value) < sum(playercards_value) <= 20:
        joker_card.grid_forget()
        open_jokerq = Image.open("win.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
        money_point += money_bet

    elif sum(botcards_value) == sum(playercards_value):
        joker_card.grid_forget()
        open_jokerq = Image.open("tie.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
        

    elif sum(botcards_value) >= 21:
        joker_card.grid_forget()
        open_jokerq = Image.open("win.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, padx=20, pady=5, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
        money_point += money_bet
                
    else:
        joker_card.grid_forget()
        open_jokerq = Image.open("lose.jpg")
        resized_jokerq = open_jokerq.resize((375, 125))
        typed_jokerq = ImageTk.PhotoImage(resized_jokerq)
        joker_qoute = Label(game_frame, image=typed_jokerq, bg="red4")
        joker_qoute.image = typed_jokerq
        joker_qoute.grid(column=1, row=2, rowspan=2, columnspan=3, padx=5, pady=8)
        money_point -= money_bet


    
    print(deck_cards)
    print(playercards_value, "1")
    print(bot_cards)
    print(botcards_value)    
    # enables the play and bet button again

    exit_button = Button(game_frame, text="Quit Game", command=root.quit)
    exit_button.grid(column=0, row=7, padx=5, pady=5)

    money_label = Label(game_frame, text=("Total Money:", "Php" + str(money_point)))
    money_label.grid(column=2, row=7, padx=5, pady=5)

    play_button = Button(game_frame, text="Play", command=moreplay_cards)
    play_button.grid(column=4, row=7, padx=5, pady=5)

    # disable the hit and stay, enable money input again

    stay_button = Button(game_frame, text="Stay", state="disable", command=end_stay)
    stay_button.grid(column=0, row=6, padx=5, pady=5)

    money_input = Entry(game_frame)
    money_input.grid(column=2, row=6, padx=5, pady=5)
    money_input.insert(0, "Play again?")

    hit_button = Button(game_frame, text="Hit", state="disable", command=overall_hit)
    hit_button.grid(column=4, row=6, padx=5, pady=5)

    # reset counters & lists, and clear lists

    money_bet = 0
    playercolumn_pos = 2
    botcolumn_pos = 2

    deck_cards = [
                "CAce.png", "C2.png", "C3.png", "C4.png", "C5.png", "C6.png", "C7.png",
                "C8.png", "C9.png", "C10.png", "CJack.png", "CQueen.png", "CKing.png",

                "DAce.png", "D2.png", "D3.png", "D4.png", "D5.png", "D6.png", "D7.png",
                "D8.png", "D9.png", "D10.png", "DJack.png", "DQueen.png", "DKing.png",
                
                "HAce.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png", "H7.png",
                "H8.png", "H9.png", "H10.png", "HJack.png", "HQueen.png", "HKing.png",
                
                "SAce.png", "S2.png", "S3.png", "S4.png", "S5.png", "S6.png", "S7.png",
                "S8.png", "S9.png", "S10.png", "SJack.png", "SQueen.png", "SKing.png"
              ]

    card_values = [
    
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10

              ]


    bot_cards.clear()
    botcards_value.clear()
    playercards_value.clear()

    

def moreplay_cards():
    global end_stay, bot_cards, money_input, money_bet, deck_cards, card_values,\
           playercards_value, botcards_value, joker_qoute, end_stay, game_frame
    entry = money_input.get()
    entry = money_input.get()
    money_bet= int(entry)

    game_frame.forget()
    game_frame = LabelFrame(root, width=100, height=500, bg="red4", padx=30, pady=40)
    game_frame.pack(padx=10, pady=10)

    open_joker = Image.open("joker.png")
    resized_joker = open_joker.resize((100, 125))
    typed_joker = ImageTk.PhotoImage(resized_joker)
    joker_card = Label(game_frame, image=typed_joker, bg="red4")
    joker_card.image = typed_joker
    joker_card.grid(column=3, row=2, rowspan=2)

    game_title = Label(game_frame, \
                       text=
                       "Black Jâ’¶ck/er \n\
                              made by Ricodere", bg="red4")
    game_title.grid(column=0, row=2, rowspan=2, columnspan=3)
    
    if entry == "Bet first before playing":
        money_input = Entry(game_frame)
        money_input.grid(column=2, row=6, padx=5, pady=5, bg="red4")
        money_input.insert(0, "Delete Text, Place Bet")

    elif entry == "Delete Text, Place Bet":
        money_input = Entry(game_frame)
        money_input.grid(column=2, row=6, padx=5, pady=5, bg="red4")
        money_input.insert(0, "Bet first before playing")

    else:
        # player cards
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP0 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP0.image = img_typed
        unlucky_cardP0.grid(column=0, row=4, rowspan=2)

        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        playercards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        img_open = Image.open("playingcards/" + random_card)
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardP1 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardP1.image = img_typed
        unlucky_cardP1.grid(column=1, row=4, rowspan=2)

        # bot cards
        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        bot_cards.append(random_card)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB0 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB0.image = img_typed
        unlucky_cardB0.grid(column=0, row=0, rowspan=2)

        random_card = choice(deck_cards)
        index_value = deck_cards.index(random_card)
        botcards_value.append(card_values[index_value])
        deck_cards.remove(random_card)
        card_values.pop(index_value)
        bot_cards.append(random_card)
        img_open = Image.open("yugioh.png")
        img_resize = img_open.resize((100, 125))
        img_typed = ImageTk.PhotoImage(img_resize)
        unlucky_cardB1 = Label(game_frame, image=img_typed, bg="red4")
        unlucky_cardB1.image = img_typed
        unlucky_cardB1.grid(column=1, row=0, rowspan=2)

        if sum(playercards_value) == 21:  # game ends
            end_stay()
            
        else: 
            play_button = Button(game_frame, text="Play", state="disable", command=firstplay_cards)
            play_button.grid(column=4, row=7, padx=5, pady=5)

            exit_button = Button(game_frame, text="Quit Game", command=root.quit)
            exit_button.grid(column=0, row=7, padx=5, pady=5)
            
            stay_button = Button(game_frame, text="Stay", state="active", command=end_stay)
            stay_button.grid(column=0, row=6, padx=5, pady=5)

            money_input = Entry(game_frame, state="disable")
            money_input.grid(column=2, row=6, padx=5, pady=5)

            money_label = Label(game_frame, text=("Total Money:", "Php" + str(money_point)))
            money_label.grid(column=2, row=7, padx=5, pady=5)

            hit_button = Button(game_frame, text="Hit", state="active", command=overall_hit)
            hit_button.grid(column=4, row=6, padx=5, pady=5)

            
# Initial Structure
# Row 0-1

    
# Row 2-3
open_joker = Image.open("joker.png")
resized_joker = open_joker.resize((100, 125))
typed_joker = ImageTk.PhotoImage(resized_joker)
joker_card = Label(game_frame, image=typed_joker, bg="red4")
joker_card.image = typed_joker
joker_card.grid(column=3, row=2, rowspan=2)

game_title = Label(game_frame, \
                   text=
                   "Black Jâ’¶â‚¡k/er   \n\
                            \n\
                          made by Eric Delos Reyes", bg="red4")
game_title.grid(column=0, row=2, rowspan=2, columnspan=3)
# Row 4-5



# Row 6
stay_button = Button(game_frame, text="Stay", state="disable", command=end_stay)
stay_button.grid(column=0, row=6, padx=5, pady=5)

money_input = Entry(game_frame)
money_input.grid(column=2, row=6, padx=5, pady=5)
money_input.insert(0, "Bet first before playing")

hit_button = Button(game_frame, text="Hit", state="disable", command=overall_hit)
hit_button.grid(column=4, row=6, padx=5, pady=5)

spacer1 = Label(game_frame, text="    ", bg="red4")
spacer1.grid(column=1, row=6, padx=50, pady=5)
spacer2 = Label(game_frame, text="    ", bg="red4")
spacer2.grid(column=3, row=6, padx=50, pady=5)


# Row 7
exit_button = Button(game_frame, text="Quit Game", command=root.quit)
exit_button.grid(column=0, row=7, padx=5, pady=5)

money_label = Label(game_frame, text=("Total Money:", "Php" + str(money_point)))
money_label.grid(column=2, row=7, padx=5, pady=5)

play_button = Button(game_frame, text="Play", command=firstplay_cards)
play_button.grid(column=4, row=7, padx=5, pady=5)

spacer1 = Label(game_frame, text="    ", bg="red4")
spacer1.grid(column=1, row=7, padx=5, pady=5)
spacer2 = Label(game_frame, text="    ", bg="red4")
spacer2.grid(column=3, row=7, padx=5, pady=5)

    

root.mainloop()