# calcalc
Calorie Calculator for Bulkup.

## How to use.

### 0. Clone this repository.

```sh
git clone https://github.com/HiromuMasuda/calcalc.git
```

### 1. Register your own data to mydata.yml

```yaml
height: 172.5
weight: 72.0
age: 24
sex: "man"
activity_level: 4
calorie_control: 5
```

### 2. Run the script.

```sh
python calcalc.py
```

## About mydata.yml.

### height[Float]
Your height(cm).

### weight[Float]
Your weight(kg).

### age[int]
Your age.

### sex[string]
Your sex, `man` or `woman`.

### activity_level[int]
Your activity level.

- Sedentary (little or no exercise): `1`
- Lightly active (training/sports 2-3 days/week): `2`
- Moderately active (training/sports 4-5 days/week): `3`
- Very active (training/sports 6-7 days a week): `4`
- Extremely active (twice per day, extra heavy workouts): `5`

### calorie_control[int]

- Goal: Fat loss
  - Current body fat is over 30%: `1`
  - Current body fat is 20%-30%: `2`
  - Current body fat is 10%-20%: `3`
  - Current body fat is less than 10%: `4`
- Goal: Muscle gein: `5`

## Calorie calculation logic.

### Step 1. Calculate your BMR

BMR stands for Basal metabolic rate, in other words it is the **base** calories that you can burn in a day. The description is [here](https://en.wikipedia.org/wiki/Basal_metabolic_rate), and the fomula is below (Harris-Benedict).

Man: 66.47 + 13.75 * WEIGHT + 5.00 * HEIGHT - 6.78 * AGE
Woman: 65.1 + 9.56 * WEIGHT + 1.85 * HEIGHT - 4.68 * AGE

### Step 2. Adjust for Activity

You need to add an 'activity multiplier' (x1.2~x1.9) to your BMR depending on your lifestyle/training.

- Sedentary (little or no exercise): BMR x 1.2
- Lightly active (training/sports 2-3 days/week): BMR x 1.375
- Moderately active (training/sports 4-5 days/week): BMR x 1.55
- Very active (training/sports 6-7 days a week): BMR x 1.725
- Extremely active (twice per day, extra heavy workouts): BMR x 1.9

From these two calculations we now have our approximate daily energy expenditure (TDEE).

### Step 3. Adjust Calorie Intake Based On Your Goal

#### Goal: Fat Loss

|Current estimated body fat %|Reduce calorie intake by|
|--|--|
|30%>|30%|
|20-30%|25%|
|10-20%|20%|
|<10%|15%|

#### Goal:Muscle Gain

Increase TDEE by 20%.


### Step4. Calcurate PFC intake

So you’ve got your TDEE sorted. Now let’s figure out the macronutrient ratios that will make up your bodymaking.

Here are the calorie values for each macronutrient.

- 1g Protein = 4 Calories
- 1g Carbohydrate = 4 Calories
- 1g Fat = 9 Calories

#### Protein

First, let’s start with protein. Protein is essential for the growth of new tissue as well as fixing broken tissue – like what happens when you work out. Protein should be your new best friend if you want to gain or maintain muscle.

- Protein(g): WEIGHT * 2.5(g)
- Protein(cal): WEIGHT * 2.5(g) * 4(cal)

#### Fat

Consumption of dietary fat is important for hormonal regulation, especially testosterone production. It should never be eliminated from a diet.

- Fat(g): WEIGHT * 1.0(g)
- Fat(cal): WEIGHT * 1.0(g) * 9(cal)

#### Carbohydrate

Think of all your favorite foods and chances are they are high in Carbohydrates. Your body uses carbohydrates to make glucose which is the preferred fuel or energy that our bodies run off of. They’re what keeps us going.

- Carbohydrate(cal): TDEE - Protein(cal) - Far(cal)
- Carbohydrate(g): Carbohydrate(cal) / 4(cal/g)
