import matplotlib.pyplot as plt
import random

class Rectangle:
    def __init__(self, width, height, rotation=False):
        self.width = width
        self.height = height
        self.rotation = rotation
    
    def rotate(self):
        self.width, self.height = self.height, self.width
        self.rotation = not self.rotation

def can_place_rectangle(region, rect):
    region_width, region_height = region
    if rect.width + 1 <= region_width and rect.height + 1 <= region_height:
        return True
    return False

def place_rectangles(region, rectangles):
    if not rectangles:
        return []
    
    rect = rectangles[0]
    
    if can_place_rectangle(region, rect):
        return [(0, 0, rect.width, rect.height, rect.rotation)] + place_rectangles((region[0] - rect.width - 1, region[1]), rectangles[1:])
    
    rect.rotate()
    if can_place_rectangle(region, rect):
        return [(0, 0, rect.width, rect.height, rect.rotation)] + place_rectangles((region[0] - rect.width - 1, region[1]), rectangles[1:])
    
    raise ValueError("Placement is not possible")

def generate_random_rectangles(n=5):
    return [Rectangle(random.randint(5, 20), random.randint(5, 20)) for _ in range(n)]

def plot_rectangles(rectangles):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')

    x_offset = 0
    for i, (x, y, width, height, rotation) in enumerate(rectangles):
        rect = plt.Rectangle((x_offset + x, y), width, height, edgecolor='black', facecolor='none', lw=2)
        ax.add_patch(rect)
        x_offset += width + 1

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    region = (100, 100)
    rectangles = generate_random_rectangles()
    
    try:
        placed_rectangles = place_rectangles(region, rectangles)
        plot_rectangles(placed_rectangles)
    except ValueError as e:
        print(e)
