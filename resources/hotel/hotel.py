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
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return ("message: Hotel não encontrado!"), 404

    # Create Hotel
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_object = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_object.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_object = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_object.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        exist_hotel = Hotel.find_hotel(hotel_id)
        if exist_hotel:
            hoteis.remove(exist_hotel)
            return ("message: Deletado com sucesso!"), 200
        return ("message: id não encontrado"), 404
        