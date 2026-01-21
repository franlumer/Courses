from pydantic import BaseModel

class User(BaseModel): # User(id = id, name = "name", email = "email", age = age)
    username :str
    full_name : str
    email : str
    disabled : bool

class UserDB(User):
    password : str

users_db = {
    'luciano': {
        "username": "luciano",
        "full_name": "Luciano",
        "email": "franlumer09@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'florencia': {
        "username": "florencia",
        "full_name": "Florencia",
        "email": "bflorenciaaraceli@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'franco': {
        "username": "franco",
        "full_name": "Franco",
        "email": "example.example@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'test': {
        "username": "test",
        "full_name": "test",
        "email": "tes@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'santiago': {
        "username": "santiago",
        "full_name": "Santiago",
        "email": "santiago.rodriguez@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'maria': {
        "username": "maria",
        "full_name": "María",
        "email": "maria.gonzalez@hotmail.com",
        "disabled": False,
        "password": "123456"
    },
    'diego': {
        "username": "diego",
        "full_name": "Diego",
        "email": "diego.martinez@yahoo.com",
        "disabled": True,
        "password": "123456"
    },
    'valentina': {
        "username": "valentina",
        "full_name": "Valentina",
        "email": "valentina.lopez@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'mateo': {
        "username": "mateo",
        "full_name": "Mateo",
        "email": "mateo.fernandez@outlook.com",
        "disabled": True,
        "password": "123456"
    },
    'camila': {
        "username": "camila",
        "full_name": "Camila",
        "email": "camila.garcia@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'nicolas': {
        "username": "nicolas",
        "full_name": "Nicolás",
        "email": "nicolas.perez@hotmail.com",
        "disabled": False,
        "password": "123456"
    },
    'sofia': {
        "username": "sofia",
        "full_name": "Sofía",
        "email": "sofia.sanchez@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'joaquin': {
        "username": "joaquin",
        "full_name": "Joaquín",
        "email": "joaquin.romero@yahoo.com",
        "disabled": False,
        "password": "123456"
    },
    'isabella': {
        "username": "isabella",
        "full_name": "Isabella",
        "email": "isabella.torres@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'tomas': {
        "username": "tomas",
        "full_name": "Tomás",
        "email": "tomas.diaz@outlook.com",
        "disabled": False,
        "password": "123456"
    },
    'martina': {
        "username": "martina",
        "full_name": "Martina",
        "email": "martina.ruiz@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'benjamin': {
        "username": "benjamin",
        "full_name": "Benjamín",
        "email": "benjamin.morales@hotmail.com",
        "disabled": False,
        "password": "123456"
    },
    'emma': {
        "username": "emma",
        "full_name": "Emma",
        "email": "emma.castro@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'lucas': {
        "username": "lucas",
        "full_name": "Lucas",
        "email": "lucas.vargas@yahoo.com",
        "disabled": False,
        "password": "123456"
    },
    'mia': {
        "username": "mia",
        "full_name": "Mía",
        "email": "mia.silva@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'agustin': {
        "username": "agustin",
        "full_name": "Agustín",
        "email": "agustin.mendez@outlook.com",
        "disabled": False,
        "password": "123456"
    },
    'catalina': {
        "username": "catalina",
        "full_name": "Catalina",
        "email": "catalina.rojas@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'thiago': {
        "username": "thiago",
        "full_name": "Thiago",
        "email": "thiago.herrera@hotmail.com",
        "disabled": True,
        "password": "123456"
    },
    'julieta': {
        "username": "julieta",
        "full_name": "Julieta",
        "email": "julieta.flores@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'emiliano': {
        "username": "emiliano",
        "full_name": "Emiliano",
        "email": "emiliano.ortiz@yahoo.com",
        "disabled": True,
        "password": "123456"
    },
    'antonella': {
        "username": "antonella",
        "full_name": "Antonella",
        "email": "antonella.rios@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'bautista': {
        "username": "bautista",
        "full_name": "Bautista",
        "email": "bautista.nunez@outlook.com",
        "disabled": False,
        "password": "123456"
    },
    'renata': {
        "username": "renata",
        "full_name": "Renata",
        "email": "renata.vega@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'lautaro': {
        "username": "lautaro",
        "full_name": "Lautaro",
        "email": "lautaro.molina@hotmail.com",
        "disabled": False,
        "password": "123456"
    },
    'victoria': {
        "username": "victoria",
        "full_name": "Victoria",
        "email": "victoria.jimenez@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'facundo': {
        "username": "facundo",
        "full_name": "Facundo",
        "email": "facundo.cruz@yahoo.com",
        "disabled": False,
        "password": "123456"
    },
    'delfina': {
        "username": "delfina",
        "full_name": "Delfina",
        "email": "delfina.reyes@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'santino': {
        "username": "santino",
        "full_name": "Santino",
        "email": "santino.gutierrez@outlook.com",
        "disabled": False,
        "password": "123456"
    },
    'francesca': {
        "username": "francesca",
        "full_name": "Francesca",
        "email": "francesca.ramos@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'lorenzo': {
        "username": "lorenzo",
        "full_name": "Lorenzo",
        "email": "lorenzo.luna@hotmail.com",
        "disabled": True,
        "password": "123456"
    },
    'olivia': {
        "username": "olivia",
        "full_name": "Olivia",
        "email": "olivia.campos@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'juancruz': {
        "username": "juancruz",
        "full_name": "Juan Cruz",
        "email": "juancruz.medina@yahoo.com",
        "disabled": True,
        "password": "123456"
    },
    'alma': {
        "username": "alma",
        "full_name": "Alma",
        "email": "alma.sosa@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'matias': {
        "username": "matias",
        "full_name": "Matías",
        "email": "matias.navarro@outlook.com",
        "disabled": False,
        "password": "123456"
    },
    'milagros': {
        "username": "milagros",
        "full_name": "Milagros",
        "email": "milagros.ponce@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'gael': {
        "username": "gael",
        "full_name": "Gael",
        "email": "gael.dominguez@hotmail.com",
        "disabled": False,
        "password": "123456"
    },
    'pilar': {
        "username": "pilar",
        "full_name": "Pilar",
        "email": "pilar.aguilar@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'ian': {
        "username": "ian",
        "full_name": "Ian",
        "email": "ian.cortes@yahoo.com",
        "disabled": False,
        "password": "123456"
    },
    'jazmin': {
        "username": "jazmin",
        "full_name": "Jazmín",
        "email": "jazmin.cabrera@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'felipe': {
        "username": "felipe",
        "full_name": "Felipe",
        "email": "felipe.leon@outlook.com",
        "disabled": False,
        "password": "123456"
    },
    'clara': {
        "username": "clara",
        "full_name": "Clara",
        "email": "clara.miranda@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    'simon': {
        "username": "simon",
        "full_name": "Simón",
        "email": "simon.bravo@hotmail.com",
        "disabled": True,
        "password": "123456"
    },
    'luna': {
        "username": "luna",
        "full_name": "Luna",
        "email": "luna.castillo@gmail.com",
        "disabled": True,
        "password": "123456"
    },
    'rodrigo': {
        "username": "rodrigo",
        "full_name": "Rodrigo",
        "email": "rodrigo.vera@yahoo.com",
        "disabled": False,
        "password": "123456"
    },
    'abril': {
        "username": "abril",
        "full_name": "Abril",
        "email": "abril.espinoza@gmail.com",
        "disabled": True,
        "password": "123456"
    }
}