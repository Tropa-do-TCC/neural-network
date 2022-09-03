import read_landmarks_from_database
from util_scripts_data_augmentation import generate_train_file, generate_test_file
import train
import infer

test_list = ["CT-040"]


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
    # TODO: dividir a lista de cts entre 70% treino e 30% teste
    # TODO: verificar se há necessidade de criar um novo shape-model
    generate_train_file.generate_list_train_with_list(ct_folders_list)
    generate_test_file.generate_empty_test_file()
    train.main()


def made_a_test_infer_landmarks_and_reconstruct():
    # STEP 3: Crate test file with 30% and made the test
    generate_test_file.generate_list_test_with_list(test_list)
    infer.main()

    # STEP 4: Reconstruction with predict landmarks
    for test_input in test_list:
        predict_landmarks = read_predict_landmarks("./results/landmarks/test/" + test_input + "_ps.txt")
        # TODO: checar modulo de reconstrucao para confirmar se a pasta é essa msm
        dcm_folder = "../dataset/cq500/CQ500-" + test_input + "/"

        # reconstruction_module.reconstruct(dcm_folder, predict_landmarks)
