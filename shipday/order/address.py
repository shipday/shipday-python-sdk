from collections import defaultdict

from shipday.utils.verifiers import verify_none_or_instance_of


class Address:
    def __init__(self, *args, unit: str = None, street: str = None, city: str = None,
                 state: str = None, zip: str = None, country: str = None,
                 **kwargs):
        kwargs = defaultdict(lambda: None, **kwargs)
        self._unit = unit
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip
        self._country = country

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    def __repr__(self):
        return self.get_single_line()

    def verify(self):
        verify_none_or_instance_of(str, self.unit, "Unit must be a str")
        verify_none_or_instance_of(str, self.street, "Street must be str")
        verify_none_or_instance_of(str, self.city, "City must be str")
        verify_none_or_instance_of(str, self.state, "State must be str")
        verify_none_or_instance_of(str, self.zip, "Zip must be str")
        verify_none_or_instance_of(str, self.country, "Country must be str")

    def get_breakdown(self) -> dict:
        obj = dict()
        if self.unit is not None:
            obj['unit'] = self.unit
        if self.street is not None:
            obj['street'] = self.street
        if self.city is not None:
            obj['city'] = self.city
        if self.state is not None:
            obj['state'] = self.state
        if self.zip is not None:
            obj['zip'] = self.zip
        if self.country is not None:
            obj['country'] = self.country
        return obj

    def get_single_line(self) -> str:
        l = []
        if self.street is not None:
            l.append(self.street)
        if self.city is not None:
            l.append(self.city)
        if self.state is not None:
            l.append(self.state)
        if self.zip is not None:
            l.append(self.zip)
        if self.country is not None:
            l.append(self.country)
        return ', '.join(l)
