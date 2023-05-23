from tkinter import *
from tkinter import ttk


class TkinterService:
    def __init__(self, title: str, width: int, height: int):
        self._tk = self._create_tk(title, width, height)

    def run_loop(self) -> None:
        self._tk.mainloop()

    def quit(self) -> None:
        self._tk.quit()

    def create_frame(self) -> ttk.Frame:
        return ttk.Frame(self._tk)

    def create_canvas(self, bg: str = 'white') -> Canvas:
        return Canvas(self._tk, bg=bg)

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
