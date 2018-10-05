import yaml

f = open("mydata.yml", "r+")
mydata = yaml.load(f)

HEIGHT = mydata["height"]
WEIGHT = mydata["weight"]
AGE = mydata["age"]
WORKOUT_LEVEL = mydata["workout_level"]
CONTROL_CALORIE = mydata["control_calorie"]

# Harris-Benedict(JP ver.)
bmr = 66.0 + 13.7*WEIGHT + 5.0*HEIGHT - 6.8*AGE

# daily_calorie
daily_calorie_consumption = bmr * WORKOUT_LEVEL
daily_calorie_intake = daily_calorie_consumption + CONTROL_CALORIE

# PFC
protein_gram = WEIGHT * 2.5
protein_kcal = protein_gram * 4.0
fat_gram = WEIGHT * 1.0
fat_kcal = fat_gram * 9.0
carbon_kcal = daily_calorie_intake - protein_kcal - fat_kcal
carbon_gram = carbon_kcal / 4.0

# OUTPUT
print("daily calorie intake: %dkcal" % daily_calorie_intake)
print("protain: %dg/%dkcal" % (protein_gram, protein_kcal))
print("fat: %dg/%dkcal" % (fat_gram, fat_kcal))
print("carbon: %dg/%dkcal" % (carbon_gram, carbon_kcal))
