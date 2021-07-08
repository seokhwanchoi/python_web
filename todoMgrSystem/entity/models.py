class Todo:
    def __init__(self, id,title,contents, date, done):
        self.id=id
        self.title=title
        self.contents=contents
        self.date= date
        self.done=done
    
    def info(self):
        return self.id + " : "+ self.title + " : "+ self.contents + " : "+ self.date + " : " + self.done