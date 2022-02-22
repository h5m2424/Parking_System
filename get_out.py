"""
1.车辆出场，扫描到车牌
2.判断车辆在不在字典里，如果不在提示“没有车辆入场纪录，请咨询保安！”。
3.如果车辆在字典里，显示“停车费”，“停车时长”，“入场时间”，“出场时间”
4.确认收费后闸门开启，从字典里删除车辆，剩余车位+1
"""
from datetime import datetime
import ast
import os.path


def open_gate(car_num):
    # do some action
    # to open the gate
    print("一路顺风！", car_num)


def writing_file_pz(parking_zone):
    with open(".\\parking_zone.txt", "w", encoding="utf-8") as fo:
        fo.write(str(parking_zone))


def writing_file_ap(available_place):
    with open(".\\available_place.txt", "w", encoding="utf-8") as fo:
        fo.write(str(available_place))


def out_parking(parking_zone, available_place, parking_price, car_num):
    if car_num not in parking_zone:
        print("未查询到入场纪录，请联系门卫人员！")
    
    else:
        out_time = datetime.today()
        parking_time_in_second = (out_time - datetime.strptime(parking_zone[car_num], "%Y-%m-%d %H:%M:%S")).seconds

        if parking_time_in_second / 3600 < 1: # 1小时免收停车费
            print("停车时长：", parking_time_in_second / 3600, "小时")
            open_gate(car_num)
            available_place += 1
            parking_zone.pop(car_num)
            writing_file_pz(parking_zone)
            writing_file_ap(available_place)

        else:    
            print("每小时收费：", parking_price, "元")
            print("停车时长：", parking_time_in_second / 3600, "小时")
            print("停车费用：", parking_time_in_second / 3600 * parking_price, "元")
            pay = int(input("请交费:"))
            while pay < parking_time_in_second / 3600 * parking_price:
                pay = int(input("请交费:"))
            else:
                open_gate(car_num)
                available_place += 1
                parking_zone.pop(car_num)
                writing_file_pz(parking_zone)
                writing_file_ap(available_place)


if __name__ == "__main__":
    if os.path.exists(".\\parking_zone.txt"):
        parking_zone_io = open(".\\parking_zone.txt", "r", encoding="utf-8")
        parking_zone_str = parking_zone_io.readline()
        parking_zone = ast.literal_eval(parking_zone_str) #
    else:
        parking_zone = {}
    
    if os.path.exists(".\\available_place.txt"):
        available_place_io = open(".\\available_place.txt", "r", encoding="utf-8")
        available_place_str = available_place_io.readline()
        available_place = int(available_place_str)
    else:
        available_place = 50 # 车位总数
    
    parking_price = 10 # 每小时停车费
    car_num = input("车牌已被扫描：")
    out_parking(parking_zone, available_place, parking_price, car_num)
