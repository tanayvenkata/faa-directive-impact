"""Model calls for evaluation runs: one request, one structured response.

Every call is recorded with its request, response, tokens, and cost so a run
can be re-scored without calling the model, and tests can replay it offline.
"""
