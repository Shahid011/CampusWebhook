from functools import wraps

def tryMultipleTimes(func,loginFunc):
    @wraps(func)
    def wrapped(*args, **kwargs):
        tries = 1
        while 1:
            try:
                return func(*args, **kwargs)

            except Exception as e:
                tries+=1
                if tries == 2 :
                    loginFunc()
                    
                if tries > 3:
                    raise Exception(e)
                pass
        return func(*args, **kwargs)
    return wrapped