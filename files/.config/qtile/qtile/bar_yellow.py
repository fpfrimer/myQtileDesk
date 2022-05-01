from libqtile import  widget
from libqtile.bar import Bar
from libqtile.lazy import lazy
# from libqtile.currentlayout import CurrentLayout
# from libqtile.window_count import WindowCount
# from libqtile.windowname import WindowName
# from libqtile.cpu import CPU
# from libqtile.memory import Memory
# from libqtile.net import Net
# from libqtile.systray import Systray
# from libqtile.clock import Clock
# from libqtile.spacer import Spacer
# from libqtile.sep import Sep
# from libqtile.groupbox import GroupBox

from colors import gruvbox, pure

bar = Bar([ 
    widget.CurrentLayout(
        background=gruvbox['dark-yellow'],
    ),
    # widget.Sep(background=gruvbox['dark-yellow']),
    # widget.WindowCount(
    #     text_format='\ufab1{num}',
    #     background=gruvbox['dark-yellow'],
    #     show_zero=True,
    #     mouse_callbacks = {'Button1': lazy.spawn("rofi -show window")}
    # ),
    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['white'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['yellow'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['black'],
        padding=10,
        fontsize=18
    ),
    widget.Sep(foreground=pure['white']),
    widget.WindowName(foreground=gruvbox['dark-yellow']),    
    # widget.Sep(foreground=pure['white']),
    # widget.Image(
    #   filename="~/.config/qtile/icons/cpu.svg", 
    #   margin=4,
    #   mouse_callbacks = {'Button1': lazy.spawn("kitty -e htop")}
    # ),	
    # widget.CPU(
    #     format='{freq_current}GHz {load_percent}%',
    #     foreground=pure['blue'],
    #     mouse_callbacks = {'Button1': lazy.spawn("kitty -e htop")}
    # ),
    # widget.Sep(foreground=pure['white']),
    # ThermalZone(
    #     format='\ue780 {temp}\ufa03',
    #     background=gruvbox['dark-cyan']
    # ),
    # widget.Image(
    #   filename="~/.config/qtile/icons/ram.svg", 
    #   margin=4,
    #   mouse_callbacks = {'Button1': lazy.spawn("kitty -e htop")}
    # ),
    # widget.Memory(
    #     format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
    #     mouse_callbacks = {'Button1': lazy.spawn("kitty -e htop")},
    #     foreground=pure['green']
    # ),
    # widget.Sep(foreground=pure['white']),
    widget.Systray(
        padding=10,
        icon_size=23,
        background=gruvbox['black']
    ),
    widget.Spacer(10),
    widget.Clock(
        background=gruvbox['black'],
        foreground=gruvbox['white'],
        format='%Y-%m-%d %a %H:%M',
        mouse_callbacks = {'Button1': lazy.spawn("gsimplecal")}
    ),
    # widget.Sep(background=gruvbox['dark-yellow']),
    # widget.TextBox(
    #     background=gruvbox['dark-yellow'],
    #     fmt="\u23fb",
    #     mouse_callbacks = {'Button1': lazy.spawn("power-menu")}
    # )         
],
    26,
    background="#000000",
    opacity=0.8,
    margin=[0, 0, 0, 0],
    border_width=[0, 0, 0, 0],  # Draw top and bottom borders
    border_color=gruvbox['dark-yellow']  # Borders are blue
)
