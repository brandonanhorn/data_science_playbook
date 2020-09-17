import pandas as pd
from sklearn_pandas import DataFrameMapper, CategoricalImputer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.feature_selection import SelectPercentile
from sklearn.pipeline import make_pipeline
import mummify

df = pd.read_csv('ames.csv')
df = df.drop('Id', axis=1)

target = 'SalePrice'
X = df.drop(target, axis=1)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# pd.DataFrame(df.dtypes).sort_values(0).to_dict()[0]

mapper = DataFrameMapper([
    (['MSSubClass'], [SimpleImputer(), StandardScaler()]),
    (['BsmtUnfSF'], [SimpleImputer(), StandardScaler()]),
    (['TotalBsmtSF'], [SimpleImputer(), StandardScaler()]),
    (['1stFlrSF'], [SimpleImputer(), StandardScaler()]),
    (['2ndFlrSF'], [SimpleImputer(), StandardScaler()]),
    (['LowQualFinSF'], [SimpleImputer(), StandardScaler()]),
    (['GrLivArea'], [SimpleImputer(), StandardScaler()]),
    (['BsmtFullBath'], [SimpleImputer(), StandardScaler()]),
    (['BsmtHalfBath'], [SimpleImputer(), StandardScaler()]),
    (['FullBath'], [SimpleImputer(), StandardScaler()]),
    (['HalfBath'], [SimpleImputer(), StandardScaler()]),
    (['BedroomAbvGr'], [SimpleImputer(), StandardScaler()]),
    (['KitchenAbvGr'], [SimpleImputer(), StandardScaler()]),
    (['TotRmsAbvGrd'], [SimpleImputer(), StandardScaler()]),
    (['Fireplaces'], [SimpleImputer(), StandardScaler()]),
    (['GarageCars'], [SimpleImputer(), StandardScaler()]),
    (['GarageArea'], [SimpleImputer(), StandardScaler()]),
    (['WoodDeckSF'], [SimpleImputer(), StandardScaler()]),
    (['OpenPorchSF'], [SimpleImputer(), StandardScaler()]),
    (['EnclosedPorch'], [SimpleImputer(), StandardScaler()]),
    (['3SsnPorch'], [SimpleImputer(), StandardScaler()]),
    (['ScreenPorch'], [SimpleImputer(), StandardScaler()]),
    (['PoolArea'], [SimpleImputer(), StandardScaler()]),
    (['MiscVal'], [SimpleImputer(), StandardScaler()]),
    (['MoSold'], [SimpleImputer(), StandardScaler()]),
    (['YrSold'], [SimpleImputer(), StandardScaler()]),
    (['BsmtFinSF2'], [SimpleImputer(), StandardScaler()]),
    (['BsmtFinSF1'], [SimpleImputer(), StandardScaler()]),
    (['LotArea'], [SimpleImputer(), StandardScaler()]),
    (['OverallQual'], [SimpleImputer(), StandardScaler()]),
    (['OverallCond'], [SimpleImputer(), StandardScaler()]),
    (['YearBuilt'], [SimpleImputer(), StandardScaler()]),
    (['YearRemodAdd'], [SimpleImputer(), StandardScaler()]),
    (['LotFrontage'], [SimpleImputer(), StandardScaler()]),
    (['MasVnrArea'], [SimpleImputer(), StandardScaler()]),
    (['GarageYrBlt'], [SimpleImputer(), StandardScaler()]),
    ('BsmtQual', [CategoricalImputer(), LabelBinarizer()]),
    ('GarageFinish', [CategoricalImputer(), LabelBinarizer()]),
    ('Neighborhood', [CategoricalImputer(), LabelBinarizer()]),
    ('LandSlope', [CategoricalImputer(), LabelBinarizer()]),
    ('GarageQual', [CategoricalImputer(), LabelBinarizer()]),
    ('GarageCond', [CategoricalImputer(), LabelBinarizer()]),
    ('PavedDrive', [CategoricalImputer(), LabelBinarizer()]),
    ('Utilities', [CategoricalImputer(), LabelBinarizer()]),
    ('LandContour', [CategoricalImputer(), LabelBinarizer()]),
    ('LotShape', [CategoricalImputer(), LabelBinarizer()]),
    ('Alley', [CategoricalImputer(), LabelBinarizer()]),
    ('Street', [CategoricalImputer(), LabelBinarizer()]),
    ('PoolQC', [CategoricalImputer(strategy='constant', fill_value='Unknown'), LabelBinarizer()]),
    ('Fence', [CategoricalImputer(), LabelBinarizer()]),
    ('MiscFeature', [CategoricalImputer(), LabelBinarizer()]),
    ('MSZoning', [CategoricalImputer(), LabelBinarizer()]),
    ('SaleType', [CategoricalImputer(), LabelBinarizer()]),
    ('LotConfig', [CategoricalImputer(), LabelBinarizer()]),
    ('GarageType', [CategoricalImputer(), LabelBinarizer()]),
    ('Functional', [CategoricalImputer(), LabelBinarizer()]),
    ('Condition1', [CategoricalImputer(), LabelBinarizer()]),
    ('BsmtCond', [CategoricalImputer(), LabelBinarizer()]),
    ('BsmtExposure', [CategoricalImputer(), LabelBinarizer()]),
    ('BsmtFinType1', [CategoricalImputer(), LabelBinarizer()]),
    ('ExterCond', [CategoricalImputer(), LabelBinarizer()]),
    ('BsmtFinType2', [CategoricalImputer(), LabelBinarizer()]),
    ('ExterQual', [CategoricalImputer(), LabelBinarizer()]),
    ('MasVnrType', [CategoricalImputer(), LabelBinarizer()]),
    ('Heating', [CategoricalImputer(), LabelBinarizer()]),
    ('SaleCondition', [CategoricalImputer(), LabelBinarizer()]),
    ('FireplaceQu', [CategoricalImputer(), LabelBinarizer()]),
    ('CentralAir', [CategoricalImputer(), LabelBinarizer()]),
    ('Exterior2nd', [CategoricalImputer(), LabelBinarizer()]),
    ('Exterior1st', [CategoricalImputer(), LabelBinarizer()]),
    ('RoofMatl', [CategoricalImputer(), LabelBinarizer()]),
    ('RoofStyle', [CategoricalImputer(), LabelBinarizer()]),
    ('HouseStyle', [CategoricalImputer(), LabelBinarizer()]),
    ('BldgType', [CategoricalImputer(), LabelBinarizer()]),
    ('KitchenQual', [CategoricalImputer(), LabelBinarizer()]),
    ('Condition2', [CategoricalImputer(), LabelBinarizer()]),
    ('Foundation', [CategoricalImputer(), LabelBinarizer()]),
    ('Electrical', [CategoricalImputer(), LabelBinarizer()]),
    ('HeatingQC', [CategoricalImputer(), LabelBinarizer()])
    ], df_out=True
)

Z_train = mapper.fit_transform(X_train)
Z_test = mapper.transform(X_test)

model = LinearRegression().fit(Z_train, y_train)
model.score(Z_test, y_test)

select = SelectPercentile(percentile=10)
select.fit(Z_train, y_train)

Z_train = select.transform(Z_train)
Z_test = select.transform(Z_test)

model = Lasso()
params = {
    'alpha': [1, 10, 100, 1000, 10000],
    'fit_intercept': [True, False]
}

grid = GridSearchCV(model, params, cv=3, n_jobs=-1, verbose=1)

grid.fit(Z_train, y_train)
grid.best_score_
grid.best_params_

model = grid.best_estimator_

model.score(Z_train, y_train)
score = model.score(Z_test, y_test)

pipe = make_pipeline(mapper, select, grid)

pipe.fit(X_train, y_train)
pipe.predict(X_test)

mummify.log(f'Built full pipeline, test score is {score}')
