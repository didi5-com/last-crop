TREATMENTS = {
    "cassava": {
        "Cassava Mosaic Disease (CMD)": {
            "severity": "High",
            "symptoms": "Leaf chlorosis, distortion, and stunted growth.",
            "causes": "Whitefly-transmitted virus.",
            "organic_treatment": "Use disease-free cuttings and remove infected plants.",
            "chemical_treatment": "No direct chemical treatment for the virus; control whiteflies with neem oil.",
            "prevention": "Plant resistant varieties like TMS 30572.",
            "fertilizer_recommendation": "High potassium fertilizer to boost tuber health.",
            "isolation_advice": "Immediately remove and burn infected plants.",
            "watering_advice": "Ensure consistent moisture but avoid waterlogging."
        },
        "Brown Leaf Spot": {
            "severity": "Medium",
            "symptoms": "Brown circular spots on older leaves.",
            "causes": "Fungus (Cercospora henningsii).",
            "organic_treatment": "Prune infected leaves and improve air circulation.",
            "chemical_treatment": "Copper-based fungicides if severe.",
            "prevention": "Avoid overhead irrigation; use wider plant spacing.",
            "fertilizer_recommendation": "Balanced NPK 15-15-15.",
            "isolation_advice": "Remove lower infected leaves.",
            "watering_advice": "Water at the base of the plant."
        }
    },
    "tomato": {
        "Early Blight": {
            "severity": "Medium to High",
            "symptoms": "Target-like spots on older leaves, yellowing.",
            "causes": "Fungus (Alternaria solani).",
            "organic_treatment": "Compost tea spray and mulching.",
            "chemical_treatment": "Chlorothalonil or Mancozeb.",
            "prevention": "Crop rotation and staking plants.",
            "fertilizer_recommendation": "Calcium-rich fertilizer to prevent secondary issues.",
            "isolation_advice": "Remove lower branches to prevent soil splash.",
            "watering_advice": "Drip irrigation only."
        },
        "Late Blight": {
            "severity": "Critical",
            "symptoms": "Dark, water-soaked patches on leaves and fruit.",
            "causes": "Oomycete (Phytophthora infestans).",
            "organic_treatment": "Copper sprays (OMRI listed).",
            "chemical_treatment": "Ridomil Gold or similar systemic fungicides.",
            "prevention": "Avoid planting near potatoes; use resistant hybrids.",
            "fertilizer_recommendation": "Phosphorus-heavy fertilizer.",
            "isolation_advice": "Destroy entire plant immediately if detected.",
            "watering_advice": "Keep foliage dry at all costs."
        }
    },
    "maize": {
        "Maize Rust": {
            "severity": "Medium",
            "symptoms": "Orange pustules on leaves.",
            "causes": "Fungus (Puccinia sorghi).",
            "organic_treatment": "Sulfur-based organic dusts.",
            "chemical_treatment": "Triazole fungicides.",
            "prevention": "Plant early in the season; use resistant hybrids.",
            "fertilizer_recommendation": "Nitrogen-rich fertilizer.",
            "isolation_advice": "Monitor nearby fields.",
            "watering_advice": "Standard maize irrigation."
        }
    },
    "potato": {
        "Early Blight": {
            "severity": "Medium",
            "symptoms": "Dark brown spots with concentric rings.",
            "causes": "Fungus (Alternaria solani).",
            "organic_treatment": "Crop rotation and removing debris.",
            "chemical_treatment": "Mancozeb or Chlorothalonil.",
            "prevention": "Avoid overhead watering.",
            "fertilizer_recommendation": "High phosphorus at planting.",
            "isolation_advice": "Remove infected foliage.",
            "watering_advice": "Keep soil moist but not wet."
        },
        "Late Blight": {
            "severity": "Critical",
            "symptoms": "Dark, water-soaked patches on leaves.",
            "causes": "Phytophthora infestans.",
            "organic_treatment": "Copper-based fungicides.",
            "chemical_treatment": "Systemic fungicides like Ridomil.",
            "prevention": "Use certified seed potatoes.",
            "fertilizer_recommendation": "Balanced NPK.",
            "isolation_advice": "Destroy infected plants immediately.",
            "watering_advice": "Avoid evening watering."
        }
    },
    "rice": {
        "Rice Blast": {
            "severity": "High",
            "symptoms": "Spindle-shaped spots with gray centers.",
            "causes": "Fungus (Magnaporthe oryzae).",
            "organic_treatment": "Proper water management and silicon fertilizer.",
            "chemical_treatment": "Tricyclazole or Carbendazim.",
            "prevention": "Use resistant varieties and balanced nitrogen.",
            "fertilizer_recommendation": "Avoid excessive nitrogen.",
            "isolation_advice": "Burn stubble after harvest.",
            "watering_advice": "Maintain consistent water levels."
        },
        "Bacterial Leaf Blight": {
            "severity": "High",
            "symptoms": "Yellowing and drying of leaf tips.",
            "causes": "Bacteria (Xanthomonas oryzae).",
            "organic_treatment": "Field sanitation and balanced nutrition.",
            "chemical_treatment": "Copper hydroxide if detected early.",
            "prevention": "Avoid field flooding during early stages.",
            "fertilizer_recommendation": "Potassium-rich fertilizers.",
            "isolation_advice": "Keep fields well-drained.",
            "watering_advice": "Controlled irrigation."
        }
    },
    "banana": {
        "Black Sigatoka": {
            "severity": "Critical",
            "symptoms": "Dark streaks on leaves, leading to leaf death.",
            "causes": "Fungus (Mycosphaerella fijiensis).",
            "organic_treatment": "Pruning and removing infected leaves.",
            "chemical_treatment": "Fungicide rotations (Mancozeb, etc.).",
            "prevention": "Good drainage and proper spacing.",
            "fertilizer_recommendation": "High potassium for fruit quality.",
            "isolation_advice": "De-leaf regularly.",
            "watering_advice": "Avoid wetting foliage."
        }
    },
    "mango": {
        "Anthracnose": {
            "severity": "High",
            "symptoms": "Dark, sunken spots on leaves and fruit.",
            "causes": "Fungus (Colletotrichum gloeosporioides).",
            "organic_treatment": "Neem oil or potassium bicarbonate.",
            "chemical_treatment": "Copper-based fungicides.",
            "prevention": "Post-harvest heat treatment for fruit.",
            "fertilizer_recommendation": "Micronutrient sprays (Zinc, Boron).",
            "isolation_advice": "Prune dead branches.",
            "watering_advice": "Water at the drip line."
        }
    }
}

def get_treatment_plan(crop, disease):
    """
    Stage 5: AI Agricultural Recommendation Engine.
    Returns detailed treatment and advice for a specific crop and disease.
    """
    crop_data = TREATMENTS.get(crop.lower(), {})
    plan = crop_data.get(disease, {
        "severity": "Unknown",
        "symptoms": "Consult an agricultural expert for detailed symptoms.",
        "causes": "Unknown biological or environmental factor.",
        "organic_treatment": "General organic compost and soil health improvement.",
        "chemical_treatment": "Consult a local specialist for approved treatments.",
        "prevention": "General crop hygiene and rotation.",
        "fertilizer_recommendation": "Standard NPK balance.",
        "isolation_advice": "Keep the plant observed for further changes.",
        "watering_advice": "Maintain standard soil moisture."
    })
    return plan
