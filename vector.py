from math import sqrt, atan2, degrees

class Vector:
    def __init__(self, x0, y0, x1, y1):
        # x0 and y0 are the coordinates of the vector's tail
        self.x0 = x0
        self.y0 = y0
        # x1 and y1 are the coordinates of the vector's tip
        self.x1 = x1
        self.y1 = y1

    # This method is called when the object is printed
    def calculate_properties(self):
        dx = self.x1 - self.x0 # Calculate the x component of the vector
        dy = self.y1 - self.y0 # Calculate the y component of the vector
        magnitude = sqrt(dx**2 + dy**2) # Calculate the magnitude of the vector
        angle = degrees(atan2(dy, dx)) # Calculate the angle of the vector
        return dx, dy, magnitude, angle