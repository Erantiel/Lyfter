from sqlalchemy.inspection import inspect

def to_dict(self):
    return {
        column.key: getattr(self, column.key)
        for column in inspect(self).mapper.column_attrs
    }