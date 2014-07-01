MONGO_HOST = 'localhost'
MONGO_DBNAME = 'todo'

RESOURCE_METHODS = ['GET', 'DELETE', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

todos = {
    'schema': {
        'text': {
            'type': 'string',
            'required': True,
        },
        'done': {
            'type': 'boolean',
            'required': True,
        },
    },
}

DOMAIN = {
    'todos': todos,
}

# Disable etags. Will make accidental overwriting possible, but makes the
# Angular JS code a lot easier.
IF_MATCH = False

# Makes requests return submitted/changed object
BANDWIDTH_SAVER = False

X_DOMAINS = '*'
X_HEADERS = ['Accept']
