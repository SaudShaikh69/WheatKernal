from sklearn.model_selection import RandomizedSearchCV
from Model_building.ml_model import AccessTrainTestData
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


class ParameterTuning:

    """

    Class_Name : ParameterTuning
    Description: This Class is used to perform hyperparamter tuning on the Random Forest model.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.a = AccessTrainTestData()

    def model_access(self):

        """

        Method Name : model_access
        Description : This method is used to access the training and testing data as well as machine learning model built.
        output      : DataFrame
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        try:
            model = self.a.svc_model()
            return model
        except Exception as e:
            raise e

    def set_params(self):

        """

        Method Name : setting_parameters
        Description : This method is used to choose the best parameters and assigning it with set of values which can help our model to give better results.
        output      : None
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        try:
            param_grid = {
                'kernel': ['linear', 'rbf', 'sigmoid', 'poly'],
                'degree': [i for i in range(1, 10, 1)],
                'gamma': ['scale', 'auto'],
                'decision_function_shape': ['ovr', 'ovo'],
                'C': [i for i in range(1, 50, 1)]
            }
            return param_grid
        except Exception as e:
            raise e

    def model_tuning(self):

        """

        Method Name : model_tuning
        Description : This method is used to perform hyperparameter tuning using the set of values .
        output      : Acc.Scores
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        x_train, x_test, y_train, y_test = self.a.data_access()
        model = self.model_access()
        params = self.set_params()
        try:
            svc_randomcv = RandomizedSearchCV(estimator=model, param_distributions=params, n_iter=100,cv=3, n_jobs=-1, random_state=100, verbose=True)
            svc_randomcv.fit(x_train, y_train)
            svc_best = svc_randomcv.best_params_
            print(svc_best)
            svc_clf = SVC(kernel=svc_best['kernel'], degree=svc_best['degree'], gamma=svc_best['gamma'], C=svc_best['C'], decision_function_shape=svc_best['decision_function_shape'])
            svc_clf.fit(x_train, y_train)
            y_pre = svc_clf.predict(x_test)
            print(metrics.accuracy_score(y_test, y_pre))
            print(svc_clf.score(x_train, y_train))
            return svc_clf
        except Exception as e:
            raise e

























