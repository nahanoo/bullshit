def sum_certain_number(players,certain_number):
    certain_number_count = 0
    for player in players:
        for dice_value in player.dices.values():
            if dice_value == certain_number or dice_value == 1:
                certain_number_count += 1
    return certain_number_count

def average_certain_number(n_rounds,n_players,n_dices_per_person):
    certain_number_sums = []
    for round in range(n_rounds):
        players = create_players(n_players,n_dices_per_person)
        #print_throw(players)
        certain_number_sums.append(sum_certain_number(players,5))
    return sum(certain_number_sums)/len(certain_number_sums)

def plot_certain_number_occurance(max_players,max_n_dices_per_person):
    z = []
    x = []
    y = []
    for n_players in range(max_players):
        for n_dices_per_person in range(max_n_dices_per_person):
            x.append(n_players)
            y.append(n_dices_per_person)
            z.append(average_certain_number(1000,n_players,n_dices_per_person))
    df = pd.DataFrame({'n players':x,'n dices':y,'average sum of certain number (1 inclusive)':z})
    fig = px.scatter_3d(df,x='n players',y='n dices',z='average sum of certain number (1 inclusive)')
    fig.show()