from train_disease import train_disease_model

if __name__ == "__main__":
    # Training script for Rice disease detection
    # Expected dataset structure: training/datasets/rice_diseases/{train,val}/{Healthy,Blast,Bacterial_Blight}
    train_disease_model(
        crop_name='rice', 
        data_dir='training/datasets/rice_diseases',
        model_name='efficientnet_b3'
    )
