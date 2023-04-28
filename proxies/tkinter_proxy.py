from tkinter import *

from proxies.canvas_proxy import CanvasProxy
from proxies.menu_proxy import MenuProxy


class TkinterProxy:
    def __init__(self, title: str, width: int, height: int):
        self._tk = self._create_tk(title, width, height)

    def create_canvas(self) -> CanvasProxy:
        return CanvasProxy(self._tk)

    def create_menu(self) -> MenuProxy:
        return MenuProxy(self._tk)

    def run_loop(self) -> None:
        self._tk.mainloop()

    @staticmethod
    def _create_tk(title: str, width: int, height: int) -> Tk:
        tk = Tk()
        tk.title(title)
        tk.resizable(False, False)

        screen_width = tk.winfo_screenwidth()
        screen_height = tk.winfo_screenheight()
        window_x = int(screen_width // 2 - width // 2)
        window_y = int(screen_height // 2 - height // 2)
        tk.geometry('{}x{}+{}+{}'.format(width, height, window_x, window_y))

        return tk
