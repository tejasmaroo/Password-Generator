# Tasks 
The PyPassword Generator is a python based password generator. It is used to create a strong and randimized password.
In the code, first wwe start by importing the random module.Then we create 3 lists- letters numbers and symbols.
Then we create an empty list named pwlist.We then take input from the user on the number of  letters number and symbols required in the password.
We run three for loops, each for letters, numbers and symblols. First we use the range function, for example in the first for loop we use range function from 1 to number of letters taken input + 1. Inside the loop first we use the append function to make changes in the pwlist then we use the random.choice funtion to select a random letter from the letters list.
Repeat this same logic for numbers and symbol loops.
By using the random.shuffle function we shuffle the position of the elements in the pwlist.
Then we initialize an empty string named pw, by looping though each element in the pwlist, we store them inside the pw string.
We finally print pw using f strings to dislay the randomised  password generated.
