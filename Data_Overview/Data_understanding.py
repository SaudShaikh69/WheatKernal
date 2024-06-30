import pandas as pd
import numpy as np
from Data_Acquisition.Data_loader import GetData


class DataInfo:

    """

    Class Name : DataInfo
    Description: This class is used to figure out size and shape and overall info of data we loaded previously
    Written by : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = GetData()

    def get_shape(self):

        """

        Method_Name : get_shape()
        Description : This method is used to get the shape of the dataset loaded previously
        output      : 2-D array
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.data.acquire_data()
            shape = data.shape
            return shape
        except Exception as e:
            raise e

    def get_info(self):

        """

        Method_Name : get_info()
        Description : This method is used to find the info i.e data type of columns,check null values , values present in column,etc.
        output      : Pandas DataFrame
        on failure  : raise Exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try :
            data = self.data.acquire_data()
            info = data.info()
            return info
        except Exception as e:
            raise e

    def get_size(self):

        """

        Method Name : get_size()
        Description : This method is used to find overall size of the dataset loaded.
        output      : Integer Value
        on Failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        try:
            data = self.data.acquire_data()
            size = data.size
            return size
        except Exception as e:
            raise e


