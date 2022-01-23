class Page:

  entered = -1
  referenced = -1

  def __init__(self, label, references):
    self.label = label
    self.references = references

  def enter(self, time):
    self.entered = time
    self.reference(time)

  def reference(self, time):
    self.referenced = time

  def is_referenced(self, time):
    return time in self.references

  def next_reference(self, time):
    refs = list(filter(lambda ref: ref > time, self.references))
    if refs: return refs[0]
    else: return -1
