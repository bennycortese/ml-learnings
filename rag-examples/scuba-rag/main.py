

def embedding_generation(text):
    return text # Text as a vector embedding

def upload_to_database(embedding):
    # upload the embedding to any database, abstract away into another class potentially and make this take a functor of that class
    return "Success"

def retrieve_embedding_from_database(new_embedding, k):
    # query the database with the new embedding, grabbing k other documents with the most similar embedding
    return [] # the k embedding list


