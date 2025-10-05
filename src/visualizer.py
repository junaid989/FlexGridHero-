# src/visualizer.py

class Visualizer:
    def __init__(self):
        self.layouts = {
            1: "[Flexbox Container]\n[Item1][Item2][Item3]",
            2: "[Grid Container]\n[Item1][Item2]\n[Item3][Item4]",
            3: "[Nested Flexbox]\n[Parent][Child1][Child2]"
        }

    def show_preview(self, level, ui=None):
        """
        Display a preview layout.
        If `ui` is provided, uses ui.print_info, else prints normally.
        """
        layout = self.layouts.get(level, "[Unknown Layout]")
        if ui:
            ui.print_info(f"Layout Preview:\n{layout}")
        else:
            print(f"Layout Preview:\n{layout}")

    def build(self, level, ui=None):
        """
        Simulate building the layout (ASCII animation style).
        """
        layout = self.layouts.get(level, "[Unknown Layout]")
        if ui:
            ui.print_info("Building Layout...")
            for i in range(1, 4):
                ui.print_info("." * i)
        else:
            print("Building Layout...")
            for i in range(1, 4):
                print("." * i)
        if ui:
            ui.print_info(f"{layout}\n")
        else:
            print(f"{layout}\n")
