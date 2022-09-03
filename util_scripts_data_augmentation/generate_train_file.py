PATH_DATA_FILE_TRAIN = "../data/list_train.txt"
PATH_DATA_FILE_TRAIN_NETWORK = "../neural-network/data/list_train.txt"
PATH_DATA_FILE_TEST_NETWORK = "../neural-network/data/list_test.txt"


def generate_list_train():
    with open(PATH_DATA_FILE_TRAIN, 'w') as f:
        for i in range(1, 200):
            f.write("CT-" + str(i) + "\n")
        f.close()


def generate_list_train_with_list(list_read):
    with open(PATH_DATA_FILE_TRAIN_NETWORK, 'w') as f:
        for folder_read in list_read:
            f.write(folder_read + "\n")
        f.close()
