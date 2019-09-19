from datetime import datetime
time1 = "19:00"
time2 = "20:59"
time3 = "21:00"
time4 = "18:59"
time5 = "23:59"
time6 = "00:00"
new_t1 = datetime.strptime(time1, "%H:%M")
new_t2 = datetime.strptime(time2, "%H:%M")
new_t3 = datetime.strptime(time3, "%H:%M")
new_t4 = datetime.strptime(time4, "%H:%M")
new_t5 = datetime.strptime(time5, "%H:%M")
new_t6 = datetime.strptime(time6, "%H:%M")
def parking_side(day, hour):
    h = datetime.strptime(hour, "%H:%M")
    if new_t1 < h < new_t2:
        return "both sides"
    elif day % 2 == 0 and new_t3 < h < new_t5:
        return "left"
    elif day % 2 != 0 and new_t3 < h < new_t5:
        return "right"
    elif day % 2 == 0 and new_t6 < h < new_t4:
        return "right"
    elif day % 2 != 0 and new_t6 < h < new_t4:
        return "left"
print(parking_side(2, "19:30"))
print(parking_side(2, "21:30"))
print(parking_side(3, "18:58"))
print(parking_side(3, "21:03"))
print(parking_side(2, "18:54"))


