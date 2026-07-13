class MLModel:
    model_count = 0
    
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy
        MLModel.model_count += 1
        
    def report(self):
        return f"{self.name}:{self.accuracy:.0%}"
        
    @classmethod
    def count(cls):
        return f"Model traied: {cls.model_count}"
    @staticmethod
    def is_accepatble(acc):
        return acc >= 0.80
m1 = MLModel("RandomForest", 0.88)
m2 = MLModel("SVM", 0.76)
print(m1.report())
print(MLModel.count())
print(MLModel.is_accepatble(0.99))