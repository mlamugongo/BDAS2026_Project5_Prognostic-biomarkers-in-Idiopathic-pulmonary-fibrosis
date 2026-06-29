# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-06-23

### Added

#### Core Features
- DICOM loading and preprocessing using SimpleITK
- Lung segmentation with threshold-based and deep learning methods
- Radiomics feature extraction using PyRadiomics
- Three feature preselection approaches (variance, correlation, mutual information)
- LASSO regression model with cross-validation
- Comprehensive model evaluation with delta FVC analysis
- SHAP-based model explainability
- Complete end-to-end pipeline

#### Package Components
- `ipf_fvc.imaging`: DICOM loading and image preprocessing
- `ipf_fvc.segmentation`: Lung segmentation methods
- `ipf_fvc.radiomics`: Radiomics feature extraction
- `ipf_fvc.feature_selection`: Feature preselection approaches
- `ipf_fvc.modeling`: ML model training and evaluation
- `ipf_fvc.pipeline`: Complete FVCPredictionPipeline class

#### Documentation
- Comprehensive README with installation and usage instructions
- Jupyter notebook with complete workshop tutorial
- Docstrings for all public functions
- Example scripts demonstrating pipeline usage
- Contributing guidelines

#### Testing
- Unit tests for all modules
- Pytest fixtures for test data
- CI/CD configuration (ready)

#### Configuration
- `pyproject.toml` for modern Python packaging
- `requirements.txt` for pip installation
- `setup.py` for backward compatibility
- `.gitignore` for version control

### Technical Stack

**Core Libraries**
- NumPy for numerical computing
- Pandas for data manipulation
- Scikit-learn for machine learning
- SimpleITK for medical image processing
- PyRadiomics for radiomics feature extraction

**Advanced Features**
- SHAP for model explainability
- Plotly for interactive visualization
- Joblib for model serialization

### Performance Metrics

Expected model performance on training data:
- MAE: 50-150 mL
- RMSE: 75-200 mL
- R²: 0.4-0.7
- Mean Absolute % Error: 15-30%

### Known Limitations

1. GPU support requires manual PyTorch installation
2. Large dataset processing may require batch processing
3. Lungmask model requires separate download
4. Clinical data format must match provided specifications

### Future Roadmap

- [ ] Temporal analysis (multiple time points)
- [ ] Deep learning models (CNN, RNN)
- [ ] Web interface for inference
- [ ] LIME explainability option
- [ ] Ensemble model support
- [ ] Model deployment guides
- [ ] Clinical validation studies
- [ ] Privacy-preserving federated learning

## [Unreleased]

### Planned Features
- Multi-model ensemble
- Temporal cohort analysis
- Advanced statistical testing
- Database integration
- REST API for inference
- Docker containerization

---

## How to Update This Changelog

When making contributions:

1. Add your changes under the appropriate section (Added, Changed, Fixed, Deprecated, Removed, Security)
2. Keep entries organized by category
3. Use clear, user-facing language
4. Include PR numbers where applicable
5. Update version numbers following semantic versioning

### Format Examples

**Added Features**
- New feature: description ([#PR](link))

**Bug Fixes**
- Fixed issue: description ([#PR](link))

**Breaking Changes**
- BREAKING: description of change ([#PR](link))
