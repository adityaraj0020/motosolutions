from fastapi import FastAPI,Form,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
import joblib,pandas as pd,numpy as np

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

model=joblib.load("r15_model.joblib")
df=pd.read_csv("r15_dataset.csv")

meta={r["diagnosis"]:r.to_dict() for _,r in df.iterrows()}

@app.post("/diagnose")
async def diagnose(model_name:str=Form(...),symptoms:str=Form(...),fault_code:str=Form(""),file:UploadFile=File(None)):
X=[symptoms+" "+fault_code]
p=model.predict_proba(X)[0]
c=model.classes_
top=np.argsort(p)[::-1][:3]
return{"predictions":[{"diagnosis":c[i],"confidence":float(p[i])} for i in top]}