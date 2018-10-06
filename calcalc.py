import yaml

class CalCalc:

    def __init__(self):
        f = open("mydata.yml", "r+")
        mydata = yaml.load(f)

        self.height = mydata["height"]
        self.weight = mydata["weight"]
        self.age = mydata["age"]
        self.sex = mydata["sex"]
        self.activity_level = mydata["activity_level"]
        self.calorie_control = mydata["calorie_control"]

    def calc_calories(self):
        bmr = self.calc_bmr()
        calorie_intake = self.calc_calorie_intake(bmr)
        self.print_calorie_pfc(calorie_intake)

    def calc_bmr(self):
        if self.sex == "man":
            bmr = 66.47 + 13.75*self.weight + 5.00*self.height - 6.78*self.age
        elif self.sex == "woman":
            bmr = 65.1 + 9.56*self.weight + 1.85*self.height - 4.68*self.age
        else:
            raise Exception('Sex must be man or woman.')
        return bmr

    def calc_calorie_intake(self, bmr):
        activity_multiplier = self.get_activity_multiplier(self.activity_level)
        intake_multiplier = self.get_calorie_intake_multiplier(self.calorie_control)
        daily_calorie_consumption = bmr * activity_multiplier
        daily_calorie_intake = daily_calorie_consumption * intake_multiplier
        return daily_calorie_intake

    def print_calorie_pfc(self, daily_calorie_intake):
        protein_gram = self.weight * 2.5
        protein_kcal = protein_gram * 4.0
        fat_gram = self.weight * 1.0
        fat_kcal = fat_gram * 9.0
        carbon_kcal = daily_calorie_intake - protein_kcal - fat_kcal
        carbon_gram = carbon_kcal / 4.0
        print("daily calorie intake: %dkcal" % daily_calorie_intake)
        print("protain: %dg/%dkcal" % (protein_gram, protein_kcal))
        print("fat: %dg/%dkcal" % (fat_gram, fat_kcal))
        print("carbon: %dg/%dkcal" % (carbon_gram, carbon_kcal))

    def get_activity_multiplier(self, activity_level):
        return {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}[activity_level]

    def get_calorie_intake_multiplier(self, calorie_control):
        return {1: 0.70, 2: 0.75, 3: 0.80, 4: 0.85, 5: 1.20}[calorie_control]

if __name__ == '__main__':
    c = CalCalc()
    c.calc_calories()
