from sklearn.model_selection import train_test_split
from Data_Acquisition.Data_loader import GetData


class SeparateIndependentFeature:

    """

    class Name  : SeperateIndependentFeature
    Description : This class is used to split the dataset in training and testing set.
    Written by  : Adityaraj Hemant Chaudhari
    Version     : 0.1
    Revision    : None

    """

    def __init__(self):
        self.data = GetData()

    def x_y_feat(self):

        """

        Method_Name : x_y_feat
        Description : Splitting the dataset into dependent and independent features.
        Output      : DataFrame
        On Failure  : Raise Exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        try:
            data = self.data.acquire_data()
            x = data.drop("Type_Of_Kernel", axis=1)
            y = data["Type_Of_Kernel"]
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
            return x_train, x_test, y_train, y_test

        except Exception as e:
            raise e


s = SeparateIndependentFeature()
s.x_y_feat()