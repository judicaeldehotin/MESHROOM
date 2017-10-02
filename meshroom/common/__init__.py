Model = None
Slot = None
Signal = None
Property = None
BaseObject = None

if 1:  # TODO: switch types according to something
    # PySide types
    from .qt import Model, Slot, Signal, Property, BaseObject
else:
    # Core types
    from .core import Model, Slot, Signal, Property, BaseObject


class _BaseModel:
    """ Common API for model implementation """

    def __init__(self, keyAttrName="name", **kwargs):
        """
        :param keyAttrName: name of the attribute containing the unique key for an object
        """
        pass

    @property
    def objects(self):
        """ Return a dictionary with {unique_key: object} mapping"""
        return None

    def get(self, key):
        """ Get the object with the unique key 'key' """
        pass

    def add(self, obj):
        """ Add given object using its 'keyAttrName' as unique key """
        pass

    def pop(self, key):
        """ Remove 'item' with unique key 'key' from the model """
        pass

    def remove(self, obj):
        """ Remove 'obj' from the model """
        pass

    def clear(self):
        """ Remove all internal objects """
        pass