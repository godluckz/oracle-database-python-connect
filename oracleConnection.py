import oracledb
from os import environ


def main() -> None:

    w_user    = environ.get("ORACLE_DB_USERNAME")
    w_userpwd = environ.get("ORACLE_DB_PASSWORD")
    if not w_user or not w_userpwd:
        print("Invalid user details")
        return      
        
    w_init_client = environ.get("ORACLE_INIT_CLIENT")
    if not w_init_client:
        print("Invalid Init Client.")
        return
    
    w_host         = environ.get("ORACLE_DB_HOST")
    w_port         = environ.get("ORACLE_DB_PORT")
    w_service_name = environ.get("ORACLE_SERVICE_NAME")
    if not w_host or not w_service_name or not w_port:
        print("Invalid Connection Details")
        return
    
    oracledb.init_oracle_client(lib_dir=w_init_client)        
        
    with oracledb.connect(  user         = w_user, 
                            password     = w_userpwd, 
                            host         = w_host, 
                            port         = w_port, 
                            service_name = w_service_name) as connection:
        print("connected.")
        with connection.cursor() as cursor:
            sql = """select 1 from dual"""
            for r in cursor.execute(sql):
                print(r)


if __name__ == "__main__":
    main()