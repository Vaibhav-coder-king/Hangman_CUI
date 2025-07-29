import random as r
import pyfiglet as p

def display(n_wrong):
	print("*********************************************")
	print("                     |                       ")
	h_pic=[["                                             ","                                             ","                                             "],
	["                     0                       ","                                             ","                                             "],
	["                     0                       ","                     |                       ","                                             "],
	["                     0                       ","                    /|                       ","                                             "],
	["                     0                       ","                    /|\\                     ","											   "],
	["                     0                       ","                    /|\\                     ","                    /                        "],
	["                     0                       ","                    /|\\                     ","                    / \\                     "]]
	
	for i in h_pic[n_wrong]:
		print(i)
	print("*********************************************")
	print("Guess the word:-\n")

def win_chk():
	if n_wrong==6:
		return False 
	elif a==list(word ):
		return True
		
def get_words():
	with open(r"hangman_words.txt","r") as f:
		wrd=f.readlines()
		s=[]
		for w in wrd[:-1]:
			s.append(w[:-1])
		s.append(wrd[-1])
		return s
			

def main():
	global n_wrong,a,word 
	word=r.choice(get_words())
	l=len(word)
	a=[]
	comment=""
	r_word=[]#wrong words 
	n_wrong=0
	for k in range(l):
		a.append("_")
	while True:
		print(p.figlet_format("Hangman",font="slant"))
		display(n_wrong)
		print(f"\n {6-n_wrong} chances Left.\n")
		print("<",end=" ")
		for m in a:
			print(m,end=" ")
		print(">")
		if win_chk():
			print("You Win 🏆")
			break
		elif win_chk() is False:
			print ("You Lose.")
			print(f"Correct words is {word.capitalize()}")
			break
		print(comment)
		comment=""
		ask=input("\nenter your choice:").lower()
		if ask in word and len(ask)==1:
			if ask in a and ask!="_":
				comment=f"{ask} is already guess."
			for f in range(l):
				if word[f]==ask:
					a[f]=ask
		elif ask==word :
			for f in range(l):
				if word [f]==ask[f]:
					a[f]=ask[f]
		else:
			n_wrong+=1
			comment=f"{ask} is not correct guess."
		
		
if __name__=="__main__":
	play=True 
	while play:
		main()
		while True:
			ask=input("wanna play again🤔?").lower()
			if ask=="y":
				break
			elif ask=="n":
				play=False
				break
			else:
				print("plz,input y or n.")
	print(p.figlet_format("Bye-bye",font="small"))
