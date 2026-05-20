from train_disease import train_disease_model

if __name__ == "__main__":
    # Training script for Maize disease detection
    # Expected dataset structure: training/datasets/maize_diseases/{train,val}/{Healthy,Rust,etc}
    train_disease_model(
        crop_name='maize', 
        data_dir='training/datasets/maize_diseases',
        model_name='efficientnet_b3'
    )
