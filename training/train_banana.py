from train_disease import train_disease_model

if __name__ == "__main__":
    # Training script for Banana disease detection
    # Expected dataset structure: training/datasets/banana_diseases/{train,val}/{Healthy,Sigatoka}
    train_disease_model(
        crop_name='banana', 
        data_dir='training/datasets/banana_diseases',
        model_name='efficientnet_b3'
    )
