from packages.models.Frame import Frame


class Memory:

  def __init__(self, size):
    self.time = 0
    self.frames = [Frame() for _ in range(size)]

  def get_page(self, page):
    for frame in self.frames:
      if frame.page is page:
        frame.reference(self.time)
        self.time += 1
        return True
    return False

  def insert_page(self, page, index):
    self.frames[index].set_page(page, self.time)
    self.time += 1