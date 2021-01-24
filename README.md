## Introduction:

Predict person's gender using English first name.


## Get Started

If you want to run the Django app, 

1. Clone the Repo to your destination: 

```
cd my/dir
git clone https://github.com/JasonZhangHub/django_gender_app.git
```

2. Build the Django app in Docker Container

After successfully building the Django app, you can then run

```
python manage.py runserver 0.0.0.0:8000
```

You can get the gender prediction by calling the API below on your browser, such as Jason

```
http://localhost:8000/gender_recognition/predict_gender?name=Jason
```

You should be able to get the result

```
{"Gender": "male"}

```
or
```
http://localhost:8000/gender_recognition/predict_gender?name=Hannah
```

You should be able to get the result

```
{"Gender": "female"}
```




If you want to get the prediction on local machine, you can try follow steps to predict the gender with a first name.

1. Clone the Repo to your destination: 

```
cd my/dir
git clone https://github.com/JasonZhangHub/django_gender_app.git
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

4. Run the prediction model

```
cd path/gender_recognition
import genderPredictor
print(genderPredictor.genderPredict('YourName')
```



## Dataset and Model
If you want to know more about the dataset and how the model is built. 

You can refer to the jupyter notebook in the data folder. 



## Contact:
For any kind of comments/suggestions regarding improving accuracy/performance of the model. 

Please mail me at jszhang0001@gmail.com.