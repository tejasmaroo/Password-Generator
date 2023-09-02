# Tasks 
The PyPassword Generator is a python based password generator.
It helps us to create a completely randomised and a strong password.
The basic logic used by the program is that it takes input from the user of how many number of letters numbers
and symbols are required. Then it loops through the individual lists of letters numbers and sysmbols. 
These list consist of all the letters symbols and numbers present on the keyboard.
The loop runs using the range funtion, which ranges from 1 to number of letters/numbers/symbols enterd by user + 1.
Inside the loop we first use the append function to append the empty list "pwlist" created earlier.
Then we use the random.choice function to select any random element from the lists 