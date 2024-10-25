class Bike:
    def __init__(self, size, speed, score):
        self.size = size
        self.speed = speed
        self.score = score
    
    def add_points(self, points):
        self.score += points