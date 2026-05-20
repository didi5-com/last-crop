from train_disease import train_disease_model

if __name__ == "__main__":
    # Training script for Mango disease detection
    # Expected dataset structure: training/datasets/mango_diseases/{train,val}/{Healthy,Anthracnose}
    train_disease_model(
        crop_name='mango', 
        data_dir='training/datasets/mango_diseases',
        model_name='efficientnet_b3'
    )
