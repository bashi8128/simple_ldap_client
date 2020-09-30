#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Wed, 30 Sep 2020 16:28:11 +0900

"""Example module
"""
import base64
import ldap


def ldapsearch(server, base, scope, filterstr):
    """ 
    Execute LDAP SRCH operation

    Parameters
    ----------
    server : string
        LDAP URI which begins protocol name like "ldap://"
    base : string
        LDAP search base
    scope : int
        Scope to apply in the search
        Scope should be 0(base), 1(onelevel), 2(subtree) or 3(subordinate)
    filterstr : string
        Filter to apply in the search

    Returns
    -------
    ld_res : list
        List of uid and search result
    """
    ld = ldap.initialize(server)
    ld.simple_bind_s()
    ld_res = ld.search_s(base, scope, filterstr)
    ld.unbind_s()

    return ld_res


if __name__ == "__main__":
    pass
