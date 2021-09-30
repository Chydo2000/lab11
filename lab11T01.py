def time(seconds):
    hrs = int(seconds / 3600)    
    mins = int(seconds % 3600 / 60)
    secs = int(seconds % 3600 % 60)


    if hrs < 10:
        hrs = "0"+ str(hrs)
    if mins < 10:
        mins = "0"+ str(mins)
    if secs < 10:
        secs = "0"+ str(secs) 
        
    return (str(hrs) + ":" + str(mins) + ":" + str(secs))
print(time(10000))