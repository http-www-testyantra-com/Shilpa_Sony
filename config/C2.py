from configparser import ConfigParser,ExtendedInterpolation
c = ConfigParser(interpolation=\
                 ExtendedInterpolation())
c.read("D:\\python\\Akshay\\Sample1.ini")
print(c.sections())
print(c.get("settings",'secret_key'))
print(c.options("settings"))
print("DB" in c)
print(c.get('DB','db_port'))
print(c.getint('DB','db_default_port',fallback=330))
print(c.getboolean("settings",'debug'))