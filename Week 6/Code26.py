fruit = "banana" ##we are trying to parse this string
index = 0 ##we are parsing this string using an index where we tell the program what to do
while index < len(fruit): ##we create an infinite loop telling the program to start at while but always stay less than the length of our string
    letter = fruit[index] ##we are telling the program what to do here
    print index, letter ##we are telling the program to print the index used and the letter, 
    index = index + 1 ##this is our iteration variable for the while loop or our increment for the index once one iteration is properly executed
    