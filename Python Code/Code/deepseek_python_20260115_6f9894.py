import numpy as np

L = 8
num_bounces = 576
origin = np.array([0, 0])

# Use EXACT π/9
H = np.pi / 9  # ≈ 0.3490658503988659
input_direction = np.array([3, H])  # Exact π/9
direction = input_direction / np.linalg.norm(input_direction)

# Rest of the code as before...
enable_mobius = False
position = origin.copy()
velocity = direction.copy()

vertical_bounce_y = []

for bounce in range(num_bounces):
    next_position = position + velocity
    
    for i in range(2):
        if next_position[i] < 0 or next_position[i] > L:
            if i == 0:  # Vertical wall
                if velocity[i] != 0:
                    if next_position[i] < 0:
                        t = (0 - position[i]) / velocity[i]
                    else:
                        t = (L - position[i]) / velocity[i]
                    bounce_y = position[1] + t * velocity[1]
                    vertical_bounce_y.append(bounce_y % 1)
            
            velocity[i] = -velocity[i]
            if enable_mobius:
                velocity[(i + 1) % 2] *= -1
            next_position = position + velocity
    
    position = next_position

# Analyze with exact H
favor_above = 0
favor_below = 0

for y in vertical_bounce_y:
    m = round(y / H)
    target = (m * H) % 1
    if y > target:
        favor_above += 1
    else:
        favor_below += 1

print(f"Using EXACT π/9 = {H}")
print(f"Vertical bounces: {len(vertical_bounce_y)}")
print(f"Favor above: {favor_above} ({favor_above/len(vertical_bounce_y):.3f})")
print(f"Favor below: {favor_below} ({favor_below/len(vertical_bounce_y):.3f})")
print(f"Ratio above/below: {favor_above/favor_below:.3f}")
print(f"Expected ratio: {0.65/0.35:.3f}")