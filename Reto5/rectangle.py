from shape.shape import Shape, Point

class Rectangle(Shape): # Done
  def __init__(self, vertices:list[Point], is_regular):
    super().__init__(vertices, is_regular)
    Shape.compute_edges(self)

  def compute_area(self):
    area = self.edges[0].length * self.edges[1].length
    return area

  def compute_perimeter(self):
    perimeter = (self.edges[0].length*2) + (self.edges[1].length*2)
    return perimeter

  def compute_inner_angle(self):
    inner_angle = 0
    return inner_angle

class Square(Rectangle): # Done
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=True)

  def compute_area(self):
    area = self.edges[0].length ** 2
    return area

  def compute_perimeter(self):
    perimeter = self.edges[0].length * 4
    return perimeter
