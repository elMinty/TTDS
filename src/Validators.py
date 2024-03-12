
trackDetailsValidator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': [
            'track_id', 'album_id', 'track_name', 'artist_name', 'track_link',
            'added_on', 'release_date', 'duration_ms', 'explicit',
            'danceability', 'energy', 'genres'
        ],
        'properties': {
            'track_id': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'album_id': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'track_name': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'artist_name': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'track_link': {
                'bsonType': 'object',
                'required': ['spotify'],
                'properties': {
                    'spotify': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    }
                }
            },
            'added_on': {
                'bsonType': 'string',
                'description': 'must be a string in a date-time format and is required'
            },
            'release_date': {
                'bsonType': 'string',
                'description': 'must be a string in a date format and is required'
            },
            'duration_ms': {
                'bsonType': 'int',
                'description': 'must be an integer and is required'
            },
            'explicit': {
                'bsonType': 'bool',
                'description': 'must be a boolean and is required'
            },
            'danceability': {
                'bsonType': 'double',
                'description': 'must be a double and is required'
            },
            'energy': {
                'bsonType': 'double',
                'description': 'must be a double and is required'
            },
            'genres': {
                'bsonType': 'array',
                'description': 'must be an array of strings and is required',
                'items': {
                    'bsonType': 'string'
                }
            }
        }
    }
}

updateTracksValidator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': [
            'added_on', 'album_id', 'album_cover', 'album_name', 'artist_name',
            'release_date', 'track_id', 'track_name', 'track_link', 'duration_ms',
            'explicit', 'danceability', 'energy', 'genres', 'lyrics'
        ],
        'properties': {
            'added_on': {
                'bsonType': 'string',
                'description': 'must be a string in a date-time format and is required'
            },
            'album_id': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'album_cover': {
                'bsonType': 'array',
                'description': 'must be an array of objects and is required',
                'items': {
                    'bsonType': 'object',
                    'required': ['height', 'url', 'width'],
                    'properties': {
                        'height': {
                            'bsonType': 'int',
                            'description': 'must be an integer and is required'
                        },
                        'url': {
                            'bsonType': 'string',
                            'description': 'must be a string and is required'
                        },
                        'width': {
                            'bsonType': 'int',
                            'description': 'must be an integer and is required'
                        }
                    }
                }
            },
            'album_name': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'artist_name': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'release_date': {
                'bsonType': 'string',
                'description': 'must be a string in a date format and is required'
            },
            'track_id': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'track_name': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'track_link': {
                'bsonType': 'object',
                'required': ['spotify'],
                'properties': {
                    'spotify': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    }
                }
            },
            'duration_ms': {
                'bsonType': 'int',
                'description': 'must be an integer and is required'
            },
            'explicit': {
                'bsonType': 'bool',
                'description': 'must be a boolean and is required'
            },
            'danceability': {
                'bsonType': 'double',
                'description': 'must be a double and is required'
            },
            'energy': {
                'bsonType': 'double',
                'description': 'must be a double and is required'
            },
            'genres': {
                'bsonType': 'array',
                'description': 'must be an array of strings and is required',
                'items': {
                    'bsonType': 'string'
                }
            },
            'lyrics': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            }
        }
    }
}

album_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['album_id', 'album_cover', 'album_name'],
        'properties': {
            'album_id': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'album_cover': {
                'bsonType': 'object',
                'required': ['height', 'url', 'width'],
                'properties': {
                    'height': {
                        'bsonType': 'int',
                        'description': 'must be an integer and is required'
                    },
                    'url': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'width': {
                        'bsonType': 'int',
                        'description': 'must be an integer and is required'
                    }
                },
                'description': 'must be an object with height, url, and width and is required'
            },
            'album_name': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            }
        }
    }
}

TrackLyricsValidator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['track_id', 'lyrics'],
        'properties': {
            'track_id': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'lyrics': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            }
        }
    }
}


lyric_indexer_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['lyric', 'tracks'],
        'properties': {
            'lyric': {
                'bsonType': 'string',
                'description': 'must be a string and is required'
            },
            'tracks': {
                'bsonType': 'array',
                'description': 'must be an array of objects with trackId and positions and is required',
                'items': {
                    'bsonType': 'object',
                    'required': ['trackId', 'positions'],
                    'properties': {
                        'trackId': {
                            'bsonType': 'string',
                            'description': 'must be a string and is required'
                        },
                        'positions': {
                            'bsonType': 'array',
                            'description': 'must be an array of integers and is required',
                            'items': {
                                'bsonType': 'int'
                            }
                        }
                    }
                }
            }
        }
    }
}


