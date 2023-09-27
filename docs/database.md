
# Dataset

The dataset is publically available on the Kaggle website with the description: "The "Framingham" heart disease dataset includes over 4,240 records,16 columns and 15 attributes. The goal of the dataset is to predict whether the patient has 10-year risk of future (CHD) coronary heart disease"

## Attributes

### Demographic

- Sex: male or female(Nominal)
  - 1=Men
  - 2=Women
- Age: Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
  - 32-81 years old
- Education: Attained Education
  - 1=0-11 years
  - 2=High School Diploma, GED
  - 3=Some College, Vocational School
  - 4=College (BS, BA) degree or more

### Behavioral

- Current Smoker: whether or not the patient is a current smoker (Nominal)
  - 0=Not current smoker
  - 1=Current smoker
- Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)
  - 0=Not current smoker
  - 1-90 cigarettes per day

### Information on medical history

- BP Meds: whether or not the patient was on blood pressure medication (Nominal)
  - 0=Not current smoker
  - 1-90 cigarettes per day
- Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)
  - 0=Free of disease
  - 1=Prevalent disease
- Prevalent Hyp: whether or not the patient was hypertensive (Nominal)
  - 0=Free of disease
  - 1=Prevalent disease
- Diabetes: whether or not the patient had diabetes (Nominal)
  - 0=Not a diabetic
  - 1=Diabetic

### Information on current medical condition

- Tot Chol: total cholesterol level (Continuous)
- Sys BP: systolic blood pressure (Continuous)
- Dia BP: diastolic blood pressure (Continuous)
- BMI: Body Mass Index (Continuous)
- Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
- Glucose: glucose level (Continuous)

[EOF]
