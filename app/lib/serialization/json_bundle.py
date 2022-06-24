import json
from inspect import ismethod, isfunction
from typing import Collection, TypeVar, Generic


def get_class_annotations(class_object):
    temp = class_object

    while temp.__bases__:
        for key in vars(temp):
            if not key.startswith('__'):
                yield key, getattr(temp, key)

        if hasattr(class_object, '__annotations__'):
            for key, bundle in class_object.__annotations__.items():
                yield key, bundle

        if JsonBundle in temp.__bases__:
            return

        temp = temp.__class__


def get_field_generator(object_of_class: object):
    for key in vars(object_of_class):
        yield key, getattr(object_of_class, key)

    for key, bundle in get_class_annotations(object_of_class.__class__):
        yield key, bundle


T = TypeVar('T')


class JsonBundle(Generic[T]):

    @classmethod
    def to_dict_class(cls, data_object: T):
        pass

    def to_dict(self, data_object: T):
        result = dict()

        for key, bundle in get_field_generator(self):

            if ismethod(bundle) or isfunction(bundle):
                result[key] = bundle(data_object)
            elif isinstance(bundle, str | int | bool | None):
                result[key] = getattr(data_object, key)
            elif bundle is str or bundle is int or bundle is bool:
                result[key] = getattr(data_object, key)
            elif isinstance(bundle, JsonBundle):
                data = getattr(data_object, key)
                result[key] = bundle.to_dict(data)

        return result

    def to_json(self, data_object: T, **json_props):
        return json.dumps(self.to_dict(data_object), **json_props)

    def to_json_array(self, data_object_list: Collection[T], **json_props):
        result = list()

        for item in data_object_list:
            result.append(self.to_dict(item))

        return json.dumps(result, **json_props)
