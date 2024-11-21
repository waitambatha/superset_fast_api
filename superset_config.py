# superset_config.py

# Import the SQLAlchemy URI from an external configuration file if desired
from database_config import SQLALCHEMY_DATABASE_URI

# Other Superset configurations
SECRET_KEY = 'JZYE1tXSjEje7ESXd5rcZHiSU3wYofeckvz5TUXfLziWj8mRVtXVRzA'

# Enable Cross-Origin Resource Sharing (CORS)
ENABLE_CORS = True

# Disable SQLAlchemy Track Modifications to reduce overhead
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ensure the SQLAlchemy URI is set to use SQLite, if not already defined in `database_config.py`
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI if SQLALCHEMY_DATABASE_URI else 'sqlite:////app/superset/datasets/medicines.db'

# Optional: configure how long queries should take before being considered "slow"
SQLALCHEMY_DATABASE_URI = 'sqlite:////app/superset/datasets/medicines.db'

# You can also configure other optional parameters, e.g., for authentication or performance tuning
