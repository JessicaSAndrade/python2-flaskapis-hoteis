from sql_alchemy import banco

class HotelModel(banco.Model):

# Espelho do banco de dados
    __tablename__ = 'hoteis'
    hotel_id = banco.Column(banco.String(80), primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

# Método padrão de inicialização da minha classe objeto
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }


    @classmethod
    # pesquisar por hotel_id
    def find_hotel(cls, hotel_id):
        #SELECT * FROM HOTEL WHERE HOTEL_ID = HOTEL_ID
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    # Cria um  hotel
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    # Edita um hotel
    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()