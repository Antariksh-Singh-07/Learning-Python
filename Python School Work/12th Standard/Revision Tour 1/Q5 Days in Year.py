def day_calc(day_no_inp, day_inp):
    days_to_add = (day_no_inp-1)%7
    days = {'Sun':'Sunday', 'Mon':'Monday', 'Tue':'Tuesday', 'Wed':'Wednesday', 'Thu':'Thursday', 'Fri':'Friday', 'Sat':'Saturday'}
    day_index = list(days).index(day_inp)
    solution = days_to_add + day_index
    if solution>6:
        solution-=7
    return days[list(days)[solution]]
    
day_no_inp = int(input("Input the day number of a Year [2-365]: "))
day_inp = input("Input the first day of the Year: [Sun, Mon, Tue, Wed, Thu, Fri, Sat]: ").title()
print(f"on day {day_no_inp} the day was {day_calc(day_no_inp,day_inp)}")