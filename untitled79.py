seconds = 7755
if seconds < 60:
    print(seconds)
elif seconds < 3600:
    minutes = seconds//60
    seconds = seconds - 60*minutes
    print(f"{minutes} minutes and {seconds} seconds")
elif seconds < 86400:
    hours = seconds//3600
    print(hours)
    seconds = seconds - hours * 3600
    print(seconds)
    if seconds > 60:
        
        minutes = seconds//60
        print(minutes)
        seconds = seconds - 60*minutes
        print(seconds)
        if hours > 1 and minutes > 1 and seconds > 1:
            print(f"{hours} hours {minutes} minutes and {seconds} seconds")
        elif hours > 1 and minutes > 1 and seconds == 1:
            print(f"{hours} hours {minutes} minutes and {seconds} second")
        elif hours >1 and minutes == 1 and seconds > 1:
            print(f"{hours} hours {minutes} minute and {seconds} seconds")
        elif hours == 1 and minutes > 1 and seconds >1:
            print(f"{hours} hour {minutes} minutes and {seconds} seconds")
        elif hours > 1 and minutes == 1 and seconds == 1:
            print(f"{hours} hours {minutes} minute and {seconds} second")
        elif hours == 1 and minutes == 1 and seconds == 1:
            print(f"{hours} hour {minutes} minute and {seconds} second")
    elif seconds < 60:
        
        if hours > 1 and seconds > 1:
            print(f"{hours} hour and {seconds} seconds")
        elif hours > 1 and seconds == 1:
            print(f"{hours} hour 74 {seconds} second")
        elif hours == 1 and seconds == 1:
            print(f"{hours} hour and {seconds} second")
    else:
        if hours > 1:
            print(f"{hours} hours")
        else:
            print(f"{hours} hours")
elif seconds < 31536000 :
    days = seconds //3600
    seconds = seconds - days*3600
    if seconds > 3600:
        hours = seconds // 3600
        seconds = seconds - hours*3600
        