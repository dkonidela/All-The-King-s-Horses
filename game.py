
'''
@author; Dileep Konidela
'''
import copy
possible_moves=[[1,-2],[-1,-2],[-2,-1],[-2,1]]

'''
get the next possible state
'''
def get_new_state(player_state,state,index):
	
	state=state-1

	player_state[index][0]=player_state[index][0]+possible_moves[state][0]
	player_state[index][1]=player_state[index][1]+possible_moves[state][1]

	#print player_state
	if (player_state[index][0] >=0) and (player_state[index][1]>=0):

		#Checking if there is any overlap
		i=0
		
		while i < 4:
			j=i+1
			while j < 4:
				#
				if player_state[i][0]==player_state[j][0] and player_state[i][1]==player_state[j][1]:
					return None
				j=j+1
			i=i+1

		return player_state

	return None

'''
implements the play functionality
'''
def play(player_state,turn,alpha,beta):
	 #print "entered play"
	 if turn==1:
		player_state=best_move_evaluation1(player_state,1,1,-1)
		if player_state==None:
      #			print "inside turn 1"
			#print "player 2 Wins"
			return
		else:
			#print "Player 2 Wins "
			print player_state
			print "---------------------------"

	 else:
		player_state=best_move_evaluation1(player_state,2,1,-1)
		if player_state==None:
      #			print "inside 2"
			#print "player 1 Wins"
			return
		else:
			#print "Player 1 Wins "
			print player_state
			print "---------------------------"


'''
implements different evaluaton funtion which is called by play function
'''

def best_move1(player_state,turn):
	if turn==1:
		#Finding the best move
		max_dis=0
		a=0
		mov=0
		max_dis=0

		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,0)

			if new_player_state!=None:
				temp_dis=(new_player_state[0][0]+new_player_state[0][1])

				if max_dis < temp_dis:
					max_dis=temp_dis
					a=0
					mov=x
			x=x+1
		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,1)
			
			if new_player_state!=None:
				temp_dis=(new_player_state[1][0]+new_player_state[1][1])
				if max_dis < temp_dis:
					max_dis=temp_dis
					a=1
					mov=x
			x=x+1

		new_player_state=copy.deepcopy(player_state)
		#Moving in the direction of best move
		new_player_state=get_new_state(new_player_state,mov,a)
		return new_player_state
	else:
		#Finding the best move
		max_dis=0
		a=0
		mov=0
		max_dis=0
		x=1

		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			#print new_player_state
			new_player_state=get_new_state(new_player_state,x,2)
			if new_player_state!=None:
				temp_dis=(new_player_state[2][0]+new_player_state[2][1])

				if max_dis < temp_dis:
					max_dis=temp_dis
					a=2
					mov=x
			x=x+1

		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,3)
			#print new_player_state
			if new_player_state!=None:
				temp_dis=(new_player_state[3][0]+new_player_state[3][1])
				if max_dis < temp_dis:
					max_dis=temp_dis
					a=3
					mov=x
			x=x+1

		new_player_state=copy.deepcopy(player_state)
		new_player_state=get_new_state(new_player_state,mov,a)
		return new_player_state


def best_move_evaluation1(player_state,turn,alpha,beta):
	
	if turn==1:
		print "player 1"
		#Finding the best move
		max_dis=0
		a=0
		mov=0
		max_dis=0

		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,0)
		
			if new_player_state!=None:
				temp_dis=(new_player_state[0][0]*new_player_state[0][0])+(new_player_state[0][1]*new_player_state[0][1])

				if max_dis < temp_dis:
					max_dis=temp_dis
					a=0
					mov=x
			x=x+1
		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,1)
			
			if new_player_state!=None:
				temp_dis=(new_player_state[1][0]*new_player_state[1][0])+(new_player_state[1][1]*new_player_state[1][1])
				if max_dis < temp_dis:
					max_dis=temp_dis
					a=1
					mov=x
			x=x+1

		new_player_state=copy.deepcopy(player_state)
		#Moving in the direction of best move
		new_player_state=get_new_state(new_player_state,mov,a)
		print new_player_state
		if new_player_state==None:
      			print "player 2 wins"
			return None

		print "__________________________________"
		
		res=best_move_evaluation1(new_player_state,2,alpha,beta)
		
		if res > beta: 
			if a==0:
				beta=mov
				return beta
			else:
				beta=mov+4
				return beta
		return None

	else:
		print "player 2"
		#Finding the best move
		max_dis=0
		a=0
		mov=0
		max_dis=0
		x=1

		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			#print new_player_state
			new_player_state=get_new_state(new_player_state,x,2)

			if new_player_state!=None:
				temp_dis=(new_player_state[2][0])+(new_player_state[2][1])

				if max_dis < temp_dis:
					max_dis=temp_dis
					a=2
					mov=x
			x=x+1

		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,3)
			#print new_player_state
			if new_player_state!=None:
				temp_dis=(new_player_state[3][0])+(new_player_state[3][1])
				if max_dis < temp_dis:
					max_dis=temp_dis
					a=3
					mov=x
			x=x+1

		new_player_state=copy.deepcopy(player_state)
		#Moving in the direction of best move
		new_player_state=get_new_state(new_player_state,mov,a)

		print new_player_state
		print "__________________________________"
		if new_player_state==None:
      			print "player 1 wins"
			return None
		
		res=best_move_evaluation1(new_player_state,1,alpha,beta)


		if res < alpha: 
			if a==0:
				alpha=mov*-1
				return alpha
			else:
				alpha=(mov+4)*-1
				return alpha

		
    	return None

