#!/usr/bin/env python3
# Copyright (C) 2014 Russell Haley
# 
# This file is part of euler.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import itertools

class Digraph:
    """
    A directed graph data structure.
    """

    def __init__(self):
        self.vertices = {}
        self.arc_out_table = {}
        self.arc_in_table = {}
        self.arc_props = {}
        self.idgen = itertools.count()

    def __getitem__(self, vertex_id):
        try:
            return self.vertices[vertex_id]
        except TypeError:
            return [ self.vertices[k] for k in vertex_id ]

    def __iter__(self):
        return iter(self.vertices)

    def connect(self, arc, arc_prop=None):
        """
        Create an arc from arc[0] to arc[1], with optional property.

        Parameters
        ----------
        arc : tuple of int
            Pair of (from, to) vertex_ids that specifies an arc.
        arc_proc : object, optional
            Some property of the arc. Cost, etc.
        
        Notes
        -----
        If the arc already exists, disconnect() does not create a
        duplicate arc.  It does, however, replace the existing arc
        property with the specified property, to insure idempotence.
        """
        from_vertex, to_vertex = arc
        if to_vertex not in self.arc_out_table[from_vertex]:
            self.arc_out_table[from_vertex].append(to_vertex)
            self.arc_in_table[to_vertex].append(from_vertex)
        if arc_prop is not None:
            self.arc_props[(from_vertex,to_vertex)] = arc_prop

    def disconnect(self, arc):
        """
        Destroy the arc from arc[0] to arc[1].

        Parameters
        ----------
        arc : tuple of int
            Pair of (from, to) vertex_ids that specifies an arc.

        Notes
        -----
        If the arc does not exist, disconnect() does nothing. I.e., it
        is idempotent.
        """
        from_vertex, to_vertex = arc
        if to_vertex in self.arc_out_table[from_vertex]:
            self.arc_out_table[from_vertex].remove(to_vertex)
            self.arc_in_table[to_vertex].remove(from_vertex)
            self.arc_props.pop((from_vertex,to_vertex),None)

    def insert(self,item):
        """
        Insert a vertex into the graph and return the vertex_id.
        """
        key = next(self.idgen)
        self.vertices[key] = item
        self.arc_in_table[key] = []
        self.arc_out_table[key] = []
        return key

    def _pop(self, vertex_id):
        """
        Internal pop with undefined behavior if vertex_id is not in the graph.
        """
        # destroy connections
        for arc_out in self.arc_out_table[vertex_id]:
            self.disconnect(vertex_id, arc_out)
        for arc_in in self.arc_in_table[vertex_id]:
            self.disconnect(arc_in, vertex_id)
        # pop vertex
        return self.vertices.pop(vertex_id)

    def pop(self, vertex_id, *args):
        """
        Remove specified vertex_id and return vertex data.

        Parameters
        ----------
        vertex_id : int
            pop this vertex
        default : object, optional, positional
            If vertex_id is not in the graph, default is returned
        """
        if len(args) > 1:
            raise TypeError("pop expected at most 2 arguments, "
                            "got {}".format(len(args)+1))
        if vertex_id in self:
            return self._pop(vertex_id)
        elif len(args) == 1:
            return args[0]
        else:
            raise KeyError(vertex_id)

    def children(self, vertex_id):
        """
        Get a list of vertices reachable from vertex_id in a single hop.
        """
        return self.arc_out_table[vertex_id]

    def parents(self, vertex_id):
        """
        Get a list of vertices that can reach vertex_id in a single hop.
        """
        return self.arc_in_table[vertex_id]

    def arc_prop(self, arc):
        """
        Get the arc property for arc.

        Parameters
        ----------
        arc : tuple of int
            Pair of (from, to) vertex_ids that specifies an arc.
        """
        return self.arc_props[arc]
        

