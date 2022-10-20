class BMI:

    def __init__(self) -> None:
        self.__weight = 0.0
        self.__height = 0.0
        self.__bmi = 0.0

    def set_weight(self, weight: float):
        self.__weight = weight

    def set_height(self, height: float):
        self.__height = height  

    def calc_bmi(self):
        self.__bmi = self.__weight / (self.__height / 100 ) ** 2

    def get_bmi(self):
        return self.__bmi

# testing BMI class
def main():
    bmi = BMI()
    height = float(input("What is your height? "))
    weight = float(input("What is your weight? "))
    bmi.set_height(height)
    bmi.set_weight(weight)
    bmi.calc_bmi()
    print(bmi.get_bmi())

main()




