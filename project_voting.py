candidate1=input("Enter 1st candidate name:")
candidate2=input("Enter 2st candidate name:")
cand1_votes=0
cand2_votes=0
voters_id=[101,102,103,104,105,106,107,108,109,110]
no_of_voters=len(voters_id)
print("Number of voters:",no_of_voters)
voted=[]

while True:
    if voters_id==[]:
        print("Voting is over")
        if cand1_votes>cand2_votes:
            print(f"{cnadidate} won the election with {cand1_votes}")
        elif cand2_votes>cand1_votes:
            print("{candidate2} won the election with {cand2_votes}")
        elif cand1_votes==cand2_votes:
            print(" Tied !!")
        break
    
    else:
        voter=int(input("Enter your voter id:"))
        if voter in voted:
            print("Not allow to vote becoz you are already voted")
        else:
            if voters in voters_id:
                print(f"1.{cnadidate1}\n2.{candidate2}")
                choice=int(input("Enter your choice number for voting"))
                if choice==1:
                    cand1_votes+=1
                    print(f"You voted for{candidate1}")
                elif choice==2:
                    cand2_votes+=1
                    print(f"You voted for{candidate2}")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("You are not allow to vote becoz you are not voter")




    
