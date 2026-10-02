
# Imports 

import re
from collections import defaultdict
import json

# Feature_Weighted_Similarity

def similarity(a,b):
    a_tokens = re.findall(r'\w+', a.upper())
    b_tokens = re.findall(r'\w+', b.upper())

    score = 0
    for token in a_tokens:
        if token in b_tokens:
            if token in ["ROWNUM","SYSDATE","PROCEDURE"]:
                score += 2
            else:
                score += 1

    return score / (len(set(a_tokens)) + 1)

# Knowledge_Base


with open("dataset.json","r") as f:
    knowledge_base = json.load(f)

# Feature_Aware_Top-k_Retrieval

def get_features(sql):
    features = []
    if "ROWNUM" in sql or "SYSDATE" in sql:
        features.append("DIALECT_DIFF")
    if "JOIN" in sql:
        features.append("JOIN")
    if "SELECT" in sql:
        features.append("CORE_SQL")
    return features

def find_top_k(query, k=5):
    query_features = get_features(query)

    filtered = [
        item for item in knowledge_base
        if any(f in item["features"] for f in query_features)
    ]

    scores = [(similarity(query, item["oracle"]), item) for item in filtered]
    scores.sort(reverse=True, key=lambda x: x[0])

    return [(s,item) for s,item in scores[:k] if s > 0.2]

# Weighted_Voting

def weighted_vote(matches):
    score_map = defaultdict(float)

    for score,item in matches:
        score_map[item["postgres"]] += score

    return max(score_map, key=score_map.get)

# Conversion_Engine

def convert(sql):
    matches = find_top_k(sql, k=5)

    if matches:
        confidence = max([m[0] for m in matches])

        if confidence > 0.25:
            result = weighted_vote(matches)
            return result, round(confidence,2)

    # fallback rules
    sql = sql.replace("SYSDATE","CURRENT_DATE")
    sql = sql.replace("FROM dual","")

    sql = re.sub(r"ROWNUM\s*<=\s*(\d+)", r"LIMIT \1", sql)
    sql = re.sub(r"ROWNUM\s*=\s*(\d+)", r"LIMIT \1", sql)

    sql = sql.replace("SYSTIMESTAMP","CURRENT_TIMESTAMP")
    sql = sql.replace("NVL","COALESCE")

    if "PROCEDURE" in sql:
        return "CREATE FUNCTION converted() RETURNS void AS $$ BEGIN NULL; END; $$ LANGUAGE plpgsql;", 0.5

    if "BEGIN" in sql:
        return "DO $$ " + sql + " $$;", 0.5

    return sql.strip(), 0.3

