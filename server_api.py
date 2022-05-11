from flask import Flask
from flask_restx import Api, Resource

import db_module, server_S3

app = Flask(__name__)
api = Api(app)

@api.route('/cafes')
class SELECT_FROM_CAFES(Resource):
    def get(self):
        sql = "SELECT * FROM usr.cafes;"
        row = db_module.get_cafe_list(sql)
 
        for i in range(len(row)):
            row[i]['background'] = server_S3.create_presigned_url("hyeonrista/cafe" + str(i + 1) + ".jpeg")

        return {"cafe_list" : row}

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)