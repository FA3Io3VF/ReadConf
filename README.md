# ReadConf
Configuration Tool for Web Application

Un tool per la gestione dei parametri di configurazione di una webapp da un file .INI

## Configuration Example

```INI
# Configurazione del progetto
[DEFAULT]
# Titolo del progetto
TITLE = True
# Descrizione del progetto
DESCRIPTION = True
# Versione del progetto
VERSION = True
# Termini e condizioni
TERMS = True
# Metadata dei tag
TAGS_METADATA = [
    {
        "name": "user",
        "description": "Operations with users.",
    },
    {
        "name": "Administration",
        "description": "Administration Area",
        "externalDocs": {
            "description": "Example here",
            "url": "https://myapp.an.example.fakedoc/user_superuser/",
        },
    },
]
# Contatto per il progetto
CONTACT = contact={
        "name": "Test Application",
        "email": "email@testemail.com",
    }
# Informazioni sulla licenza del progetto
LICENSE_INFO = Apache License 2.0

[DEFAULT.DOCS]
# Abilita la documentazione
DOC = True
# URL della documentazione
DOC_URL = https://example.com/docs
# Abilita la REDOC della documentazione
REDOC = True
# URL della REDOC della documentazione
REDOC_URL = https://example.com/redoc

[DEFAULT.DATASOURCE]
# URL del database "LITE"
LITE_DATABASE_URL = sqlite:///example.db
# URL del database SQL
SQLALCHEMY_DATABASE_URL = postgresql://user:password@localhost/example_db

[ENV]
# Abilita la modalità debug
DEBUG_MODE = True
# Da usare con la modalità DEBUG
NO_GUI = True

[API]
# Chiave segreta per la firma dei token JWT
SECRET_KEY = secret_key
# Algoritmo utilizzato per la firma dei token JWT
ALGORITHM = HS256
# Durata in minuti dei token JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30

[CORS]
# Origini consentite per le richieste CORS
origins = https://example.com, https://api.example.com

[SSO]
# URL del servizio CAS
CAS_SERVICE = https://example.com/cas
# URL del servizio di autenticazione
SERVICE_URL = https://example.com/login
# Versione del protocollo CAS
CAS_VERSION = 3.0
```
