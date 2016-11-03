# Read data from a excel or csv file
# import pandas module for use
import pandas as pd
from pandas import ExcelWriter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Read csv or xls as data frame
df = pd.read_csv("ConsumerComplaints.csv", low_memory=False)

print(df.shape)  # size of the data

# print((df.dtypes))  # data types

# print(df.columns)  # column names

df = df[["Product", "Sub-product", "Consumer complaint narrative"]]  # pick columns for the dataframe

df["Consumer complaint narrative"].fillna("0", inplace=True)

comments = df["Consumer complaint narrative"].tolist()

print(comments)
# print (df)
# Process

true_k = 2
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(comments)
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i, )
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], )
    print

# save to new CSV file
# df.to_csv('products.csv', encoding='utf-8')

# save to xls

# writer = ExcelWriter('products.xlsx')
# df.to_excel(writer, 'Sheet1')
# writer.save()
