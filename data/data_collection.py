#!/usr/bin/env python3
"""
Data collection script for Protein Interaction GNN project
Downloads AlphaFold structures and STRING interaction data
"""
import os
import requests
import pandas as pd
from pathlib import Path
import time

def download_sample_data():
    """
    Download a small sample dataset to get started
    """
    print("=== Protein Interaction GNN Data Collection ===")
    print("Downloading sample data...")
    
    # Create data directories
    data_dir = Path(".")
    (data_dir / "alphafold").mkdir(exist_ok=True)
    (data_dir / "string").mkdir(exist_ok=True)
    (data_dir / "processed").mkdir(exist_ok=True)
    
    # Sample E. coli proteins (small set to start)
    sample_proteins = [
        "P0A6F5",  # groL (GroEL chaperonin)
        "P0A6F9",  # groS (GroES co-chaperonin)
        "P0A6Y8",  # dnaK (Heat shock protein)
        "P0A6Z3",  # grpE (Heat shock protein)
        "P0A6Z1"   # dnaJ (Heat shock protein)
    ]
    
    print(f"Downloading {len(sample_proteins)} sample protein structures...")
    
    # Download sample structures
    downloaded = 0
    for protein_id in sample_proteins:
        try:
            # AlphaFold URL
            filename = f"AF-{protein_id}-F1-model_v4.pdb"
            url = f"https://alphafold.ebi.ac.uk/files/{filename}"
            
            output_path = data_dir / "alphafold" / filename
            
            if not output_path.exists():
                print(f"Downloading {protein_id}...")
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    downloaded += 1
                    print(f"✓ {protein_id} downloaded")
                else:
                    print(f"✗ Failed to download {protein_id}")
                
                time.sleep(1)  # Be nice to the server
            else:
                print(f"✓ {protein_id} already exists")
                downloaded += 1
                
        except Exception as e:
            print(f"Error downloading {protein_id}: {e}")
    
    print(f"\n✓ Successfully downloaded {downloaded} protein structures")
    print("✓ Files saved in data/alphafold/")
    print("\nNext: Run the data exploration notebook!")
    
    return downloaded

if __name__ == "__main__":
    download_sample_data()