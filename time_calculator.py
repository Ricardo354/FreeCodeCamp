def add_time(start, duration,day=''):
    week = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday' : 3,
        'friday' : 4,
        'saturday' : 5,
        'sunday' : 6,
    }

    addmin = int(start.split()[0].split(':')[1]) + int(duration.split()[0].split(':')[1]) 
    addhour = int(start.split()[0].split(':')[0]) + int(duration.split()[0].split(':')[0])
    starting_point = start.split()[1]
    ampm = 'AM'

    
    if addmin > 59:
        while addmin > 59:
            addmin -= 60
            addhour += 1
    if starting_point == 'PM':
        addhour += 12

    addmin = addmin if addmin > 9 else '0' + str(addmin)
    days = int(addhour // 24)
    endHour = addhour % 24

    if endHour > 11:
        ampm = 'PM'
    
    
    if endHour > 12:
        endHour -= 12
    elif endHour == 0:
        endHour = 12
    
    

    new_time = f'{endHour}:{addmin} {ampm}'
    
#if day, return index, then add index with n of days

    if day:
        day = day.lower()
        index = week[day]
        n = int(days + index) % 7
        day = list(week.keys())[list(week.values()).index(n)]
        new_time += f', {day.title()}'


    if days:
        if days != 1:
                new_time += f" ({days} days later)"
        else:
                new_time += f' (next day)'
    

   


    return new_time 


if __name__ == '__main__':
        print(add_time("11:59 PM", "24:05", "Wednesday"))



