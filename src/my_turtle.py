import svg_turtle as st
class Turtle:
  def __init__(self, outfilename, movement_dict, angle, stride, size) -> None:
    self.outfilename = outfilename
    self.movement_dict = movement_dict
    self.movement_dict['O'] = 'O'
    self.movement_dict['('] = '('
    self.movement_dict[')'] = ')'
    self.angle = angle
    self.stride = stride
    self.hsize = size
    self.vsize = size
    self.turtle = st.SvgTurtle(self.hsize, self.vsize)

  def draw(self, path : str):
    self.turtle = st.SvgTurtle(self.hsize, self.vsize) # overwrite it -- to be able to call draw multiple times
    self.turtle.width(10)
    for char in path:
      movement = self.movement_dict[char]
      self._draw(movement)

  def _draw(self, movement):
    if movement == 'O':
      self.turtle.penup()
      self.turtle.forward(self.stride)
      self.turtle.pendown()
    elif movement == 'F':
      self.turtle.forward(self.stride)
    elif movement == 'L':
      self.turtle.left(self.angle)
    elif movement == 'R':
      self.turtle.right(self.angle)
    elif movement == '(':
      self.turtle.circle(self.stride, -self.angle)
    elif movement == ')':
      self.turtle.circle(self.stride, self.angle)

  def write_output(self):
    self.turtle.save_as(self.outfilename)

  def to_svg(self):
    return self.turtle.to_svg()