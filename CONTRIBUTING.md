# 🤝 Contributing to Celestial Circuitry AI

Thank you for your interest in contributing to Celestial Circuitry AI! We welcome contributions from the community and are excited to work with you.

## 🌟 How to Contribute

### 🐛 Bug Reports
- Use the [GitHub Issues](https://github.com/Ayushkr-iitm/celestial-circuitry-ai/issues) page
- Include detailed steps to reproduce the bug
- Provide system information (OS, Python version, etc.)
- Include error messages and screenshots if applicable

### ✨ Feature Requests
- Open a new issue with the "enhancement" label
- Describe the feature in detail
- Explain how it would benefit the project
- Consider implementation complexity

### 🔧 Code Contributions
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Make your changes
- Add tests if applicable
- Submit a pull request

## 🚀 Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Setup Steps
1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/Ayushkr-iit/celestial-circuitry-ai.git
   cd celestial-circuitry-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep the first line under 50 characters
- Add more details in the body if needed

### Example:
```
Add: New feature for exoplanet classification
- Implemented advanced BLS algorithm
- Added confidence scoring system
- Updated UI with new visualizations
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_feature_extractor.py

# Run with coverage
python -m pytest --cov=utils --cov=models
```

### Test Structure
- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Test both success and failure cases

## 📝 Documentation

### Code Documentation
- Add docstrings to all functions and classes
- Include parameter descriptions and return types
- Provide usage examples for complex functions

### Example:
```python
def process_light_curve(file_path: str) -> dict:
    """
    Process stellar light curve data for exoplanet detection.
    
    Args:
        file_path (str): Path to the light curve data file
        
    Returns:
        dict: Processed data with features and metadata
        
    Example:
        >>> result = process_light_curve('data/sample.csv')
        >>> print(result['features'])
    """
```

### README Updates
- Update README.md when adding new features
- Include installation instructions for new dependencies
- Add usage examples for new functionality

## 🎨 UI/UX Contributions

### Design Guidelines
- Maintain the space theme and aesthetic
- Ensure responsive design for all screen sizes
- Use consistent color schemes and typography
- Test on different browsers and devices

### CSS Guidelines
- Use meaningful class names
- Keep styles organized and commented
- Use CSS variables for consistent theming
- Optimize for performance

## 🔬 Scientific Contributions

### Astronomy Guidelines
- Follow standard astronomical conventions
- Use appropriate units and measurements
- Cite relevant research papers
- Validate against known exoplanet data

### AI/ML Guidelines
- Document model architecture and parameters
- Include performance metrics
- Provide training data information
- Explain feature engineering decisions

## 📊 Pull Request Process

### Before Submitting
1. **Test your changes thoroughly**
2. **Update documentation if needed**
3. **Ensure all tests pass**
4. **Check code style and formatting**

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] UI/UX enhancement

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## 🏷️ Issue Labels

We use the following labels to categorize issues:

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `question`: Further information requested
- `wontfix`: Will not be fixed
- `duplicate`: Issue already exists

## 🌟 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation
- Social media acknowledgments

## 📞 Getting Help

### Community Support
- **GitHub Discussions**: For questions and general discussion
- **GitHub Issues**: For bug reports and feature requests
- **Email**: your.email@example.com

### Code Review Process
- All PRs require at least one review
- Maintainers will provide feedback within 48 hours
- Address all feedback before merging
- Be patient and respectful during reviews

## 🎯 Project Goals

### Short Term
- Improve model accuracy
- Add more data sources
- Enhance UI/UX
- Optimize performance

### Long Term
- Support for more telescopes
- Advanced visualization tools
- Real-time data processing
- Mobile application

## 📈 Contribution Metrics

We track contributions in:
- Lines of code contributed
- Issues resolved
- Features implemented
- Documentation improvements
- Community engagement

## 🙏 Thank You

Thank you for contributing to Celestial Circuitry AI! Your contributions help advance exoplanet discovery and make space exploration more accessible to everyone.

---

**Happy Coding!** 🚀✨
