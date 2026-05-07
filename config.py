import urllib

class Config:
    # 1. Credenciales de tu SQL Server en Docker
    # REEMPLAZA 'TuPasswordAqui' por la clave que pusiste en Docker Desktop
    _user = "sa"
    _pwd = "S3guro\!2025"
    _server = "127.0.0.1,1433"
    _db = "BDD_mi_proyecto_flask"
    _driver = "{ODBC Driver 18 for SQL Server}"

    # 2. Construcción de la cadena de conexión para Mac M4
    _params = urllib.parse.quote_plus(
        f"DRIVER={_driver};"
        f"SERVER={_server};"
        f"DATABASE={_db};"
        f"UID={_user};"
        f"PWD={_pwd};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    # 3. Variable que usará Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={_params}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False