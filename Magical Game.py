import random
print("\n\t\t\t\t\t%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
      "\n\t\t\t\t\t%%%%%%%%%%% Lets Play a game %%%%%%%%%%%%%"
      "\n\t\t\t\t\t%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

getNumber=input("\nAap koi number socha."
                "\nwrite here and then press ENTER : ")
getFriendNumber=input("\nJo number aap na socha hai same number  apna dost ka add kar la. "
                      "\nAnd then press ENTER : ")
random_even = random.randrange(2, 21, 2)

myNumber=input(" \nya mera number add kara la  : " +str(random_even) )
donate=input("\nab jo aap ka pass total hoe hai in ma sa half donate kar da: ")
show=input("\nJo aap na apna dost ka add kye tha on ko return kar da : ")

print("\nAb aap ka pass atna hai:" + str(int(random_even/2)))
answer= input("kia ya he answer hai Yes/No:")


end=" \nYou don't compete with me "
print(end)
