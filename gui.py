#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Wed, 30 Sep 2020 16:15:13 +0900

"""Example module
"""
import tkinter as tk
from tkinter import ttk
import ldapsearch


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.master.geometry("600x200")
        self.master.title("LDAP Client")
        self.create_widgets()

    def create_widgets(self):
        # Variable
        self.proto = tk.StringVar()
        self.server = tk.StringVar()
        self.base = tk.StringVar()
        self.scope = tk.StringVar()
        self.filterstr = tk.StringVar()

        # Define widget for protocol type
        self.proto_list = ["ldap",
                           "ldaps",
                           "ldapi"]
        self.lab_uri = ttk.Label(self, text='uri')
        self.comb_proto = ttk.Combobox(self, values=self.proto_list)
        self.comb_proto.configure(textvariable=self.proto)

        # Define widget for server name
        self.box_serv = ttk.Entry(self)
        self.box_serv.configure(textvariable=self.server)

        # Define widget for search base
        self.lab_base = ttk.Label(self, text='Search base')
        self.box_base = ttk.Entry(self)
        self.box_base.configure(textvariable=self.base)

        # Define widget for scope type
        self.scope_list = ["BASE",
                           "ONELEVEL",
                           "SUBTREE",
                           "SUBORDINATE"]
        self.lab_scope = ttk.Label(self, text='Search scope')
        self.comb_scope = ttk.Combobox(self, values=self.scope_list)
        self.comb_scope.configure(textvariable=self.scope)

        # Define widget for search filter
        self.lab_filterstr = ttk.Label(self, text='Search filter')
        self.box_filterstr = ttk.Entry(self)
        self.box_filterstr.configure(textvariable=self.filterstr)

        # Define button for execute LDAP SRCH
        self.btn_exec = ttk.Button(self)
        self.btn_exec.configure(text="Search", command=self.exec_search)

        # Align widgets and a button
        self.lab_uri.grid(column=0, row=0, sticky=tk.E)
        self.comb_proto.grid(column=1, row=0)
        self.box_serv.grid(column=2, row=0)
        self.lab_base.grid(column=0, row=1, sticky=tk.E)
        self.box_base.grid(column=1, row=1)
        self.lab_scope.grid(column=0, row=2, sticky=tk.E)
        self.comb_scope.grid(column=1, row=2)
        self.lab_filterstr.grid(column=0, row=3, sticky=tk.E)
        self.box_filterstr.grid(column=1, row=3)
        self.btn_exec.grid(column=2, row=4)

    def exec_search(self):
        proto = self.proto.get()
        server = self.server.get()
        base = self.base.get()
        scope = self.scope.get()
        filterstr = self.filterstr.get()

        uri = proto + '://' + server

        if scope == 'SCOPE_BASE':
            scope = 0
        elif scope == 'ONELEVEL':
            scope = 1
        elif scope == 'SUBTREE':
            scope = 2
        elif scope == 'SUBORDINATE':
            scope = 3
        else:
            raise ValueError

        self.ld_res = ldapsearch.ldapsearch(uri, base, scope, filterstr)
        print(self.ld_res)


def main():
    """ My function
    """
    myApp = tk.Tk()
    app = App(master=myApp)
    app.mainloop()


if __name__ == "__main__":
    main()
