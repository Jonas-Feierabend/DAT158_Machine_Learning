import gradio as gr
import joblib 
from sktime.forecasting.base import ForecastingHorizon
from sktime.utils import mlflow_sktime 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

model_path ="./my_model" 
loaded_model = mlflow_sktime.load_model(model_uri=model_path)


 
 
 
def show_plot(data):
    x = []
    y = []
    for index,row in data.iterrows():
        #index = date 
        # int(row) -> sales num 
        x.append(index)
        y.append(row.iloc[0]) 
    
    #neu
    ax = plt.subplot(111)
    ax.xaxis_date()
    ax.bar(x,y) 
    
    
    plt.xticks(rotation=45) 
    plt.xlabel("Date") 
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    # Speichere den Graphen als Bild
    plt.savefig("output_plot.png")

    # Zeige den erstellten Graphen
    plt.show()

    # Rückgabe des Dateipfads für das erstellte Bild
    return "output_plot.png"
    
def prediction(number_of_x,shop_id,shoptyp):
    start_date = "2017-08-16"
    periods = number_of_x
    shoptyp_default = "AUTOMOTIVE"

    freq = "D"
    fh = ForecastingHorizon(
        pd.PeriodIndex(pd.date_range(start_date, periods=periods, freq=freq)), is_relative=False
    )
    y_pred = loaded_model.predict(fh)
    
    labels = (str(int(shop_id)), shoptyp,slice(None))
    
    return show_plot(y_pred.loc[labels])


inputs = [
"text"]


# Erstelle die Gradio-Schnittstelle
iface = gr.Interface(
    fn=prediction,
    inputs=[
        gr.Number(label="days",minimum=1, maximum = 30, value=24),
        gr.Number(label="shop_id",minimum=1, maximum = 54, value=3),
        gr.Textbox(label="shoptyp", value="AUTOMOTIVE"),
    ],
    outputs="image",
    title="Sales Predictor",
    description="""Here Managers have the opportunity to predict the upcoming sales in different shops and for different products
    days: number of days you want to predict into the future, due to the training data ending on the 16-08-2017 you start from there
    shop_id: shop_nbr of the shop you want to look at 
    shoptyp: the family of the store, for example 'AUTOMOTIVE', 'EGGS' , 'HARDWARE'
    
    The prediction needs approximately 20s to process"""
)


if __name__ == "__main__":
        iface.launch()   