import pickle
import numpy as np
import config

class HeartDisease():
    def __init__(self,age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall):
        print('************ INIT Function *****************')
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trtbps = trtbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalachh = thalachh
        self.exng = exng
        self.oldpeak = oldpeak
        self.slp = slp
        self.caa = caa
        self.thall = thall

    def __load_save_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

    def get_heart_disease_pred(self):
           self.__load_save_data()

           test_array = np.array([self.age, self.sex, self.cp, self.trtbps, self.chol, self.fbs, self.restecg, 
                self.thalachh, self.exng, self.oldpeak, self.slp, self.caa, self.thall], ndmin = 2)
        #    print(test_array)
        #    for i in test_array[0]:
        #         print(type(i))
           
           heart_disease_prediction = np.around(self.model.predict_proba(test_array)[0,1],4)
          #    return heart_disease_prediction    >> by using this we check probability

           if heart_disease_prediction >= 0.1312:
                return "The Patient has Heart Disease."
           else:
                return "The Patient does not have a Heart Disease."