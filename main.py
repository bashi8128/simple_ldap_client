#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Sun, 04 Oct 2020 04:19:08 +0900

"""Example module
"""
import gui
import tkinter as tk

def main():
    """ My function
    """
    # add your code here
    ldap_client = tk.Tk()
    ldap_client.geometry("800x400")
    ldap_client.title("LDAP Client")
    gui.MainFrame(ldap_client)
    ldap_client.mainloop()


if __name__ == "__main__":
    main()

