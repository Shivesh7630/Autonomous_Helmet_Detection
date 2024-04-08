import os
import random
import yaml
import argparse

class Create_Data_Yaml:

    def __init__(self, images_path, labels_path, class_names_file):
        # Constructor to initialize the object with the project name and create required files
        self.image_path = images_path
        self.labels_path = labels_path
        self.class_names_file = class_names_file
        self.create_train_val_test_txt()
        self.create_yaml_file()

    def create_train_val_test_txt(self, val_split=0.1, test_split=0.1):
        # Function to create train, validation, and test txt files with image and label paths
        images_dir = os.path.join(self.image_path)
        annotations_dir = os.path.join(self.labels_path)

        # Get list of image files
        image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

        # Split images into train, validation, and test sets
        num_val = int(len(image_files) * val_split)
        num_test = int(len(image_files) * test_split)

        val_images = random.sample(image_files, num_val)
        remaining_images = [img for img in image_files if img not in val_images]
        test_images = random.sample(remaining_images, num_test)
        train_images = [img for img in remaining_images if img not in test_images]

        # Write train.txt, val.txt, and test.txt
        for split, image_list in zip(["train", "val", "test"], [train_images, val_images, test_images]):
            self.write_image_txt_file(os.path.join("Data", f"image_{split}.txt"),
                                      image_list, annotations_dir)
            self.write_label_txt_file(os.path.join("Data", f"label_{split}.txt"),
                                      image_list, annotations_dir)

    def write_image_txt_file(self, output_file, image_list, annotations_dir):
        # Function to write image paths to a text file
        with open(output_file, 'w') as file:
            for img_file in image_list:
                img_path = os.path.join("images", img_file)
                file.write(f"{img_path}\n")

    def write_label_txt_file(self, output_file, image_list, annotations_dir):
        # Function to write label paths to a text file
        with open(output_file, 'w') as file:
            for img_file in image_list:
                annotation_file = os.path.splitext(img_file)[0] + ".txt"
                annotation_path = os.path.join("labels", annotation_file)
                file.write(f"{annotation_path}\n")

    def create_class_name_for_yaml(self):
        # Function to create a dictionary of class names based on label files
        cat_names = []
        with open(self.class_names_file, 'r') as f:
            cat_names = [line.strip() for line in f if line.strip()]

        return {idx: name for idx, name in enumerate(cat_names, start=0)}

    def create_yaml_dict(self):
        # Function to create a dictionary for YAML file with paths and class names
        self.yaml_dict = {
            "path": f"../Data/",

            "train": {
                "images": os.path.join("image_train.txt"),
                "labels": os.path.join("label_train.txt"),
            },

            "val": {
                "images": os.path.join("image_val.txt"),
                "labels": os.path.join("label_val.txt"),
            },

            "test": {
                "images": os.path.join("image_test.txt"),
                "labels": os.path.join("label_test.txt"),
            },

            "names": self.create_class_name_for_yaml()
        }

    def create_yaml_file(self):
        # Function to create the YAML file with the generated dictionary
        self.create_yaml_dict()

        yaml_file_path = os.path.join("Data", "data.yaml")

        with open(yaml_file_path, 'w') as yaml_file:
            yaml.dump(self.yaml_dict, yaml_file, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create data YAML file.')
    parser.add_argument('images_path', type=str, help='Path to the folder containing images')
    parser.add_argument('labels_path', type=str, help='Path to the folder containing labels')
    parser.add_argument('class_names_file', type=str, help='Path to the text file containing class names')
    args = parser.parse_args()

    create_data_yaml = Create_Data_Yaml(args.images_path, args.labels_path, args.class_names_file)
