# Linear Regression Model to Predict Life Expectancy
# Generate, Evaluate, and Test Model 

# import dependencies
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump, load

# read in data file
data = pd.read_csv('data/derived/final_data.csv')

# identify independent and dependent variables 
X = data[['state', 'year', 'quartile', 'gender']]
y = data['LE'].values.reshape(-1, 1)

# convert categorical variables to binary
X = pd.get_dummies(X, columns=['state', 'gender'])

# separate training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# scale data
X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)

X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)

#generate model
model = LinearRegression()
model.fit(X_train_scaled, y_train_scaled)

# plot the results
# plt.scatter(model.predict(X_train_scaled), model.predict(X_train_scaled) - y_train_scaled, c="blue", label="Training Data")
# plt.scatter(model.predict(X_test_scaled), model.predict(X_test_scaled) - y_test_scaled, c="orange", label="Testing Data")
# plt.legend()
# plt.hlines(y=0, xmin=y_test_scaled.min(), xmax=y_test_scaled.max())
# plt.title("Residual Plot")
# plt.show()

# evaluate model
train_predictions = model.predict(X_train_scaled)
training_mse = mean_squared_error(y_train_scaled, train_predictions)
train_r2 = model.score(X_train_scaled, y_train_scaled)

test_predictions = model.predict(X_test_scaled)
testing_mse = mean_squared_error(y_test_scaled, test_predictions)
test_r2 = model.score(X_test_scaled, y_test_scaled)

print(f"Training MSE: {training_mse}, Training R2: {train_r2}")
print(f"Testing MSE: {testing_mse}, Testing R2: {test_r2}")

# export model and scaler
production = LinearRegression()
production.fit(X_train_scaled, y_train)
dump(production, 'model/model.joblib')
dump(X_scaler, 'model/model_scaler.joblib')

# Test Model

# dictionary for state names
us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'DC': 'District of Columbia',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}

# read in data files
data = pd.read_csv('data/derived/final_data.csv')
income_quartile = pd.read_csv('data/derived/ref_2018.csv')

# create dataframe that can be used to select state inputs for model 
sel_state = pd.DataFrame(data['state'])
sel_state['state'] = sel_state['state'].str.upper()
sel_state['st_name'] = sel_state['state'].map(us_state_abbrev)
sel_state = pd.get_dummies(sel_state, columns=['state'])
sel_state = sel_state.drop_duplicates()
sel_state = sel_state.rename(columns={"st_name": "state"})
sel_state['state'] = sel_state['state'].str.lower()
sel_state = sel_state.set_index('state')

# create dataframe that can be used to select income inputs for model 
income_quartile = income_quartile.rename(columns={"State": "state", "_25th_Percentile": "_25", "Median": "_50", "_75th_Percentile": "_75"})
income_quartile['state'] = income_quartile['state'].str.lower()
income_quartile = income_quartile.set_index('state')

# export data frames
sel_state.to_csv(path_or_buf='data/derived/sel_state.csv')
income_quartile.to_csv(path_or_buf='data/derived/income_quartile.csv')

# function that creates input for model based on values provided
sel_state = pd.read_csv('data/derived/sel_state.csv')
sel_state = sel_state.set_index('state')
income_quartile = pd.read_csv('data/derived/income_quartile.csv')
income_quartile = income_quartile.set_index('state')

def user_input(u_year, u_income, u_state, u_gender):
    user_df = pd.DataFrame()
    user_df['year'] = [u_year]
    u_state = u_state.lower()
    if u_income <= income_quartile.loc[u_state, '_25']:
        user_df['quartile'] = [1]
    elif u_income <= income_quartile.loc[u_state, '_50']:
        user_df['quartile'] = [2]
    elif u_income <= income_quartile.loc[u_state, '_75']:
        user_df['quartile'] = [3]
    else:
        user_df['quartile'] = [4]
    user_df['state'] = u_state
    new_df = sel_state.loc[[u_state]]
    user_df = pd.merge(user_df, new_df, on = 'state')
    user_df = user_df.drop(columns=['state'])  
    u_gender = u_gender.lower()
    if u_gender == 'female':
        x = 1
        y = 0
    elif u_gender == 'male':  
        x = 0
        y = 1
    user_df['gender_Female'] = [x]
    user_df['gender_Male'] = [y] 
    return user_df

# import model and scaler
model = load('model/model.joblib')
X_scaler = load('model/model_scaler.joblib')

# test model
mytest = user_input(2020, 10000, 'Alabama', 'Female')
mytest_scaled = X_scaler.transform(mytest)
predict_le = model.predict(mytest_scaled)
print(predict_le)