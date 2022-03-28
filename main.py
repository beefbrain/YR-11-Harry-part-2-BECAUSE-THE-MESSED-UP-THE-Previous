#sets and dictionaries 

#dictionary of all the characters all characters have the same value of 0 so i found a finction that is a short cut for this
char_score = {}.fromkeys(["Hermioni Granger", "Harry Potter", "Ron Weasley", "Draco Malfoy", "Neville Longbottom", "Luna Lovegood", "Cedric Diggory", "Fred and George Weasley", "Ginny Weasley" ], 0)

print ("Who would you want to be friends with?")
print ("--------------------------------------")
print ("someone who is a bit of a bad influence, breaking rules are part of the fun")
print ("Enter 0")
print ("Someone who is a good influence so they can encurage me to stay on track")
print ("Enter 1")
print ("Someone a bit quiet and down to earth, they are very relaxing to hang out with")
print ("Enter 2")
#what id id to make this work was made my while and if statememnt more specific and added the input in the loop which i didn't do before.
ans = int(input("Enter your option here: "))
  
while ans > 2:
    print("That is not an option, try again")
    ans = int(input("Enter your option here..."))
    if ans <=2:
     break

print("   ")
  
bad_boy_girl = {"Harry Potter", "Draco Malfoy", "Ginny Weasley"} 
gd_influ = {"Hermioni Granger", "Neville Longbottom", "Ginny Weasley"} 
quiet = {"Neville Longbottom", "Luna Lovegood", "Cedric Diggory"} 
ans_set = {}

if ans == 0:
  for character in bad_boy_girl:
    char_score[character] +=1
elif ans == 1:
    for character in gd_influ:
      char_score[character] +=1
elif ans == 2:
  for character in quiet:
    char_score[character] +=1

print (char_score)





 #This is where i do the same thing for the rest of the questions





  
  
