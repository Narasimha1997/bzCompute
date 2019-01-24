import time


LOG_FILE = 'logs.txt' #Redirect this to your own logging path

class Exception :

    def __init__(self, cause = 'Unknown Cause', log = False):

        self.cause = cause
        self.time = time.time()

        #logging function
        if log : 
            open(LOG_FILE, 'w').write(time + ": "+ cause+ "\n")
        
        print("Error : " + self.cause)

    def __str__(self):

        return self.cause

