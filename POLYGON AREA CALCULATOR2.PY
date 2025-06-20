def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2

# Example usage
polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
print("Area of the polygon:", polygon_area(polygon))
