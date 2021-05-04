class paperNode:
  def __init__(self,title:str='',date:tuple='',link:str='',doi:int=None,authors:list=[],refrences:list=[]):
    '''
    date: tuple of threes integers--year, month and date.
    authors: list of strings.
    references: list of paperNode.
    '''
    self.title = tile
    self.date = date
    self.llink = link
    self.doi = doi
    self.authors = authors
    self.references = references
