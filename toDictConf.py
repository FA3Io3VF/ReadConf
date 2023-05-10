import os
import builtins
import configparser
import validators


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

    def read_config(self):
        config_dict = {}
        try:
            self.config.read(self.config_file)
        except FileNotFoundError:
            print(f"Errore: il file di configurazione '{self.config_file}' non esiste")
            return None
        except Exception as e:
            print(f"Errore durante la lettura del file di configurazione: {str(e)}")
            return None

        try:
            config_dict['DEBUG_MODE'] = self.config.getboolean('ENV', 'DEBUG_MODE')
            config_dict['NO_GUI'] = self.config.getboolean('ENV', 'NO_GUI')
            config_dict['SECRET_KEY'] = self.config.get('API', 'SECRET_KEY')
            config_dict['ALGORITHM'] = self.config.get('API', 'ALGORITHM')
            access_token_expire_minutes = self.config.get('API', 'ACCESS_TOKEN_EXPIRE_MINUTES')
            if not access_token_expire_minutes.isdigit():
                raise ValueError(f"ACCESS_TOKEN_EXPIRE_MINUTES non è un intero valido: {access_token_expire_minutes}")
            config_dict['ACCESS_TOKEN_EXPIRE_MINUTES'] = int(access_token_expire_minutes)
            origins_str = self.config.get('CORS', 'origins')
            origins = [origin.strip() for origin in origins_str.split(",")]
            for origin in origins:
                if not validators.url(origin):
                    raise ValueError(f"'{origin}' non è un link valido")
            config_dict['origins'] = origins
        except configparser.NoOptionError as e:
            print(f"Errore: la chiave '{e.option}' non è presente nel file di configurazione")
            return None
        except configparser.NoSectionError as e:
            print(f"Errore: la sezione '{e.section}' non è presente nel file di configurazione")
            return None
        except ValueError as e:
            print(f"Errore: {str(e)}")
            return None
        except Exception as e:
            print(f"Errore durante l'esportazione delle costanti: {str(e)}")
            return None

        return config_dict


    
if __name__ == '__main__':
    config = Config('config.ini')
    config_dict = config.read_config()
    if config_dict is not None:
        print(config_dict)
    else:
        print("Errore nella lettura del file di configurazione")

