"""
1.车辆入场，扫描到车牌
2.判断该车牌在不在场内，如果已经在场内闸门不开启；并显示“车辆已经在场内！”
3.如果车辆未在场内，判断是否有剩余车位，如果没有剩余车位闸门不开启；并显示“车位已满！”
4.如果还有剩余车位，闸门开启；并显示“剩余车位”，“每小时收费价格”，”车牌号“，“入场时间”；剩余车位-1
5.车辆车牌和入场时间放入字典
6.车辆出场，扫描到车牌
7.显示“停车费”，“停车时长”，“入场时间”，“出场时间”
8.确认收费后闸门开启，剩余车位+1
"""
import time
import ast
import os.path


def open_gate(car_num):
    # do some action
    # to open the date
    print("欢迎光临！", car_num)


def writing_file_pz(parking_zone):
    with open("parking_zone.txt", "w", encoding="utf-8") as fo:
        fo.write(str(parking_zone))


def writing_file_ap(available_place):
    with open("available_place.txt", "w", encoding="utf-8") as fo:
        fo.write(str(available_place))


def in_parking(parking_zone, available_place, parking_price, car_num):
    if car_num in parking_zone:
        print("车辆已经在场内！")
    else:
        if available_place == 0:
            print("车位已满！")
        else:
            open_gate(car_num)
            in_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("剩余车位：", str(available_place) + "个")
            print("每小时收费：", str(parking_price) + "元")
            print("入场时间：", in_time)
            print("剩余车位：", available_place)
            available_place -= 1
            parking_zone[car_num] = in_time
            writing_file_pz(parking_zone)
            writing_file_ap(available_place)


if __name__ == "__main__":
    if os.path.exists("parking_zone.txt"):
        parking_zone_io = open("parking_zone.txt", "r", encoding="utf-8")
        parking_zone_str = parking_zone_io.readline()
        parking_zone = ast.literal_eval(parking_zone_str)
    else:
        parking_zone = {}
    if os.path.exists("available_place.txt"):
        available_place_io = open("available_place.txt", "r", encoding="utf-8")
        available_place_str = available_place_io.readline()
        available_place = int(available_place_str)
    else:
        available_place = 5
    parking_price = 10
    car_num = input("车牌已被扫描：")
    in_parking(parking_zone, available_place, parking_price, car_num)
