import pickle
from Hyperparameter_tuning.parameter_tuning import ParameterTuning


class SaveModel:

    """

    class Name  : SaveModel
    Description : This class is used to save the machine learning model in serialized format.
    Written by  : Adityaraj Hemant Chaudhari
    Version     : 0.1
    Revision    : None

    """

    def __init__(self):
        self.model = ParameterTuning()
        self.mode = 'wb'
        self.path = 'SVCModel.pkl'

    def save(self):

        """

        Method_Name : save
        Description : This method helps us saving the model in pickle file.
        Output      : Pickle File
        On Failure  : Raise Exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        try:
            model=self.model.model_tuning()
            path = self.path
            mode = self.mode
            pickle.dump(model, open(path, mode))
        except Exception as e:
            raise e





