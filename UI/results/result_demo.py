from Core.utilities.results.success_result import SuccessResult
from Core.utilities.results.error_result import ErrorResult
from Core.utilities.results.success_data_result import SuccessDataResult
from Core.utilities.results.error_data_result import ErrorDataResult

class ResultDemo:

    def fonk1(self,value1):
        return SuccessResult("OK").toMap()

    def fonk2(self,value1):
        return ErrorResult("NOT OK").toMap()

    def fonk3(self,value1):
        result = value1
        return SuccessDataResult("OK",result).toMap()

    def fonk4(self,value1):
        result = value1
        return ErrorDataResult("NOT OK",result).toMap()
    