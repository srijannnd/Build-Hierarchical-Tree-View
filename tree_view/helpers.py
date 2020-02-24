from tree_view.db import database


# Recursive function to create nested json
def assign_children(relations, skill_map, skill, keywords, index=0):
    if index < len(skill_map):
        if "name" not in relations:
            relations["name"] = skill_map[index]["_id"]
            keywords.append(skill_map[index]["_id"])
        if "children" in relations and index+1 < len(skill_map):
            child_query = list(filter(lambda x: x["name"] == skill_map[index+1]["_id"], relations["children"]))
            if len(child_query):
                obj = child_query[0]
            else:
                relations["children"].append({})
                obj = relations["children"][-1]
        elif "children" in relations:
            relations["children"].append({})
            obj = relations["children"][-1]
        else:
            relations["children"] = [{}]

            obj = relations["children"][-1]
        assign_children(obj, skill_map, skill, keywords, index+1)
    else:
        relations["name"] = skill


def get_nested_structure(result, skill, relations, keywords):
    result["skillMap"].sort(key=lambda x: x["depth"], reverse=True)
    assign_children(relations, result["skillMap"], skill, keywords)
    return relations


def generate_tree(skills):
    results = list(database["capabilities"].aggregate([
        {"$match": {"_id": {"$in": skills}}},
        {
          "$graphLookup": {
             "from": "capabilities",
             "startWith": "$parent",
             "connectFromField": "parent",
             "connectToField": "_id",
             "as": "skillMap",
             "depthField": "depth"
          }
       }
    ]))
    keywords = []
    nested_results = {}
    for result in results:
        skill = result["_id"]
        if skill not in keywords:
            get_nested_structure(result, skill, nested_results, keywords)
    return nested_results
