from matplotlib import pyplot as plt
from GRAPHPack.Model import FormValues
class MyForm:

    def sub(self):
        aa=FormValues()
        aa.value()
    def Newform(self):
        res=" "
        tup1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        tup2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        print(tup1[11])
        # print(len(res))
        for i in range(len(res)):
            # print(res[i])
            r = res[i]
            # print(r[0])
            # count=0
            if r[0] == 1:
                tup2[0] = tup2[0] + 1
            if r[0] == 2:
                tup2[1] = tup2[1] + 1
            if r[0] == 3:
                tup2[2] = tup2[2] + 1
            if r[0] == 4:
                tup2[3] = tup2[3] + 1
            if r[0] == 5:
                tup2[4] = tup2[4] + 1
            if r[0] == 6:
                tup2[5] = tup2[5] + 1
            if r[0] == 7:
                tup2[6] = tup2[6] + 1
            if r[0] == 8:
                tup2[7] = tup2[7] + 1
            if r[0] == 9:
                tup2[8] = tup2[8] + 1
            if r[0] == 10:
                tup2[9] = tup2[9] + 1
            if r[0] == 11:
                tup2[10] = tup2[10] + 1
            if r[0] == 12:
                tup2[11] = tup2[11] + 1

        print(" ", tup1)
        print(" ", tup2)

        plt.bar(tup1, tup2)
        plt.show()

