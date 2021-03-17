class DecoratorHelper:
    
    @staticmethod
    def on_before_func(*args):
        #print("before: ", args)
        if(type(args[1]) is not str):
            print("Custom Error")

    @staticmethod
    def on_after_func(result,*args):
        #print("after: ", result, args)
        if(result == True):
            print("Log: ",str(result))
        else:
            raise Exception("After Error")

    @staticmethod
    def on_exception_func(*args):
        #print("error: ", args)
        print("Throw Custom Error")
        return "Custom Result"

