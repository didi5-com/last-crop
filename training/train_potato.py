from train_disease import train_disease_model

if __name__ == "__main__":
    # Training script for Potato disease detection
    # Expected dataset structure: training/datasets/potato_diseases/{train,val}/{Healthy,Early_Blight,Late_Blight}
    train_disease_model(
        crop_name='potato', 
        data_dir='training/datasets/potato_diseases',
        model_name='efficientnet_b3'
    )
