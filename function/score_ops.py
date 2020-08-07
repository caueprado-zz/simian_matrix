from function.db_config import score_col

pipe = [{'$group': {
              "_id": "$specie",
              'count': {'$sum': 1}
          }}]

pipe2 = [{
      '$count': "species"
    }]


def group_species():
    result = score_col.aggregate(pipe)
    results = []
    for doc in result:
        results.append(doc)
    return results


def count():
    count = score_col.aggregate(pipe2)
    for doc in count:
        return doc


def get_score():
    species = group_species()
    for i in [0, 1]:
        print(species[i]['_id'])
        if species[i]['_id'] == 'Simian':
            count_mutant_dna = species[i]['count']
        else:
            count_human_dna = species[i]['count']
    return {"count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": count_mutant_dna/count_human_dna
            }
