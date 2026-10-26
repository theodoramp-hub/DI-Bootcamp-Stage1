human_years = int(input("How many years ago did you get your pets? "))

if  human_years == 1:
    print([1,15,15])
elif human_years == 2:
    print([2,24,24])
else:
    print([human_years, 24 + (human_years-2)*4, 24  + (human_years-2)*5])
    
