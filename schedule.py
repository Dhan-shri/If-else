time=float(input("enter a time"))
# time is given in 24 format 
if time>6 and time<=7:
    print("morning exercise")
elif time>7 and time<=8.30:
    print("breakfast")
elif time>8.30 and time<=9.30:
    print("english activity")
elif time>9.30 and time<=13:
    print("coding time")
elif time>13 and time<=14.30:
    print("lunch break")
elif time>14.30 and time<=17:
    print("study")
elif time>17 and time<=19:
    print("cultural time")
elif time>19 and time<=21:
    print("study coding time")
elif time>21 and time<=22:
    print("dinner time")
elif (time>22 and time<=24) or (time>=1 and time<=6):
    print("personnel time")
else:
    print("time is not valid")