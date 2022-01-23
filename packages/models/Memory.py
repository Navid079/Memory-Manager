from packages.models.Frame import Frame


class Memory:

  def __init__(self, size):
    self.time = 0
    self.pointer = 0
    self.frames = [Frame() for _ in range(size)]

  def get_page(self, page):
    for frame in self.frames:
      if frame.page is page:
        frame.reference(self.time)
        self.time += 1
        return False
    return True

  def get_empty_frame(self):
    for i, frame in enumerate(self.frames):
      if frame.is_empty(): return i
    return -1

  def get_frame_on_pointer(self):
    frame = self.frames[self.pointer]
    if frame.is_empty():
      return self.pointer
    elif frame.clock_flag == 1:
      frame.unset_clock_flag()
      self.pointer = self.pointer + 1 if self.pointer < len(self.frames -
                                                            1) else 0
      return -1
    return self.pointer

  def insert_page(self, page, index):
    self.frames[index].set_page(page, self.time)
    self.time += 1