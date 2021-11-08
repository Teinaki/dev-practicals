class BlogPost:
    """Adds a post to the blog and provides a save() method for it."""
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self._db = Database()
        
    def save(self):
        try:
            self._db.save(self)
        except DBAPIError as e:
            with open(ERRLOG, 'a') as log:
                log.write('Error saving blog post:')
                log.write(e)

# This violates the single responsibility principle. It has at least two
# reasons to change. We might change something about the data attributes 
# we store, or we might change the way we log errors. We need to 
# extract the error logging responsibilty into another class

class BlogPost:
    """Adds a post to the blog and provides a save() method for it."""
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self._db = Database()
        
    def save(self):
        try:
            self._db.save(self)
        except DBAPIError as e:
            log = ErrorLog('Error saving blog post:')
            log.write()

class ErrorLog:
    def __init__(self, message):
        pass