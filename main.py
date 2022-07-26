import read_landmarks_from_database
from util_scripts_data_augmentation import generate_train_file, generate_test_file
import train
import infer
from reconstruct import reconstruction


def read_predict_landmarks(file_path):
    with open(file_path) as file:
        new_points = []
        read = file.read().splitlines()
        for line in read:
            points = line.split()
            new_points.append(points)
    return new_points


def train_neural_network_with_dataset():
    # STEP 1: read informations from dataset and generate the files
    read_landmarks_from_database.create_output_folder()
    ct_folders_list = read_landmarks_from_database.generate_files_landmarks_and_nifit("../dataset/")

    # STEP 2: Create train/test files and made neural network train with read ct's
    size = len(ct_folders_list)
    train_set = ct_folders_list[0: int(size*0.7)]
    test_set = ct_folders_list[int(size*0.7): size]

    generate_train_file.generate_list_train_with_list(train_set)
    generate_test_file.generate_list_test_with_list(test_set)
    #train.main()


def made_a_test_infer_landmarks_and_reconstruct():
    # STEP 3: Crate test file with 30% and made the test
    infer.main()

    # STEP 4: Reconstruction with predict landmarks
    test_list = generate_test_file.read_test_file()
    for test_input in test_list:
        original_landmarks = read_predict_landmarks("./data/landmarks_from_ct/" + test_input + "_ps.txt")
        predict_landmarks = read_predict_landmarks("./results/landmarks/test/" + test_input + "_ps.txt")
        # TODO: checar modulo de reconstrucao para confirmar se a pasta é essa msm
        dcm_folder = "./data/" + test_input + "/"
        print(original_landmarks)
        print(predict_landmarks)

        reconstruction.reconstruct_with_landmarks(dcm_folder, original_landmarks, predict_landmarks)

train_neural_network_with_dataset()