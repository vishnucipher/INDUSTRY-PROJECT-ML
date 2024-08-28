import sys

#from logger import logging
def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  ## exc_tb == traceback i will store on which line number the exception is occurs.... whic file 
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = "Error occeured in python script name [{0}] Line number [{1}], error message [{2}]".format(file_name,line_number,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__()   # Initialize the parent Excepting class
        self.error_message = error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):  # This method return the detailed error message when the exceptin is printed or converted to a string
        return self.error_message


'''
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info('Zero Division Error')
        raise CustomException(e,sys)'''