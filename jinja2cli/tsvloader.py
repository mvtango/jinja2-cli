import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def loads(tsvstring):
    try:
        memfile = StringIO(tsvstring)
        memfile.seek(0)
        reader = csv.DictReader(memfile, delimiter="\t")
        return { "data" : [ row for row in reader ] }
    except Exception as e:
        raise TSVError from e


class TSVError(Exception):
    pass
