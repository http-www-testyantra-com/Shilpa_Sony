from configparser import ConfigParser

c = ConfigParser()
c["settings"] = {
    'debug' : "true",
    'secret_key':"abc123",
    'log_path' : "D:\python\Akshay"
}
c["DB"] = {
    'db_name' : 'MySql',
    'db_type' : "RDBMS",
    'db_port' : 8888


}
f = open("D:\\python\\Akshay\\Sample1.ini","w")
c.write(f)
f.close()