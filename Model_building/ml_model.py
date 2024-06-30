from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import metrics
from Data_Splitting.train_test_split import SeparateIndependentFeature


class AccessTrainTestData:

    """

    Class_Name : AccessTrainTestData
    Description: This class is used to access training and testing data and then using this data to train the Machine Learning Model
    Written by : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = SeparateIndependentFeature()

    def data_access(self):

        """

        Method_Name : data_access
        Description : This method is used to access the training and testing data
        Output      : Dataframe
        On_Failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            x_train, x_test, y_train, y_test = self.data.x_y_feat()
            return x_train, x_test, y_train, y_test
        except Exception as e:
            return e

    def rfc_model(self):

        """

        Method_Name : rfc_model
        Description : Using Random Forest Algorithm to build a model based on training data
        Output      : Model Accuracy
        On_Failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            x_train, x_test, y_train, y_test = self.data_access()
            rfc = RandomForestClassifier()
            rfc.fit(x_train, y_train)
            y_pred = rfc.predict(x_test)
            print(metrics.accuracy_score(y_test, y_pred))
            print(rfc.score(x_train, y_train))
            return rfc
        except Exception as e:
            return e

    def svc_model(self):

        """

        Method_Name : svc_model
        Description : Using SVC Algorithm to build a model based on training data
        Output      : Model Accuracy
        On_Failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            x_train, x_test, y_train, y_test = self.data_access()
            svc = SVC()
            svc.fit(x_train, y_train)
            y_pred = svc.predict(x_test)
            print(metrics.accuracy_score(y_test, y_pred))
            print(svc.score(x_train,y_train))
            return svc
        except Exception as e:
            return e





