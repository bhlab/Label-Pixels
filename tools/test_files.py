import gdal
import numpy as np

csv_file = "../paths/species_crops_v1_valid2.csv"

data = np.loadtxt(csv_file, delimiter=',', dtype='str')
print(data.shape)
X = data[:, 0]
# 20125 -
# 100000
# 80000 to 100000
# X = X[100000:]
indexes = []
for j, i in enumerate(X):
    if i[-3:] != "jpg":
        # data = np.delete(data, j, 0)
        indexes.append(j)
        # print(i)
print(indexes)
print(len(indexes))
data2 = np.delete(data, indexes, 0)
print(data2.shape)
print(data.shape[0] - data2.shape[0])

np.savetxt("../paths/species_crops_v1_valid.csv", data2, delimiter=",", fmt='%s')
print("done")

# _image = gdal.Open("D:/DIgiKam_test/species_crops\WILD_DOG\TATR_19_BL3_597_A_I__00172.JPG___crop00_mdv4.0.jpg")
# _image = np.array(_image.ReadAsArray())
# print(_image.shape)
# _image
#
# file_name = "../paths/uc_cnn_valid.csv"
# with open(file_name, 'r', newline='\n') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     all_rows = []
#     count = 0
#     for row in plots:
#         _image = gdal.Open(row[0])
#         _image = np.array(_image.ReadAsArray())
#
#         if _image.shape[0] == 3 and _image.shape[1] == 256 and _image.shape[2] == 256:
#             all_rows.append([row[0], row[1]])
#             count += 1
#     print(count)
#
# filename = "../paths/uc_cnn_valid2.csv"
# with open(filename, 'w', newline="\n") as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerows(all_rows)
# print("CSV file created")
