from flask import Flask, request
from function.db_config import score_col
from function import score_ops, identify

app = Flask(__name__)


@app.route("/stats")
def stats():
    return score_ops.get_score()


@app.route("/health")
def health():
    return "OK Health"


@app.route("/simian", methods=['POST'])
def simian():
    payload = request.data
    if identify.verify(payload):
        species = "Simian"
    else:
        species = "Human"
    response = {
     "dna": request.get_json()['dna'],
     "specie": species
     }
    score_col.insert_one(response)
    return "OK"


if __name__ == "__main__":
    app.run()
