def switch_planes(planes, planeNumber, initialNumber):
    # Plane number is plane to which we wish to switch
    if not planes[planeNumber].collision_detect():
        return planeNumber
    else:
        return initialNumber
