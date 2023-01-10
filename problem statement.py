# def construct_hotel_rooms(nfloor, nroomInEachFloor):
#
#     roomNumber = 1
#     roomArrangement = []
#
#     for I in range(nfloor):
#         t = []
#         roomArrangement.append(t)
#         for J in range(nroomInEachFloor):
#             t.append(roomNumber)
#             roomNumber += 1
#     return roomArrangement
#
# def print_room_arrangements(hotel):
#     print(hotel)
# def main():
#
#     nhotels = int(input("Enter the number of hotels: "))
#     for I in range(nhotels):
#         print(f"Enter the values for hotel {I+1}")
#         nfloor = int(input("Enter the number of floors: "))
#         nroomsInEachFloor = int(input("Enter the number of rooms in each floor: "))
#         hotel = construct_hotel_rooms(nfloor, nroomsInEachFloor)
#         print(hotel)
#         u_val=int(input('Enter room number: '))
#         for i in range(len(hotel)):
#             if u_val in hotel[i]:
#                 print('Your room is on Floor ',hotel.index(hotel[i]),' .')
#
#
#
#
# main()




# there are three persons wants to book room in three different hotel.the room number for all three should be same.
# 1) A wants to book the room in hotel A which is having 5 floor and total 50 rooms and only multiple of 5
# 2) B wants to book the room in hotel B which is having 7 floor and 49 room and only multiple of 7
# 3) there is no restrictions for C , he can book anyone in hotel C which is of 8 floor with 7 room in each

# Now display the booked room number with the persons and the floor name including hotel

# from math import lcm

from math import gcd


# list1 = [12,48,8,60]
# lcm = list1[0]
# for i in list1[1:]:
#   lcm = int(lcm*i/gcd(lcm, i))
# print("least common multiple =  ", lcm)

def hotel(floor, rooms):
    hota = []
    rooms_per_floor = int(rooms / floor)
    a = 1
    for j in range(1, int(floor + 1)):
        # floor = j
        b = a + rooms_per_floor
        ls = [i for i in range(a, b)]
        a += rooms_per_floor
        b = a + rooms_per_floor
        hota.append(ls)
    return hota


# def room_no(a, b):
#     return lcm(a,b)

def bot():
    n = int(input('Enter the number of Hotels:'))
    hotel_ls = []
    hotelname_ls = []
    lcm_list = []
    for i in range(1, n + 1):
        hotelname_ls.append('hotel' + str(i))
        Dynamic_Variable_Name = hotelname_ls[i - 1]
        floor = input("Enter the desired floor:")
        rooms = input("Enter the desired rooms:")
        multi = int(input("Enter the desired multiple:"))
        lcm_list.append(multi)
        globals()[Dynamic_Variable_Name] = hotel(int(floor), int(rooms))
        hotel_ls.append(globals()[Dynamic_Variable_Name])

    lcm = lcm_list[0]
    for i in lcm_list[1:]:
        lcm = int(lcm * i / gcd(lcm, i))
    # print("least common multiple =  ", lcm)
    room = lcm
    print(hotel_ls)
    for k in range(len(hotel_ls)):
        for j in range(len(hotel_ls[k])):
            if room in hotel_ls[k][j]:
                floor = j
                # print(floor)

    print('room no' + str(room) + 'and floor' + str(floor))


bot()

# hotel_A = hotel(5,50)
# print(hotel_A)

# hotel_B = hotel(7,49)
# print(hotel_B)

# hotel_C = hotel(8,56)

# def room_no(a, b):
#     return lcm(a,b)

# room = room_no(5,7)

#     # hotA = [i for i in in range() ]
# # def person():
# def floor(hotel)

# for i in range(len(hotel_A)):
#     if room in hotel_A[i]:
#         floor = i
#         print(floor)
