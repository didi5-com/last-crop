from train_disease import train_disease_model

if __name__ == "__main__":
    train_disease_model(
        crop_name='tomato', 
        data_dir='training/datasets/plantvillage_tomato',
        model_name='resnet50'
    )
