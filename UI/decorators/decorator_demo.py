from Core.utilities.decorators.decorator import Decorator
from UI.decorators.decorator_helper import DecoratorHelper

class DecoratorDemo:

    @Decorator.on_before(DecoratorHelper.on_before_func)
    def on_before_demo(self,value1, value2):
        print("Row 1")
        print("Row 2")
        return "Result"
    

    @Decorator.on_after(DecoratorHelper.on_after_func)
    def on_after_demo(self,value1, value2):
        print("Row 1")
        print("Row 2")
        return True

    @Decorator.on_exception(DecoratorHelper.on_exception_func)
    def on_exception_demo(self,value1, value2):
        print("Row 1")
        raise Exception("Error")
        print("Row 2")
        return "Result"

    @Decorator.on_exception(DecoratorHelper.on_exception_func)
    @Decorator.on_after(DecoratorHelper.on_after_func)
    def double_demo(self,value1,value2):
        print("Row 1")
        print("Row 2")
        result = False
        return result


