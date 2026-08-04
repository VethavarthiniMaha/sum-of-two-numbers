 colours=input("Enter Colours Name:").split()
 print("List of Colours:",colours)
 print("Size of list:",len(colours))
 max_words=colours[0]
 min_words=colours[0]
 for word in colours:
 if len(word)>len(max_words):
        max_words=word
 if len(word)<len(min_words):
        min_words=word
 print("Greatest word:",max_words)
 print("Smallest word:",min_words)
 total=0
 for word in colours:
   total+=len(word)
  print("Sum of lengths:",total)
