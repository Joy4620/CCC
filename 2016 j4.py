meters = 120
clock = input().split(':')
clock = int(clock[0])*60 + int(clock[1])
rush_hour = [[420, 600], [900, 1140]]

while meters:
    if (clock >= rush_hour[0][0] and clock < rush_hour[0][1]) or (clock >= rush_hour[1][0] and clock < rush_hour[1][1]):
        clock += 20
        meters -= 10
    else:
        if meters < 20:
            clock += meters
            meters = 0
        else:
            meters -= 20
            clock += 20

print((f'0{str((clock//60)%24)}' if len(str((clock//60)%24)) == 1 else str((clock//60)%24)) + (f':0{str(clock%60)}' if len(str(clock%60)) == 1 else f':{str(clock%60)}'))
