# Generic entity that obeys physics. All specific entities (players, enemies)
# inherit from this. Entities are sprites. 
import pyglet 

class Entity(pyglet.sprite.Sprite):
    def __init__(self, min_x, max_x, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0.0 
        self.vy = 0.0 
        self.keys = { "left": False, "right": False, "up": False, "facing": "right" }
        self.speed = 5
        self.min_x = min_x 
        self.max_x = max_x 

    def check_bounds(self):
        if self.x + self.width // 2 > self.max_x:
            self.x = self.max_x - self.width // 2
        elif self.x - self.width // 2 < self.min_x:
            self.x = self.min_x + self.width // 2
        
    def update(self, dt):
        if self.keys['left']:
            self.vx = -self.speed 
        elif self.keys['right']:
            self.vx = self.speed
        else:
            self.vx = 0
        self.x += self.vx * dt 
        self.y += self.vy * dt
        self.check_bounds()