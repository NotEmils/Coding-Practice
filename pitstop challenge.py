#inputs
time = input("How many seconds was the race? ")
no_of_pitstops = input("How many pitstops were made? ")
avg_time_of_pitstops = input("How long were the pitstops on average? ")

#Calculations
total_pitstop_time = float(no_of_pitstops) * float(avg_time_of_pitstops)
percentage_of_race = round((float(total_pitstop_time)*100)/float(time),2)

#Results
print("Time spent in the pits: ",total_pitstop_time)
print("Percentage of race spent in the pits: ", percentage_of_race)
if percentage_of_race > 5:
    print("You need a new pit crew!")