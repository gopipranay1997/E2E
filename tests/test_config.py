from app import form_response

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)

input_data = {
    "incorrect_values":
    {"CreditScore": 3,
    "Age": 4,
    "Tenure": 'as',
    "Balance": 12,
    "NumOfProducts": 1,
    "HasCrCard": 'ab',
    "IsActiveMember":'a' ,
    "EstimatedSalary":10000,
    "Geography_Germany":1,
    "Geography_Spain": 0,
    "Gender_Male":1
    },

    "correct_values":
    {"CreditScore": 3,
    "Age": 4,
    "Tenure": 12,
    "Balance": 12,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember":1 ,
    "EstimatedSalary":10000,
    "Geography_Germany":1,
    "Geography_Spain": 0,
    "Gender_Male":1
    },
}

def test_form_response_incorrect_values(data=input_data["incorrect_values"]):
    res=form_response(data)
    assert res == NotANumber().message