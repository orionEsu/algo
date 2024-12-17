# Username Generator for Config File

## Prerequisites

- Python 3.8 or newer
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/orionEsu/algo.git
cd algo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

### 4. Access the Application
- Open a web browser
- Navigate to `http://127.0.0.1:5000`

## How to Use
1. Enter the number of usernames to generate (1-20)
2. Choose a character set (lowercase/uppercase/mixed)
3. Click "Generate Users"
4. Click "Download Updated Config" to save the modified configuration file

## Troubleshooting
- Ensure all dependencies are installed
- Check that you have write permissions in the application directory
- Verify Python version compatibility

## Notes
- The application modifies the `config.cfg` file in-place
- Backup your original configuration file before use
