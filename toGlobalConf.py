import os
import builtins
import configparser
import validators

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

    def read_config(self):
        try:
            self.config.read(self.config_file)
        except FileNotFoundError:
            print(f"Errore: il file di configurazione '{self.config_file}' non esiste")
            return False
        except Exception as e:
            print(f"Errore durante la lettura del file di configurazione: {str(e)}")
            return False

        if not self.export_constants():
            print("Errore durante l'esportazione delle costanti")
            return False
        return True

    def export_constants(self):
        try:
            builtins.TITLE = self.config.getboolean('DEFAULT', 'TITLE')
            builtins.DESCRIPTION = self.config.getboolean('DEFAULT', 'DESCRIPTION')            
            builtins.VERSION = self.config.getboolean('DEFAULT', 'VERSION')            
            builtins.TERMS = self.config.getboolean('DEFAULT', 'TERMS')            
            builtins.TAGS_METADATA = self.config.get('DEFAULT', 'TAGS_METADATA')
            builtins.CONTACT = self.config.get('DEFAULT', 'CONTACT')
            builtins.LICENSE_INFO = self.config.get('DEFAULT', 'LICENSE_INFO')
            
            builtins.DOC = self.config.getboolean('DEFAULT.DOCS', 'DOC')
            builtins.DOC_URL = self.config.get('DEFAULT.DOCS', 'DOC_URL')
            builtins.REDOC = self.config.getboolean('DEFAULT.DOCS', 'REDOC')
            builtins.REDOC_URL = self.config.get('DEFAULT.DOCS', 'REDOC_URL')
            
            builtins.LITE_DATABASE_URL = self.config.get('DEFAULT.DATASOURCE', 'LITE_DATABASE_URL')
            builtins.SQLALCHEMY_DATABASE_URL = self.config.get('DEFAULT.DATASOURCE', 'SQLALCHEMY_DATABASE_URL')
                       
            builtins.DEBUG_MODE = self.config.getboolean('ENV', 'DEBUG_MODE')
            builtins.NO_GUI = self.config.getboolean('ENV', 'NO_GUI')            

            builtins.SECRET_KEY = self.config.get('API', 'SECRET_KEY')
            builtins.ALGORITHM = self.config.get('API', 'ALGORITHM')
             
            access_token_expire_minutes = self.config.get('API', 'ACCESS_TOKEN_EXPIRE_MINUTES')
            if not access_token_expire_minutes.isdigit():
                raise ValueError(f"ACCESS_TOKEN_EXPIRE_MINUTES non è un intero valido: {access_token_expire_minutes}")
            builtins.ACCESS_TOKEN_EXPIRE_MINUTES = int(access_token_expire_minutes)
            
            origins_str = self.config.get('CORS', 'origins')
            origins = [origin.strip() for origin in origins_str.split(",")]
            for origin in origins:
                if not validators.url(origin):
                    raise ValueError(f"'{origin}' non è un link valido")
            builtins.origins = origins
            
            builtins.CAS_SERVICE = self.config.get('SSO', 'CAS_SERVICE')
            builtins.SERVICE_URL = self.config.get('SSO', 'SERVICE_URL')
            builtins.CAS_VERSION = self.config.get('SSO', 'CAS_VERSION')

            
        except configparser.NoOptionError as e:
            print(f"Errore: la chiave '{e.option}' non è presente nel file di configurazione")
            return False
        except configparser.NoSectionError as e:
            print(f"Errore: la sezione '{e.section}' non è presente nel file di configurazione")
            return False
        except ValueError as e:
            print(f"Errore: {str(e)}")
            return False
        except Exception as e:
            print(f"Errore durante l'esportazione delle costanti: {str(e)}")
            return False
        return True
    
if __name__ == '__main__':
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = Config(config_file)
    if config.read_config():
        # Le costanti ora sono disponibili come variabili globali
        print(SECRET_KEY)
        print(DEBUG_MODE)


