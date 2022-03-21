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
ans = int(input("Enter your option here..."))
while ans > 2:
  print("That is not an option, try again")
  ans = int(input("Enter your option here..."))
  if ans <=2:
   break
  
bad_boy_girl = {"Harry Potter", "Draco Malfoy", "Ginny Weasley"} 
gd_influ = {"Hermioni Granger", "Neville Longbottom", "Ginny Weasley"} 
quiet = {"Neville Longbottom", "Luna Lovegood", "Cedric Diggory"} 
ans_set = {}

if ans == 0:
    ans_set = bad_boy_girl
elif ans == 1:
    ans_set = gd_influ
elif ans == 2:
  ans_set = quiet

# the keys in the the dictionary char_score is the same to the value of all of the sets. i need to use a for loop to link them as the for loop will check the dictionary keys one after the other.

for character in ans_set:
#character holds the values in ans_set

  char_score[character] +=1
#print (char_score)
#printing to test if the vaules are added up correctly 



  

#printing wish chacaters have the most points (could be sigle character, could be multiple)




  

#I need to order the dictionary from largest to smallest and i found a format for that.

sort_char_score = sorted(char_score.items(), key=lambda x: x[1], reverse=True)

print (sort_char_score)
#this is to see if the format worked

#i need to see if there are any ties and if there are i need to print them. 

#for this i will use a while loop only going the length of the set and see now many of the values after the first is equal to the first

i = 0
# i will be the amount of ties
while i < len(sort_char_score)
  first_key = list(sort_char_score)[i] 
  next_key = list(sort_char_score)[i+1]
#^this goes on until there are no ties, if there are no ties, the loop will be broken
  if first_key == next_key
    break

#I print the results here

#I need to print the key of the sorted dictionary up to 'i' place holder 
# i will be using a for loop for this

for j range(i)
first_key = list(sort_char_score)[j]
#i am only printing the keys
print (firt key [0])