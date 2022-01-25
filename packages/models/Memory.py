from packages.models.Frame import Frame


class Memory:

  def __init__(self, size):
    self.time = 0
    self.pointer = 0
    self.pointer_history = []
    self.frames = [Frame() for _ in range(size)]
    self.faults = []

  def __str__(self):
    if not self.pointer_history:
      string =  '\n'.join(map(lambda frame: str(frame), self.frames)) + '\n'
    else:
      string = ''
      for i, frame in enumerate(self.frames):
        for j, history in enumerate(frame.history):
          flag = frame.flag_history[j]
          string += '|'
          if self.pointer_history[j] == i:
            string += f'>{history}' + ('*' if flag else '.')
          else:
            string += f' {history}' + ('*' if flag else '.')
        string += '|\n'
    for f in self.faults:
        string += '  f ' if f else '    '
    return string

  def get_page(self, page):
    for frame in self.frames:
      if frame.page is page:
        frame.reference(self.time)
        self.time += 1
        self.faults.append(False)
        return False
    self.faults.append(True)
    return True

  def get_empty_frame(self):
    for i, frame in enumerate(self.frames):
      if frame.is_empty(): return i
    return -1

  def get_frame_on_pointer(self, check_flag = True):
    if not check_flag:
      p = self.pointer
    else:
      frame = self.frames[self.pointer]
      if frame.is_empty():
        p = self.pointer
      elif frame.clock_flag == 1:
        frame.unset_clock_flag()
        p = -1
      else:
        p = self.pointer
    self.pointer = self.pointer + 1 if self.pointer < len(
        self.frames) - 1 else 0
    return p

  def pointer_stop(self):
    self.pointer_history.append(self.pointer)

  def insert_page(self, page, index):
    self.frames[index].set_page(page, self.time)
    self.time += 1

  def save_history(self):
    for frame in self.frames:
      frame.save_history()