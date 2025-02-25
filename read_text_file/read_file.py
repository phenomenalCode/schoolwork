#creating a variable that uses the function open  a file and return data and reading it with the r w string
#creating an formatted file that opens a file and pass a "w" string that lets use write inside the file.
f = open("customers-100.csv", "r")
formatted_file = open("customers_100.txt", "w") 
#creating variables that hold a decimal value of 20 and 50.
#creating a variable that holds the valur of keyword true
shortw = 20
longw = 50
is_first_line = True
#this is indicating that this variable is a boolian and its value is either true or false
#using forloop to iteriete over each line that is in inside the variable f.
    #inside the forloop we are creating a variable i which we will be using as an index in the body of the while loop
    #creating two fariables inside th for loop that are equal too empty strings
 
        #if i = i+1
                #if is_first_line and c is equal to string with space pass c to val. i = i+1

for ln in f:
#HERE WE ARE USING THE FOR LOOP TO ITERIETE EACH LINE IN F. WE WILL USE A WHILE LOOP TO IETERATE WHATS IN LN
#ln is declared in the for loop. for every line that we read from f we are assingning it to ln
    #print(ln)
    i = 0
    val = ""
    formatted_line = ""
    #these variables are set to an empty string
    while i < len(ln):
    #WHILE LOOP is saying this: while i is less than the lenght "len" off ln "the lines" ln. am confused as to what is being done inside the body of the while loop.
        #inside the body of the while loop we have an if statement that reads
        #setting a variable "c" its value is ln we are also passing the index from files to ln "lines"
        #if c is not = to a comma then we go into the if block. if c is then we go into the else block.
    #if i = i+1. we are incrementing the variable i by one
        c = ln[i]
        #setting the value of c to the charackter that recides in the ln string one charachter at a time. with the index.
        if c != ',':
        #only if c is NOT a comma the does the next statement get executed.
        
           #setting a variable "c" its value is ln we are also passing the index from files to ln "lines"
        #if c is not = to a comma          
            if is_first_line and c == ' ':
                c = '_'
            val += c
              #THIS STATEMENT HAS NO ELSEBLOCK
             #if the  first line is true then we move to the next concitional that also has to be true.
             #that is is the value of c a space. Note c is used while iterating so at some point this conditional may be true.
             # if both are true we use the if block otherwise we go to the next line of code.                 # And vs or and = both condiditions true or only one.
             #so is those conditions are true we replace empty space with underscore _
           #ADDING variable that c holds to val +=
        else:
            #setting trailing spaces to format the output
            l = len(val)
            #capturing lenght of string val
            #setting lenght of val into format val variable into different legnhts shortw = 20 longw = 50
            if l < shortw:
            #if legnght of val is less than less than shortw
                l = shortw - l
                # change value of l short - current value of l = l
            elif l < longw:
            # if l is less than 50 (longw)
                l = longw - l
                # longw - current l = l new variable
            else:
            #if non of other if statments are true 
                l = 100 - l
            #100 - l = new value of l
            #ljust function did not work after replacing the space with underscore,
            #have not understood why just yet
            #val_space = val.ljust(l,'-')
            #work around to ljust failures
            # if l = 12 we add 12 spaces. 
            spaced_val = val + " " * l
            # space times * value of l (0_0)
            formatted_line += spaced_val
            #formatted line is an empty string value of spaced_val add gets added  to formateted string with =+ not replacing
            val= ""
        i = i+1
    
    formatted_file.write(formatted_line + "/n") 
    # we are writing to formatted file with writte function and passing formatted line + new line character
    
    is_first_line = False    
f.close()
formatted_file.close()