import datetime

week_days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
week_days_dict={"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
thirty_days_month=[5, 7, 10 , 11]
month=datetime.datetime.now().month

def speechtodate(var):
    """This function takes in text information and convert it to the date"""
    today=datetime.datetime.today()
    day_index=today.weekday()+1
    year=datetime.datetime.now().year
    day=datetime.datetime.now().day
    month=datetime.datetime.now().month
    if 'today' in var:
        return str(year)+"-"+str(month)+"-"+str(day)
    elif "tomorrow" in var:
        day=day+1
        return str(year)+"-"+str(month)+"-"+str(day)
    elif "yesterday" in var:
        day=day-1
        return str(year)+"-"+str(month)+"-"+str(day)
    elif "next" in var or "next week" in var:
        end_week=7-day_index
        end_week_index=end_week+day
        for days in week_days:
            for spday in var.split():  
                if days == spday:
                    add_index=week_days_dict[days]
                    day=end_week_index+add_index
                    if month in thirty_days_month and day>30:
                        day=day-30
                        month=month+1
                        return str(year)+"-"+str(month)+"-"+str(day)
                    else:
                        return str(year)+"-"+str(month)+"-"+str(day)
        return None
           
    elif 'monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday' or 'saturday' or 'sunday' in var:
        for dy0 in week_days:
            for dy1 in var.split():
                if dy0==dy1:
                    add=week_days_dict[dy1]
                    dif=add-day_index
                    day=day+dif
                    return str(year)+"-"+str(month)+"-"+str(day)
        return 0
    else:
        return 0

            