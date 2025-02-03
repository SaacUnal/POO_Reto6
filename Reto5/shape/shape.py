class Point:
  def __init__(self, x:float, y:float):
    self.x = x
    self.y = y

  def compute_distance(self, point):
    distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    return distance

class Line:
  def __init__(self, start_point:Point, end_point:Point, length:float):
    self.start_point = start_point
    self.end_point = end_point
    self.length = length

##############################################################################

class Shape:
  def __init__(self, vertices:list[Point], is_regular:bool, ):
    # If the input's have the wrong types or values
    if vertices is not list:
      raise TypeError("The type is wrong. It has to be a list of points. ")
    for v in vertices:
      if v is not Point():
        raise ValueError("The values are wrong. They have to be points. ")
    self.vertices = vertices

    if is_regular is not bool:
      raise TypeError("The type is wrong. It has to be a boolean. ")
    self.is_regular = is_regular
  
  def compute_edges(self):
    edges = []
    for i in range(len(self.vertices)):
      x = self.vertices[i] 
      y = self.vertices[(i+1) % len(self.vertices)]
      edges.append(Line(x, y, Point.compute_distance(x, y)))
    self.edges = edges
  
  # For the sake of the polymorphism
  def compute_area(self):
    raise NotImplementedError("Subclases have to implement compute_area() ")

  def compute_perimeter(self):
    raise NotImplementedError("Subclases have to implement compute_perimeter() ")

  def compute_inner_angles(self):
    raise NotImplementedError("Subclases have to implement compute_inner_angles() ")
