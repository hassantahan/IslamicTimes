import math
import numpy as np

def bound_angle_deg(a):
    return a - 360.0 * (math.floor(a / 360.0))

def bound_angle_rad(a):
    return a - (2 * math.pi) * (math.floor(a / (2 * math.pi)))

def sin(a):
    return math.sin(np.deg2rad(a))

def cos(a):
    return math.cos(np.deg2rad(a))

def tan(a):
    return math.tan(np.deg2rad(a))

def decimal_to_dms(decimal_deg):
    degrees = int(decimal_deg)
    minutes = int((decimal_deg - degrees) * 60)
    seconds = (decimal_deg - degrees - minutes / 60) * 3600

    return [degrees, minutes, seconds]

def decimal_to_hms(decimal_degrees):
    hours = int(decimal_degrees / 15)
    minutes = int((decimal_degrees / 15 - hours) * 60)
    seconds = (decimal_degrees / 15 - hours - minutes / 60) * 3600
    return [hours , round(minutes), seconds]

def calculate_angle_diff(azimuth1, altitude1, azimuth2, altitude2):
    # Convert degrees to radians
    azimuth1, altitude1, azimuth2, altitude2 = map(math.radians, [azimuth1, altitude1, azimuth2, altitude2])

    # Apply the haversine formula
    delta_azimuth = azimuth2 - azimuth1
    delta_altitude = altitude2 - altitude1

    a = math.sin(delta_altitude / 2)**2 + math.cos(altitude1) * math.cos(altitude2) * math.sin(delta_azimuth / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Convert the angle difference from radians to degrees
    angle_diff = math.degrees(c)
    
    return angle_diff

# Modified calculate_angle_diff for finding course angle
def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Earth radius in km

    # Calculate course angle
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    course_angle = math.degrees(math.atan2(y, x))

    return distance, course_angle

def get_cardinal_direction(degree):
    cardinals = [
        'N', 'NNE', 'NE', 'ENE',
        'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW',
        'W', 'WNW', 'NW', 'NNW'
    ]
    idx = int(((degree + 11.25) % 360) / 22.5)
    return cardinals[idx]