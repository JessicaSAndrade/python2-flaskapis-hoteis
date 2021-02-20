from flask_restful import Resource, reqparse
from models.hotel import HotelModel


# Endpoint de listagem de todos os hoteis
class Hoteis(Resource):
    def get(self):
        return {"hoteis": [hotel.json() for hotel in HotelModel.query.all()]}

# Endpoints de criaçõa, edição, remoção e pesquisa de hoteis
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo nome é obrigatório e não pode ficar em branco")
    argumentos.add_argument('estrelas', type=float, required=True, help="O campo estrelas é obrigatório e não pode ficar em branco")
    argumentos.add_argument('diaria', type=float, required=True, help="O campo diária é obrigatório e não pode ficar em branco")
    argumentos.add_argument('cidade', type=str, required=True, help="O campo cidade é obrigatório e não pode ficar em branco")

        # Find by id
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return ("message: Hotel não encontrado!"), 404

    # Create Hotel
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' ja existe".format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
              return ("message: Erro interno no servidor, consulte o suporte!"), 500
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200

        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
              return ("message: Erro interno no servidor, consulte o suporte!"), 500
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return ("message: Erro interno no servidor, consulte o suporte!"), 500
            return ("message: Deletado com sucesso!"), 200
        return ("message: id não encontrado"), 404

        
