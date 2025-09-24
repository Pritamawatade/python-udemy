def friendship_score(name1, name2):
      name1, name2 = name1.lower(), name2.lower()
      score = 0
      shared_letters = set(name1) & set(name2)
      print(f"shared letters: {shared_letters}  ")
      vowels = set('aeiou')

      score += len(shared_letters) * 5
      print(f"score = {score}")
      score += len(vowels  & shared_letters) * 10
      print(f"score = {score}")

      return min(score, 100)


print("Friendship calculator ##")

name = input("enter name 1")
name2 = input("enter name ")

score = friendship_score(name, name2)

print(f"\n score = {score}")

if(score > 70):
    print("You are like mouse and keyboard")
elif(score > 50):
    print("You are like coke and mentos")   
    
else:
    print("You are like oil and water")
    
    

