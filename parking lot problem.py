# def solution(start, leave):
#     price = 2
#     enter_hour = start[0:2]
#     enter_minute = start[3:5]
#     leave_hour = leave[0:2]
#     leave_minute = leave[3:5]
#     total_hour = int(leave_hour) - int(enter_hour)
#     total_minute = int(leave_minute) - int(enter_minute)
#     convert_hour = total_hour * 60
#     total_time = convert_hour + total_minute
#     print(total_time)
#     print(total_time % 60)
#     if total_time < 60:
#         price += 3
#     else:
#         price += 3
#         short_time = total_time - 60
#         short_hour = round((short_time/60))
#         price += (short_hour * 4)
#         if short_time % 60 > 0:
#             price += 4
#     return(price)
#
# print(solution("00:00", "23:59"))
#
# def solution(start, leave):
#     price = 2
#     enter_hour = start[0:2]
#     enter_minute = start[3:5]
#     leave_hour = leave[0:2]
#     leave_minute = leave[3:5]
#     total_hour = int(leave_hour) - int(enter_hour)
#     total_minute = int(leave_minute) - int(enter_minute)
#     convert_hour = total_hour * 60
#     total_time = convert_hour + total_minute
#     print(total_time)
#     if total_time < 60:
#         price += 3
#     else:
#         price += 3
#         short_time = total_time - 60
#         price += ((-(-short_time//60)) * 4)
#     return(price)
#
# print(solution("10:00", "13:21"))

# def solution(start, leave):
#     price = 2
#     enter_hour = start[0:2]
#     enter_minute = start[3:5]
#     leave_hour = leave[0:2]
#     leave_minute = leave[3:5]
#     total_hour = int(leave_hour) - int(enter_hour)
#     total_minute = int(leave_minute) - int(enter_minute)
#     convert_hour = total_hour * 60
#     total_time = convert_hour + total_minute
#     print(total_time)
#     if total_time < 60:
#         price += 3
#     else:
#         price += 3
#         short_time = total_time - 60
#         price += ((-(-short_time//60)) * 4)
#     return(price)
#
# print(solution("10:00", "13:21"))

def solution(start, leave):

    #gets us total time in min. final - initial
    total_min = (int(leave[0:2]) * 60 + int(leave[3:5])) - (int(start[0:2]) * 60 + int(start[3:5]))
    total_hr = int (total_min / 60)

    if total_min % 60:
        total_hr += 1

    if total_min != 0:
        return 5 + (total_hr - 1) * 4
    else:
        return 2

print(solution("10:00", "10:01"))