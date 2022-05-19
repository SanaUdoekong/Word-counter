on = True
while on: 
    #text
    sample_text = input("Enter the some text: ")

    #calculating the number of words
    result = len(sample_text.split())

    #displaying the result
    print("There are " + str(result) + ' words in the sentence: "' + sample_text + '"')

    switch = input("Enter 'q' to exit, and 'c' to continue. ")
    if switch == 'q':
        on = False
