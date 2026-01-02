import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("r15_dataset.csv")
X=df["symptoms"]
y=df["diagnosis"]

model=Pipeline([
("tfidf",TfidfVectorizer(ngram_range=(1,2))),
("clf",RandomForestClassifier(n_estimators=200))
])

model.fit(X,y)
joblib.dump(model,"r15_model.joblib")
print("Model trained")