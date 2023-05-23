class BaseShape:
    def __init__(self, _type: str, _id: int | None = None):
        self._type = _type
        self._id = _id

    def get_type(self) -> str:
        return self._type

    def set_type(self, _type) -> None:
        self._type = _type

    def get_id(self) -> int | None:
        return self._id

    def set_id(self, _id: int | None) -> None:
        self._id = _id
