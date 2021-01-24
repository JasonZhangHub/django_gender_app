## Introduction:

Predict person's gender using English first name.


## Get Started

If you want to run on local machine, you can try follow steps to predict the gender with a first name.

1. Clone the Repo to your destination: 

```
cd my/dir
git clone https://github.com/JasonZhangHub/genderPredictor.git
```

2. Setup your virtual environment and activate
```
conda create --name [yourenvname] python=3.8
conda activate [yourenvname] 
```
or 
```
python3 -m venv [yourenvname]
source [yourenvname]/bin/activate
```

3. Install requirements

```
conda install --file requirements.txt
```
or 
```
pip install -r requirements.txt
```

4. Run the model

```
cd gender_recognition/genderPredictor
import genderPredictor
print(genderPredictor.genderPredict('name')
```

Else, you can run the Django app in Docker

```
python manage.py runserver 0.0.0.0:8000
```

You can get the gender prediction by calling the API below on your browser.

```
http://localhost:8000/gender_recognition/predict_gender?name=Jason
```

## Contact:
For any kind of comments/suggestions regarding improving accuracy/performance of the model. 

Please mail me at jszhang0001@gmail.com.