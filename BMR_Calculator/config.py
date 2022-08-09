from configparser import ConfigParser
config = ConfigParser()

config.add_section('Male')
config.set('Male','bmr_constatnt','88.362')
config.set('Male','weight_constant','13.397')
config.set('Male','height_constant','4.799')
config.set('Male','age_constant','5.677')

config.add_section('Female')
config.set('Female','bmr_constatnt','447.593')
config.set('Female','weight_constant','9.247')
config.set('Female','height_constant','3.098')
config.set('Female','age_constant','4.330')


with open(r'config.ini','w')as file:
    config.write(file)