'''
implements the recursive minimax with alpha beta prunning
'''

def best_move(player_state,turn):
	
	#For turn 1
	if turn==1:
		#For horse1 of player 1
		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,0)
			if new_player_state!=None:
				res=best_move(new_player_state,2)
				if res > 0: 
					return x
			x=x+1
		#For horse 2 of player1
		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,1)
			
			if new_player_state!=None:
				res=best_move(new_player_state,2)
				if res > 0:
					return x+4
			x=x+1

		return -10

	#For turn 2
	elif turn==2:

		#For Horse1 of player1
		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,2)
			if new_player_state!=None:
				res=best_move(new_player_state,1)
				#print x
				if res < 0: 
					return x*-1
			x=x+1

		#For horse 2 of player1
		x=1
		while x <= 4:
			new_player_state=copy.deepcopy(player_state)
			new_player_state=get_new_state(new_player_state,x,3)
			if new_player_state!=None:
				res=best_move(new_player_state,1)
				#print x
				if res < 0: 
					return (x+4)*-1
			x=x+1


		return 10
'''
displays the next best move
'''
def display_best_move(player_state,move,turn):
	if turn==1:
		
		if move < 4:
			print "Horse1"
			print " ( "+ str(player_state[0][0])+","+str(player_state[0][1])+" ) -->  ( "+ str(player_state[0][0]+possible_moves[move-1][0])+" ,"+ str(player_state[0][1]+possible_moves[move-1][1])+" )"
		else:
			print "Horse2"
			print " ( "+ str(player_state[1][0])+","+str(player_state[1][1])+" ) -->  ( "+ str(player_state[1][0]+possible_moves[move-5][0])+" ,"+ str(player_state[1][1]+possible_moves[move-5][1])+" )"
	else:
		if move < 4:
			print "Horse1"
			print " ( "+ str(player_state[2][0])+","+str(player_state[2][1])+" ) -->  ( "+ str(player_state[2][0]+possible_moves[move-1][0])+" ,"+ str(player_state[2][1]+possible_moves[move-1][1])+" )"
		else:
			print "Horse2"
			print " ( "+ str(player_state[3][0])+","+str(player_state[3][1])+" ) -->  ( "+ str(player_state[3][0]+possible_moves[move-5][0])+" ,"+ str(player_state[3][1]+possible_moves[move-5][1])+" )"


def main():
	
	command=input("Play the Game with Evaluation functions or not. Enter 1 : With Evaluation \n 2: Without Evaluations")
	turn=input("Enter player turn")
	player_state=[]
	
	h1x=input()
	h1y=input()
  
	h2x=input()
	h2y=input()
  
	h3x=input()
	h3y=input()
  
	h4x=input()
  	h4y=input()
  
	h1=[]
	h1.append(h1x)
	h1.append(h1y)
	
	h2=[]
	h2.append(h2x)
	h2.append(h2y)
	
	h3=[]
	h3.append(h3x)
	h3.append(h3y)

	h4=[]
	h4.append(h4x)
	h4.append(h4y)

	player_state.append(h1)
	player_state.append(h2)
	player_state.append(h3)
	player_state.append(h4)

	if command == 1:
		play(player_state,turn,1,-1)
	else:	
	  res=best_move(player_state,turn)

	  if turn==1 and res < 0:
		  print "player 1 loses"
		  #print "No Best cases possible"
	  elif turn==1 and res > 0:
		  print "player 1 Wins!!"
		  display_best_move(player_state,res,1)
		  #print res
	  elif turn==2 and res > 0:
		  print "player 2 loses"
		  #print "No Best case possible"
	  else:
		  print "Player 2 Wins"
		  display_best_move(player_state,res*-1,2)
		  #print res

if __name__ == '__main__':
	main()

