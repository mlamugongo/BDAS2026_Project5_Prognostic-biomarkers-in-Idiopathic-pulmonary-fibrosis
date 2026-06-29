# Quick Start Guide

## Installation (Pick One Method)

### 1️⃣ Quick Installation with pip
```bash
cd /path/to/project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Modern Installation (Recommended)
```bash
cd /path/to/project
python -m venv venv
source venv/bin/activate
pip install -e ".[all]"
```

### 3️⃣ With Conda
```bash
conda create -n ipf-fvc python=3.10
conda activate ipf-fvc
pip install -r requirements.txt
```

---

## 🚀 Get Started in 5 Minutes

### Option A: Interactive Notebook (Recommended for Learning)
```bash
jupyter notebook IPF_CT_Analysis_Workshop.ipynb
```
- Open the notebook
- Run cells sequentially
- Modify and experiment with parameters
- See visualizations and results

### Option B: Command Line Pipeline
```bash
python scripts/run_pipeline.py \
    --data-dir ./Dataset \
    --output-dir ./output \
    --n-patients 10
```
- Processes 10 patients
- Extracts features
- Trains model
- Makes predictions
- Saves results to `./output`

### Option C: Python API
```python
from ipf_fvc.pipeline import FVCPredictionPipeline

# Create pipeline
pipeline = FVCPredictionPipeline()

# Process data
features = pipeline.process_dataset('./Dataset/train')

# Train model
pipeline.train_model(X_train, y_train)

# Make predictions
predictions = pipeline.predict(X_test)

# Save model
pipeline.save_model('model.pkl')
```

---

## 📁 Project Files Overview

| File | Purpose |
|------|---------|
| `IPF_CT_Analysis_Workshop.ipynb` | Main educational notebook |
| `README.md` | Full documentation |
| `requirements.txt` | Dependencies list |
| `pyproject.toml` | Python packaging config |
| `ipf_fvc/` | Main Python package |
| `scripts/` | Example scripts |
| `tests/` | Unit tests |

---

## ✅ Verify Installation

```bash
# Test imports
python -c "import ipf_fvc; print('✓ Package imported successfully')"

# Run tests
pytest tests/ -v

# Check dependencies
pip list | grep -E "SimpleITK|pyradiomics|shap|scikit-learn"
```

---

## 🎯 Common Tasks

### Extract Features from Your Own Data
```python
from ipf_fvc import imaging, segmentation, radiomics

# Load DICOM
ct = imaging.load_dicom_series('path/to/dicom/folder')

# Segment lungs
mask = segmentation.segment_lungs_by_threshold(ct)

# Extract features
features = radiomics.extract_radiomics_features(ct, mask, 'patient_id')
```

### Train Custom Model
```python
from ipf_fvc.modeling import create_full_pipeline
from sklearn.model_selection import cross_val_score

model = create_full_pipeline()
scores = cross_val_score(model, X, y, cv=5)
print(f'Cross-validation R²: {scores.mean():.4f}')
```

### Make Predictions
```python
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 🐛 Troubleshooting

**Problem:** "No module named 'ipf_fvc'"
- **Solution:** Install package: `pip install -e "."`

**Problem:** "DICOM files not found"
- **Solution:** Check path format and file structure

**Problem:** Memory error during feature extraction
- **Solution:** Process fewer patients, use smaller resolutions

**Problem:** "lungmask not available"
- **Solution:** It's optional - threshold segmentation will be used instead

---

## 📚 Learn More

- **Full Guide:** See `README.md`
- **API Docs:** Check docstrings in each module
- **Examples:** See `scripts/` directory
- **Tests:** See `tests/` directory

---

## 🎓 Workshop Outline

1. **Setup** (15 min): Installation and environment
2. **Fundamentals** (30 min): Load and visualize DICOM
3. **Segmentation** (30 min): Lung segmentation methods
4. **Features** (1 hour): Radiomics extraction
5. **Selection** (30 min): Feature preselection
6. **Modeling** (1 hour): Train LASSO models
7. **Evaluation** (30 min): Delta FVC and metrics
8. **Explainability** (30 min): SHAP interpretation
9. **Practice** (1 hour): Hands-on exercises

**Total:** ~5 hours

---

## 💡 Tips for Success

1. **Start with the notebook** - It's designed for learning
2. **Use sample data** - 10 patients is enough to start
3. **Check outputs** - Visualizations help understand results
4. **Modify parameters** - Experiment with different settings
5. **Read documentation** - Docstrings have useful info
6. **Run tests** - Ensure everything works on your system

---

## 🔗 Useful Links

- [PyRadiomics Docs](https://pyradiomics.readthedocs.io/)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/modules/lasso.html)
- [SimpleITK Docs](https://simpleitk.readthedocs.io/)

---

## 📞 Need Help?

1. Check README.md - Has troubleshooting section
2. Review the Jupyter notebook - Has detailed explanations
3. Look at docstrings - Type `help(function_name)`
4. Run tests - Shows example usage: `pytest tests/ -v`
5. Contact workshop team - workshop@example.com

---

**Ready to get started?**

Choose your preferred method above and start exploring! 🚀
