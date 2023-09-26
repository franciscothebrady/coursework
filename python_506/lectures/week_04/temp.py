ev_vehicles = [
    "Cadillac Lyric, SUV, RWD, 89, 312, 119, , $61,795",
    "Chevrolet Bolt EUV, Sedan/Wagon, FWD, 115, 247, 75, 5, $27,200",
    "Chevrolet Bolt EV, Sedan/Wagon, FWD, 120, 259, 75, 5, $25,600",
    "Ford F150 Lightning 4WD, Pickup, AWD, 66-70, 240-320, 165, 5, $55,974",
]

vehicle_count = 0
for vehicle in ev_vehicles[1:]:
    if int(vehicle[4]) >= 250:
        vehicle_count =+ 1