def player_input():
	maker =''

# keep asking player 1 to choose X or O
while maker!= 'x' and maker!='o': 
	maker = input ('player1,choose x or o:')
# Assign player 2, the apposire maker

player1 = maker

if player1 == 'x':
	player2 = 'o'
else:
	player2 = 'x'
return (player1,player2)

player_input()

