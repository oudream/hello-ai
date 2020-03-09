
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

fr = data = open('./AllElectronics.csv')
reader = csv.reader(fr)
headers = next(reader)
headers

feature_list = []
label_list = []

for row in reader:
    label_list.append(row[len(row) - 1])
    row_dict = {}
    for i in range(1,len(row)-1): # 第 1 列是序号，不用存储，因为这一列不参与决策分类
        row_dict[headers[i]] = row[i]
    feature_list.append(row_dict)

vec = DictVectorizer()
dummy_X = vec.fit_transform(feature_list).toarray()
dummy_X


lb = preprocessing.LabelBinarizer()
dummy_y = lb.fit_transform(label_list)
dummy_y

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(dummy_X, dummy_y)

one_row_X = dummy_X[0,:]
one_row_X

one_row_X.reshape(1,-1)

clf.predict(one_row_X.reshape(1,-1))


# 对数据稍作修改，再预测一下。
new_row_X = one_row_X
new_row_X[0] = 1
new_row_X[2] = 0
print("newRowX: " + str(new_row_X))

predicted_y = clf.predict(new_row_X.reshape(1,-1))
print("predictedY: " + str(predicted_y))
