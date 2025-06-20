from flask import Flask,Response
import pandas as pd
import matplotlib.pyplot as plt
import io

app=Flask(__name__)

@app.route("/Dashboard")
    
def make_bargraph():
    df=pd.read_csv("hospital data analysis - Copy.csv")

    genders=df["Gender"].value_counts().index.tolist()
    num=df["Gender"].value_counts().values.tolist()
    gender_graph,ax=plt.subplots(figsize=(3,3))

    barplot=ax.bar(genders,num,color=["pink","lightblue"],ec="black")
    ax.bar_label(barplot,labels=num,label_type="center")
    ax.set_title("Number of Male/Female Patients")

    buf = io.BytesIO()
    gender_graph.savefig(buf, format='png')
    buf.seek(0)
    plt.close(gender_graph)
    
    return Response(buf.getvalue(), mimetype='image/png')
    
if __name__ == "__main__":

    app.run()

