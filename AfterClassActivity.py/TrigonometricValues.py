import math
import random

angle_degrees = random.uniform(0, 360)

angle_radians = math.radians(angle_degrees)

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

print(f"Angle: {angle_degrees:.2f} degrees")
print(f"Sine: {sin_value:.4f}")
print(f"Cosine: {cos_value:.4f}")
print(f"Tangent: {tan_value:.4f}")