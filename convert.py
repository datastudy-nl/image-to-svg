import cv2
import svgwrite
import numpy as np


# Load the new image
image = cv2.imread('input.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours based on edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an SVG file with a white background
svg_output_path = 'output.svg'
dwg = svgwrite.Drawing(svg_output_path, profile='tiny', size=(image.shape[1], image.shape[0]))
dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))

# Convert contours to SVG paths with colors
for contour in contours:
    points = [(point[0][0], point[0][1]) for point in contour]
    path_data = "M " + " L ".join([f"{x},{y}" for x, y in points]) + " Z"

    # Get the color of the contour from the original image
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [contour], -1, 255, -1)
    # Add the path to the SVG
    dwg.add(dwg.path(d=path_data, fill='black', stroke='black', stroke_width=1))

# Save the SVG file
dwg.save()

svg_output_path
