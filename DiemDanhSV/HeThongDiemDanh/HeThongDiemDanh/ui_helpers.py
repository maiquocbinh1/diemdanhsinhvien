from __future__ import annotations

from dataclasses import dataclass
from tkinter import Tk, Misc
from tkinter import ttk


@dataclass(frozen=True)
class UIScale:
    win_w: int
    win_h: int
    sx: float
    sy: float

    def x(self, v: int) -> int:
        return int(v * self.sx)

    def y(self, v: int) -> int:
        return int(v * self.sy)

    def w(self, v: int) -> int:
        return max(1, int(v * self.sx))

    def h(self, v: int) -> int:
        return max(1, int(v * self.sy))


def init_window(root: Tk, *, title: str, base_w: int = 1530, base_h: int = 790, min_h: int = 650) -> UIScale:
    """
    Keeps legacy absolute layouts usable on different resolutions / DPI scaling
    by computing a scale factor and applying it consistently.
    """
    root.title(title)
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    win_w = min(base_w, screen_w)
    # leave room for taskbar/title bar; avoid too small height
    win_h = min(base_h, max(min_h, screen_h - 60))
    root.geometry(f"{win_w}x{win_h}+0+0")

    sx = win_w / base_w if base_w else 1.0
    sy = win_h / base_h if base_h else 1.0
    return UIScale(win_w=win_w, win_h=win_h, sx=sx, sy=sy)


def apply_ttk_style(root: Misc) -> None:
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure("App.TButton", font=("times new roman", 12, "bold"))
    style.configure("App.TEntry", font=("times new roman", 12, "bold"))
    style.configure("App.TCombobox", font=("times new roman", 12, "bold"))


def sp(scale: UIScale, widget: Misc, *, x: int, y: int, width: int | None = None, height: int | None = None, **kw):
    """Scaled place() helper."""
    opts = {"x": scale.x(x), "y": scale.y(y)}
    if width is not None:
        opts["width"] = scale.w(width)
    if height is not None:
        opts["height"] = scale.h(height)
    opts.update(kw)
    widget.place(**opts)


def center_title(scale: UIScale, *, desired_width: int = 980, min_margin: int = 260) -> tuple[int, int]:
    w = min(desired_width, max(200, scale.win_w - min_margin))
    x = max(0, (scale.win_w - w) // 2)
    return x, w

