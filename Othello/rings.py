

import tkinter


class RingsApplication:
    def __init__(self, rings: [(float, float, float, float)]):
        self._rings = rings
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 400,
            background = 'pink')



        self._canvas.grid(
            row = 0, column = 0, padx = 30, pady = 30,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()



    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_rings()


    def _draw_rings(self) -> None:
      
        self._canvas.delete(tkinter.ALL)

        for frac_x1, frac_y1, frac_x2, frac_y2 in self._rings:
            self._draw_ring(frac_x1, frac_y1, frac_x2, frac_y2)


    def _draw_ring(self, frac_x1: float, frac_y1: float, frac_x2: float, frac_y2: float) -> None:
  
        canvas_width = self._canvas.winfo_width()
        print(self._canvas.winfo_width())
        canvas_height = self._canvas.winfo_height()
        print(self._canvas.winfo_height())
        # Now we can do the multiplication and draw the oval.
        self._canvas.create_oval(
            canvas_width * frac_x1, canvas_height * frac_y1,
            canvas_width * frac_x2, canvas_height * frac_y2,
            outline = 'black')



if __name__ == '__main__':
    rings = [
        (.05, .05, .32, .32), (.37, .05, .64, .32), (.69, .05, .96, .32),
        (.19, .19, .46, .46), (.51, .19, .78, .46)
    ]

    app = RingsApplication(rings)
    app.start()
