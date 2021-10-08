from datetime import datetime
import math
def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    parking_info_dict = {}
    for record in records:
        time = record.split(' ')[0]
        car_num = record.split(' ')[1]
        if car_num in parking_info_dict:
            parking_info_dict[car_num].append(time)
        else:
            parking_info_dict[car_num] = [time]
    for parking_info in parking_info_dict:
        if len(parking_info_dict[parking_info]) % 2 == 1:
            parking_info_dict[parking_info].append('23:59')
    parking_info_dict = dict(sorted(parking_info_dict.items(), key=lambda x: x[0]))
    total_time_info_dict = {}
    for parking_info in parking_info_dict:
        parking_time_list = parking_info_dict[parking_info]
        total_time = 0
        for i in range(0, int(len(parking_time_list)/2)):
            in_time = datetime.strptime(parking_time_list[i*2], "%H:%M")
            out_time = datetime.strptime(parking_time_list[i*2+1], "%H:%M")
            time_difference = str(out_time - in_time)
            total_time += int(time_difference.split(":")[0])*60 + int(time_difference.split(":")[1])
        total_time_info_dict[parking_info] = total_time
    for car_num in total_time_info_dict:
        total_time = total_time_info_dict[car_num]
        if total_time_info_dict[car_num] < basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + math.ceil((total_time - basic_time) / unit_time) * unit_fee)