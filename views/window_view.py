from services.tkinter_service import TkinterService
from views.base_view import BaseView


class WindowView(BaseView):
    def __init__(self, tkinter_service: TkinterService):
        super().__init__()
        self._tkinter_service = tkinter_service

    def run_loop(self) -> None:
        self._tkinter_service.run_loop()
