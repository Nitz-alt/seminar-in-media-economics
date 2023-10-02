import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Loading data and combining
form1 = pd.read_csv('form1.csv')
form2 = pd.read_csv('form2.csv')
form3 = pd.read_csv('form3.csv')
form4 = pd.read_csv('form4.csv')
combined_form = pd.concat([form1, form2, form3, form4])

# Regression models
model1 = smf.ols('post1_agree ~ men_post1 + old_post1', data=combined_form).fit()
print(model1.summary())

model2 = smf.ols('post2_agree ~ men_post2 + old_post2', data=combined_form).fit()
print(model2.summary())

model3 = smf.ols('post3_agree ~ men_post3 + old_post3', data=combined_form).fit()
print(model3.summary())

model4 = smf.ols('post4_agree ~ men_post4 + old_post4', data=combined_form).fit()
print(model4.summary())

combined_form['age35'] = (combined_form['age'] >= 35).astype(int)

model5 = smf.ols('post1_agree ~ men_post1 * sex + old_post1 * age35 + pro_reform + pro_protest', data=combined_form).fit()
print(model5.summary())

model6 = smf.ols('post2_agree ~ men_post2 * sex + old_post2 * age35 + pro_reform + pro_protest', data=combined_form).fit()
print(model6.summary())

model7 = smf.ols('post3_agree ~ men_post3 * sex + old_post3 * age35 + pro_arnona', data=combined_form).fit()
print(model7.summary())

combined_form_no_arnona = combined_form[combined_form['pro_arnona'] != 2]
model8 = smf.ols('post4_agree ~ men_post4 * sex + old_post4 * age35 + pro_arnona', data=combined_form_no_arnona).fit()
print(model8.summary())

# Reshaping data for overall regression
reshaped_dfs = []

for i in range(1, 5):
    cols = [f'post{i}_agree', f'men_post{i}', f'old_post{i}', 'sex', 'age']
    temp_df = combined_form[cols]
    temp_df.columns = ['post_agree', 'men_post', 'old_post', 'sex', 'age']
    reshaped_dfs.append(temp_df)

complete_data = pd.concat(reshaped_dfs)

model9 = smf.ols('post_agree ~ men_post + old_post', data=complete_data).fit()
print(model9.summary())

complete_data['age35'] = (complete_data['age'] >= 35).astype(int)
model10 = smf.ols('post_agree ~ men_post * sex + old_post * age35', data=complete_data).fit()
print(model10.summary())
