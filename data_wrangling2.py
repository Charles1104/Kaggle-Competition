import pandas as pd
import numpy as np


def total_pers(filename='data/unimelb_training.csv'):
    # Create a new dataframe with a column for the number of persons per team

  unimelb = pd.read_csv(filename)
  tmp_df = pd.DataFrame(np.nan, index=unimelb['Grant.Application.ID'], columns=["num_of_pers"])

# add a column with each role from unimelb and then fill misisng values with 0
  for i in range(1, 16):
      tmp_df["Role." + str(i)] = unimelb[["Role." + str(i)]]
# replace all missing values by 0
  tmp_df = tmp_df.fillna(0)
# replace all non-missing values by 1
  tmp_df.replace('[^0]*', value=1, regex=True, inplace=True)

# sum the number of roles in each line and put the sum into num_of_pers column
  tmp_df["num_of_pers"] = tmp_df.sum(axis=1)

# only keep the index ("grant ID") with the column "num_of_pers"
  tmp_df = pd.DataFrame(tmp_df, columns=["num_of_pers"])

  return tmp_df


def count_countries(filename='data/unimelb_training.csv'):
    # Create a new dataframe with a column for the number of different countries per team

  unimelb = pd.read_csv(filename)
  x = np.empty(len(unimelb))

  tmp_df2 = pd.DataFrame(np.nan, index=unimelb['Grant.Application.ID'], columns=["CountCountries"])

  for i in range(1, 16):
      tmp_df2["Country.of.Birth." + str(i)] = unimelb[["Country.of.Birth." + str(i)]]

  tmp_df2 = tmp_df2.fillna(0)
  for i in range(len(unimelb)):
      x[i] = np.sum((pd.unique(tmp_df2.iloc[i, :])) != 0)
  tmp_df2["CountCountries"] = x

# only keep the index ("grant ID") with the column "CountCountries"
  tmp_df2 = pd.DataFrame(tmp_df2, columns=["CountCountries"])

  return tmp_df2


def avg_age(filename='data/unimelb_training.csv'):

  unimelb = pd.read_csv(filename)
    # Create a new dataframe with a column for the average age per team
  x = np.empty(len(unimelb))

  tmp_df3 = pd.DataFrame(np.nan, index=unimelb['Grant.Application.ID'], columns=["AvAge"])

  for i in range(1, 16):
      tmp_df3["Year.of.Birth." + str(i)] = unimelb[["Year.of.Birth." + str(i)]]

  for i in range(len(unimelb)):
      nan_ctr = tmp_df3.iloc[i, :].isnull().sum()
      x[i] = 2017 - (np.nansum(tmp_df3.iloc[i, :]) / (16 - nan_ctr))
  tmp_df3["AvAge"] = x

# only keep the index ("grant ID") with the column "AvAge"
  tmp_df3 = pd.DataFrame(tmp_df3, columns=["AvAge"])

  tmp_df3["AvAge"].fillna(tmp_df3["AvAge"].mean(), inplace=True)

  return tmp_df3


def years_uni(filename='data/unimelb_training.csv'):

  unimelb = pd.read_csv(filename)
    # Create a new dataframe with a column for the total number of years at university
  x = np.empty(len(unimelb))

  dict_years = {'Less than 0': 0, '>=0 to 5': 2.5, '>5 to 10': 7.5, '>10 to 15': 12.5, 'more than 15': 30}
  tmp_df4 = pd.DataFrame(np.nan, index=unimelb['Grant.Application.ID'], columns=["NbYearsUni"])

  for i in range(1, 16):
      tmp_df4["No..of.Years.in.Uni.at.Time.of.Grant." + str(i)] = unimelb[["No..of.Years.in.Uni.at.Time.of.Grant." + str(i)]]

  tmp_df4 = tmp_df4.replace(dict_years)

  for i in range(len(unimelb)):
      x[i] = np.nansum(tmp_df4.iloc[i, :])
  tmp_df4["NbYearsUni"] = x

# only keep the index ("grant ID") with the column "NbYearsUni"
  tmp_df4 = pd.DataFrame(tmp_df4, columns=["NbYearsUni"])

  return tmp_df4


def total_phd(filename='data/unimelb_training.csv'):

  unimelb = pd.read_csv(filename)
  x = np.empty(len(unimelb))

  tmp_df5 = pd.DataFrame(np.nan, index=unimelb['Grant.Application.ID'], columns=["Nb_Phd"])
  for i in range(1, 16):
      tmp_df5["With.PHD." + str(i)] = unimelb[["With.PHD." + str(i)]]

  tmp_df5 = tmp_df5.fillna(0)
  tmp_df5 = tmp_df5.replace('Yes ', 1)

  for i in range(len(unimelb)):
      x[i] = np.sum(tmp_df5.iloc[i, :])

  tmp_df5["Nb_Phd"] = x

# only keep the index ("grant ID") with the column "Nb_Phd"
  tmp_df5 = pd.DataFrame(tmp_df5, columns=["Nb_Phd"])

  return tmp_df5