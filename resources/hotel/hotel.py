from flask_restful import Resource, reqparse
from models.hotel import HotelModel


hoteis = [
    {"hotel_id": "copacabana", "nome": "Copacabana Palace", 
    "estrelas": 5, "diaria":1000, "cidade": "Rio de Janeio"},

    {"hotel_id": "gravata", "nome": "Hotel Gravatá",
    "estrelas": 3.8, "diaria": 400, "cidade": "Gravatá"},

    {"hotel_id": "noronha", "nome": "Hotel de Noronha",
    "estrelas": 4.5, "diaria": 300.25, "cidade": "Noronha"}
]

# Endpoint de listagem de todos os hoteis
class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}

# Endpoints de criaçõa, edição, remoção e pesquisa de hoteis
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

    # Find by id
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return ("message: Hotel não encontrado!"), 404

    # Create Hotel
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"messase": "O Hotel_id '{}' já existe, insira outro".format(hotel_id)}, 400
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, hotel_id):
        exist_hotel = Hotel.find_hotel(hotel_id)
        if exist_hotel:
            hoteis.remove(exist_hotel)
            return ("message: Deletado com sucesso!"), 200
        return ("message: id não encontrado"), 404
        