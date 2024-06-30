import pandas as pd


class GetData:

    """

    Class Name : GetData
    Description: This class is used to acquire/access data that is stored in the text file.
    Output     : Pandas DataFrame
    On Failure : Raise Exception

    Written by : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : 0

    """

    def __init__(self):
        self.data_src = r"C:\Users\LEGION\ML Projects\Wheat Kernel Classifier\Data\seeds_dataset.txt"
        self.delimiter = "\t"
        self.col_names = ['Area', 'Perimeter', 'Compactness', 'Length_of_kernel', 'Width_of_kernel', 'Asymmetry_Coeff', 'Len_Kernel_Groove', 'Type_Of_Kernel']

    def acquire_data(self):

        """

        Method_Name : acquire_data
        Description : This method is used to acquire the data from the data source
        Output      : Pandas DataFrame
        On_Failure  : Raise Exceptions

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : 0

        """

        try:
            data = pd.read_csv(self.data_src, delimiter=self.delimiter, names=self.col_names)
            return data
        except Exception as e:
            return e





