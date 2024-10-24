import redis
import pickle

r = redis.Redis(host="localhost", port=6379, db=0)


def store_in_redis(user_id: str, query_engine, rails, ttl=86400):
    """Store query_engine and rails in Redis with a TTL of 24 hours."""
    # Serialize the objects using pickle
    serialized_query_engine = pickle.dumps(query_engine)
    serialized_rails = pickle.dumps(rails)

    # Store them in Redis under the user_id
    r.set(f"{user_id}_query_engine", serialized_query_engine, ex=ttl)  # Set expiration time of 24 hours (86400 seconds)
    r.set(f"{user_id}_rails", serialized_rails, ex=ttl)


def get_from_redis(user_id: str):
    """Retrieve query_engine and rails from Redis for a specific user_id."""
    serialized_query_engine = r.get(f"{user_id}_query_engine")
    serialized_rails = r.get(f"{user_id}_rails")

    # If data is not available, return None
    if serialized_query_engine is None or serialized_rails is None:
        return None, None

    # Deserialize the data
    query_engine = pickle.loads(serialized_query_engine)
    rails = pickle.loads(serialized_rails)

    return query_engine, rails
