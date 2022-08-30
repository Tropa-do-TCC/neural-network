def Dcm2jpg():
        with open("../data/list_train.txt", 'w') as f:
            for i in range(1, 200):
                f.write("data" + str(i) + "\n")
            f.close()


Dcm2jpg()
