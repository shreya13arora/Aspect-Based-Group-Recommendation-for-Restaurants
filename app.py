from flask import Flask, request, jsonify, render_template

import pandas as pd
import numpy as np

restaurant_df = pd.read_csv(r'./Datasets/restaurant_ratings_16052021_0.18.csv')
user_df = pd.read_csv(r'./Datasets/user_weights_16052021_0.18.csv')
restaurant_name = pd.read_csv(r'./Datasets/restaurant_name.csv')
restaurant_address = pd.read_csv(r'./Datasets/restaurant_address.csv')

def groupingStrategy(restaurant_user_df,group_members):
    restaurant_user_df['Total_Score'] = 1
    for i in group_members:
        restaurant_user_df['Total_Score'] = restaurant_user_df['Total_Score'].mul(restaurant_user_df[i])
    return restaurant_user_df
    
def getRecommendation(user_friends_list, restaurant_df, user_df, restaurant_name, restaurant_address, top_n, user_id): #Business_df with file name
    
    # Replace nan by 1 and 20 to give some importance and help multiplication
    restaurant_df = restaurant_df.replace(np.nan, 1)
    user_df = user_df.replace(np.nan,20)
    
    # Replace 0 by 1 and 20 to give some importance and help multiplication
    restaurant_df = restaurant_df.replace(0, 1)
    user_df = user_df.replace(0,20)

    restaurant_df_matrix = restaurant_df.set_index('restaurant').values
    ## Add the user in the list who is looking for recommendation
    user_friends_list.append(user_id)
    ## From our user_df get the User behaviour of all the group members
    selected_user = user_df[user_df['user'].isin(user_friends_list)]
    ## Essentially performing Multiplication of Weights and Rating is MatriX Multiplication of the Data frames
    user_df_T_matrix = selected_user.set_index('user').transpose().values
    restaurant_user_matrix = restaurant_df_matrix.dot(user_df_T_matrix) 
    ## Create a Dataframe from 2D Matrix by naming the columns and indices
    new_df = pd.DataFrame(restaurant_user_matrix,columns= selected_user['user'],index= restaurant_df['restaurant'])
    ## Send this dataframe for getting Grouping Strategy process
    final_df = groupingStrategy(new_df,selected_user['user'].values)
    final_df = final_df.sort_values(by='Total_Score',ascending= False)
    ## Return a list of Top N Restaurants 
    top_id = final_df.index[:top_n]
    names = (restaurant_name.name.loc[restaurant_name['restaurant'].isin(top_id)]).values
    address = (restaurant_address.full_address.loc[restaurant_address['restaurant'].isin(top_id)]).values
    return names, address

user_friends_list = ['u0x3SXagjYDbI2N4sgJ0Tw','80MUDP_Ny_J8jeShVxzdlw','p8yQsVA51dzkc9cecDpvrw',"byro3oSQQ1gRESKlfiAqtQ"]
print(getRecommendation(user_friends_list,restaurant_df,user_df,restaurant_name,restaurant_address,5,'k0d3Jnxulohu1HdJj1Hfkg'))



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def predict():
    temp_list = []
    for x in request.form.values():
        temp_list.append(x)
    
    name, address = getRecommendation(temp_list,restaurant_df,user_df,restaurant_name,restaurant_address,5,'k0d3Jnxulohu1HdJj1Hfkg')
    return render_template('recommedation.html', prediction_text= (name, address))


if __name__ == "__main__":
    app.run(debug=True)