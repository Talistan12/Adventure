DEBUGGING = False

def debug( s ):
   if DEBUGGING:
     print "** " + s;
   return;

class userException(RuntimeError):
   def __init__(self, arg):
      self.args = arg

