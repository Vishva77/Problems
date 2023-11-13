def isRectangleOverlap(rectangle1, rectangle2):
    # Check if either rectangle is to the left of the other
    if rectangle1[2] <= rectangle2[0] or rectangle2[2] <= rectangle1[0]:
        return False

    # Check if either rectangle is above the other
    if rectangle1[3] <= rectangle2[1] or rectangle2[3] <= rectangle1[1]:
        return False

    # If none of the above conditions are met, the rectangles overlap
    return True

print(isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))  # Output: True
