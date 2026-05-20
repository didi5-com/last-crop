from train_disease import train_disease_model

if __name__ == "__main__":
    # Training script for Pepper disease detection
    # Expected dataset structure: training/datasets/pepper_diseases/{train,val}/{Healthy,Bacterial_Spot}
    train_disease_model(
        crop_name='pepper', 
        data_dir='training/datasets/pepper_diseases',
        model_name='efficientnet_b3'
    )
