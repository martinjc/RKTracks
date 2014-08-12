class Point(object):

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def same_x(self, point, tolerance):
        bound_down = point.x - tolerance
        bound_up = point.x + tolerance
        return self.x > bound_down and self.x < bound_up

    def same_y(self, point, tolerance):
        bound_left = point.y - tolerance
        bound_right = point.y + tolerance
        return self.y > bound_left and self.y < bound_right

    def same_z(self, point, tolerance):
        bound_bottom = point.z - tolerance
        bound_top = point.z + tolerance
        return self.z > bound_bottom and self.z < bound_top

    def same_point(self, point, tolerance):
        return self.same_x(point, tolerance) and self.same_y(point, tolerance) and self.same_z(point, tolerance)


class Line(object):

    def __init__(self):
        self.points = []

    def intersects(self, line, tolerance):
        for p in self.points:
            for lp in line.points:
                if p.same_point(lp, tolerance):
                    return True
        return False
