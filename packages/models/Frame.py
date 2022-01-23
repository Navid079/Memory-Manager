class Frame:

  def __init__(self):
    self.page = None
    self.clock_flag = 0
    self.history = []

  def __str__(self):
    return '| ' + ' | '.join(self.history) + ' |'

  def set_page(self, page, time):
    self.page = page
    self.clock_flag = 1
    page.enter(time)
    while len(self.history) < time + 1:
      self.history.append(self.page.label if self.page else 'E')

  def reference(self, time):
    self.clock_flag = 1
    self.page.reference(time)

  def unset_clock_flag(self):
    self.clock_flag = 0

  def get_last_reference(self):
    return self.page.referenced

  def get_next_reference(self):
    return self.page.next_reference

  def is_empty(self):
    return self.page is None

  def finalize(self, time):
     while len(self.history) < time + 1:
      self.history.append(self.page.label if self.page else 'E')