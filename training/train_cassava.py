from train_disease import train_disease_model

if __name__ == "__main__":
    # Path to your cassava dataset
    # Dataset should have 'train' and 'val' folders
    # Each folder should have subfolders for each disease class
    train_disease_model(
        crop_name='cassava', 
        data_dir='training/datasets/cassava_leaf_disease',
        model_name='efficientnet_b3'
    )
