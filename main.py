from datetime import date
exit = "YES" #Yes by default so user can get in loop
current_year = date.today().year #Getting Current Year
while exit == "YES": #Puts user in a loop
 print("This is a simple age calculator")
 birth_year = int(input("What year were you born?")) #Stores User Birth Year In a Variable
 age = current_year - birth_year #Subtract Current Year by Birth Year to get age
 print("Your age is", age)
 exit = input("Do you want to use age finder again? ").upper() #Asks user if want to exit
if exit == "NO":
  print("Program ended successfully ")
else:
  print("Invalid input enter yes or no")
