from proxies.tkinter_proxy import TkinterProxy
from views.base_view import BaseView


class WindowView(BaseView):
    def __init__(self, tkinter: TkinterProxy):
        super().__init__()
        self._tkinter = tkinter

    def run_loop(self) -> None:
        self._tkinter.run_loop()
