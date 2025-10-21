from flask import jsonify, request
from flask.views import MethodView
import files

class Sellings(MethodView):
    def get(self):
        sellings = []
        sellings = files.open_json("sellings.json")

        return jsonify({"response":sellings}), 200


    def post(self):
        try:
            sellings = []
            sellings = files.open_json("sellings.json")
            data = request.json

            sellings.append(data)

            files.create_json(sellings, "products.json")

            return jsonify({"response":sellings}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def put(self, selling_id):
        try:
            sellings = []
            sellings = files.open_json("sellings.json")
            data = request.json
            counter = 0

            if sellings == []:
                return jsonify({"error":"No sellings has been made yet."}), 400
            for value in sellings:
                if selling_id == value["id"]:
                    if not "id" in data:
                        data["id"] = selling_id
                        sellings[counter] = data
                        files.create_json(sellings, "sellings.json")
                        return sellings, 200
                    else:
                        return jsonify({"error":"Do not include the id in the body when updating a selling."}), 400
                elif counter+1 == len(sellings):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def delete(self, selling_id):
        try:
            sellings = []
            sellings = files.open_json("sellings.json")
            counter = 0
            
            if sellings == []:
                return jsonify({"error":"No sellings has been created yet."}), 400
            for value in sellings:
                if selling_id == value["id"]:
                    del sellings[counter]
                    files.create_json(sellings, "sellings.json")
                    return "", 204
                elif counter+1 == len(sellings):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


sellings_view = Sellings.as_view("sellings_api")