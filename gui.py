#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Sun, 04 Oct 2020 04:27:42 +0900

"""Example module
"""
import tkinter as tk
from tkinter import ttk
import ldapsearch
#import outputframe


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(sticky=tk.W + tk.E)
        self.create_widgets()

    def create_widgets(self):
        # Variable
        self.proto = tk.StringVar(value="")
        self.server = tk.StringVar(value="")
        self.base = tk.StringVar(value="")
        self.scope = tk.StringVar(value="")
        self.filterstr = tk.StringVar(value="")

        # Define widget for protocol type
        self.proto_list = ["ldap",
                           "ldaps",
                           "ldapi"]
        self.lab_uri = ttk.Label(self, text='uri')
        self.comb_proto = ttk.Combobox(self,
                                       values=self.proto_list,
                                       width=5)
        self.comb_proto.configure(textvariable=self.proto)

        # Define widget for server name
        self.box_serv = ttk.Entry(self)
        self.box_serv.configure(textvariable=self.server)

        # Define widget for search base
        self.lab_base = ttk.Label(self, text='Search base')
        self.box_base = ttk.Entry(self, width=28)
        self.box_base.configure(textvariable=self.base)

        # Define widget for scope type
        self.scope_list = ["BASE",
                           "ONELEVEL",
                           "SUBTREE",
                           "SUBORDINATE"]
        self.lab_scope = ttk.Label(self, text='Search scope')
        self.comb_scope = ttk.Combobox(self,
                                       values=self.scope_list,
                                       width=8)
        self.comb_scope.configure(textvariable=self.scope)

        # Define widget for search filter
        self.lab_filterstr = ttk.Label(self, text='Search filter')
        self.box_filterstr = ttk.Entry(self, width=28)
        self.box_filterstr.configure(textvariable=self.filterstr)

        # Define button for execute LDAP SRCH
        self.btn_exec = ttk.Button(self)
        self.btn_exec.configure(text="Search", command=self.exec_search)

        # Define widget for output
        self.tree_dit = ttk.Treeview(self)

        # Align widgets and a button
        self.lab_uri.grid(column=0, row=0, sticky=tk.E)
        self.comb_proto.grid(column=1, row=0, sticky=tk.E + tk.W)
        self.box_serv.grid(column=2, row=0, sticky=tk.E + tk.W)
        self.lab_base.grid(column=0, row=1, sticky=tk.E)
        self.box_base.grid(column=1, row=1, columnspan=2)
        self.lab_scope.grid(column=0, row=2, sticky=tk.E)
        self.comb_scope.grid(column=1, row=2, columnspan=2, sticky=tk.W)
        self.lab_filterstr.grid(column=0, row=3, sticky=tk.E)
        self.box_filterstr.grid(column=1, row=3, columnspan=2)
        self.btn_exec.grid(column=2, row=4)
        self.tree_dit.grid(column=0, row=5, columnspan=3,
                           sticky=tk.W + tk.E)

    def exec_search(self):
        #self.tree_dit.destroy()
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

        if filterstr != "":
            self.ld_res = ldapsearch.ldapsearch(uri, base, scope, filterstr)
        else:
            self.ld_res = ldapsearch.ldapsearch(uri, base, scope, filterstr=None)

        for entry in self.ld_res:
            if self.tree_dit.exists('hoge'):
                self.tree_dit.insert(parent='hoge',
                                     index=0,
                                     iid=entry[0],
                                     text=entry[1]['uid'][0].decode())
            else:
                self.tree_dit.insert(parent='',
                                     index=0,
                                     iid=entry[0],
                                     text=entry[1]['uid'][0].decode())

        self.tree_dit.grid(column=0, row=5, columnspan=3)


if __name__ == "__main__":
    pass
