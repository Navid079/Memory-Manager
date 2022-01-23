class Frame:

  def __init__(self):
    self.page = None

  def set_page(self, page, time):
    self.page = page
    page.enter(time)

  def reference(self, time):
    self.page.reference(time)

  def get_last_reference(self):
    return self.page.referenced

  def get_next_reference(self):
    return self.page.next_reference

  def is_empty(self):
    return self.page is None