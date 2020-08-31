import PySimpleGUI as sg

"""
    Oh yes, the classic "Hello World".  The problem is that you
    can do it so many ways using PySimpleGUI
"""

sg.PopupNoButtons('Hello World')         # the single line

sg.Window('Hello world', [[sg.Text('Hello World')]]).Read()    # single line using a real window

# This is a "Traditional" PySimpleGUI window code. First make a layout, then a window, the read it
layout = [[sg.Text('Hello World')]]
window = sg.Window('Hello world', layout)
event, values = window.Read()
