def polysum(n,s):
    # Write a function called polysum that takes 2 arguments, n and s.
    # This function should sum the area and square of the perimeter of the regular polygon.
    # The function returns the sum, rounded to 4 decimal places.

    import math
    area = (0.25 * n * s**2) / math.tan(math.pi/n) #area of the polygon
    perim = n * s # perimeter of the polygon

    return round(area + perim**2,4) #returning the area summed with perimeter squared rounded to 4 decimal places.
