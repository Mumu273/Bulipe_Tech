from enum import Enum


class BaseEnum(Enum):
    """
     Let's allow using an Enum class in model Field choices and make code more simple and modular.
     Ref: https://code.djangoproject.com/ticket/27910
     Ref: https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
    """

    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError(
                "aliases not allowed in DuplicateFreeEnum:  %r --> %r" % (a, e))

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def specific_choices(cls, excluded_values):
        return [(key.value, key.name) for key in cls if key.value not in excluded_values]

    @classmethod
    def values(cls):
        return [key.value for key in cls]

    @classmethod
    def keys(cls):
        return [key.name for key in cls]

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def get_key(cls, value):
        return [key.name for key in cls if key.value == value]

    @classmethod
    def validate(cls, items):
        available_item = []
        current_item = ''
        try:
            for item in items:
                current_item = item
                if cls.has_value(item):
                    available_item.append(item)
                else:
                    raise Exception
            return available_item
        except Exception as e:
            raise ValueError("Invalid choice:  %r for  %r" %
                             (current_item, cls))

    @classmethod
    def make_json_compatible(cls):
        return [{key.name.lower(): key.value} for key in cls]

    @classmethod
    def exclude_values(cls, items):
        return [key.value for key in cls if key.value not in items]

    @classmethod
    def get_key_name(cls, value):
        for key in cls:
            if key.value == value:
                return key.name

    @classmethod
    def jsonify(cls):
        enum_dict = dict()
        for key in cls:
            source_name = key.name.split('_')
            full_source_name = ''
            if len(source_name) < 2:
                full_source_name = source_name[0].capitalize()
            elif len(source_name) > 1:
                for portion in source_name:
                    if full_source_name != '':
                        full_source_name += " "
                    full_source_name += portion.capitalize()
            enum_dict[key.value] = full_source_name
        return enum_dict

class CountryCodeEnum(BaseEnum):
    AU = 'au'
    BD = 'bd'
    CA = 'ca'
    CN = 'cn'
