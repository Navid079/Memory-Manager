class Frame:

  def __init__(self):
    self.page = None
    self.clock = 0

  def set_page(self, page, time):
    self.page = page
    self.clock = 1
    page.enter(time)

  def reference(self, time):
    self.clock = 1
    self.page.reference(time)

  def unset_clock(self):
    self.clock = 0

  def get_last_reference(self):
    return self.page.referenced

  def get_next_reference(self):
    return self.page.next_reference

  def is_empty(self):
    return self.page is None