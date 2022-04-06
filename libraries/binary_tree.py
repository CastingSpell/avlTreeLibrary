# -*- coding: utf-8 -*-
# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e Ingeneiría de Datos
#                 Facultade de Informática
#                 Universidade da Coruña
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

from exceptions import Empty

class BinaryTree:
  """Class representing a binary tree."""

  #-------------------------- public generator --------------------------

  def __init__(self, element=None, left=None, right=None):
    """Create a binary tree.

    In a zero parameter form, the resulting binary tree will be empty
    
    In a single parameter form, element should be a leaf value,
    and the binary tree will have that value at an isolated node.

    In a three-parameter version, and left and right should be existing 
    Binary Tree instances
    
    Nota that the following two calls are equivalent:
        BinaryTree(10)
        BinaryTree(10, BinaryTree(), BinaryTree())
    """
    # firstly, an empty tree is created
    self._element = None   # indicator of an empty tree
    self._left = None
    self._right = None
    self._parent = None
    # secondly, only if element is provided, a non-empty tree is created
    if element is not None:
        self._element = element
        
        if left is not None:                        # if left is not None
            if not isinstance(left, BinaryTree):
                raise TypeError('Left child must be a BinaryTree')
            self._left = left
            left._parent = self
        else:
            self._left = BinaryTree()   # None is not a valid empty tree
            self._left._parent = self
        
        if right is not None:                       # if right is not None
            if not isinstance(left, BinaryTree):
                raise TypeError('Right child must be a BinaryTree')
            self._right = right
            right._parent = self
        else:
            self._right = BinaryTree()  # None is not a valid empty tree
            self._right._parent = self
      
  #-------------------------- public accessors --------------------------
  
  def __repr__(self):
      resultado = "("
      if not self.is_empty():
          resultado = resultado\
                     + repr(self.root_element())\
                     + " " + repr(self.left_child())\
                     + " " + repr(self.right_child())
      resultado += ")"
      return resultado
      
  def root_element(self):
    """Return the element at the root of the tree."""
    if self.is_empty():
        raise Empty('BinaryTree is empty')
    return self._element

  def parent(self):
    """Return the parent (or an empty tree if there is no parent)."""
    if self.is_empty():
        raise Empty('BinaryTree is empty')
    if self._parent:
        return self._parent
    else:
        return BinaryTree()

  def left_child(self):
    """Return the left child (or None if no left child)."""
    if self.is_empty():
        raise Empty('BinaryTree is empty')
    return self._left

  def right_child(self):
    """Return the right child (or None if no right child)."""
    if self.is_empty():
        raise Empty('BinaryTree is empty')
    return self._right

  def is_empty(self):
    """Return TRue is self is empty. False otherwise."""
    return self._element is None


    