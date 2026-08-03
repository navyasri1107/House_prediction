import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
#Load dataset
df = pd.read_csv("house_predict.csv")
x=df[['Area','Bedrooms','Age']]
y=df['Price']

model=LinearRegression()
model.fit(x,y)

#save model using pickle
with open('house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)

    print("Model saved successfully.")