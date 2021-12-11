'''
ast checker to iterating over all the nodes
'''

import ast,_ast
import re
import astunparse


class CodeVistor(ast.NodeVisitor):
    def __init__(self):
        dir(_ast)
        self.fileName = None
        self.defmagic = set()
        self.result = []

    def visit_FunctionDef(self,node):
      #parameters count
      def findCharacter(s,d):
        try:
          value = s.index(d)
        except ValueError:
          return -1
        else:
          return value
      stmt = astunparse.unparse(node.args)
      arguments = stmt.split(",")
      argsCount = 0
      for element in arguments:
        if findCharacter(element,'=') == -1:
          argsCount += 1
      self.result.append((1,self.fileName,node.lineno,argsCount))
      #function length
      lines = set()
      res = [node]
      while len(res) >= 1:
        t = res[0]
        for n in ast.iter_child_nodes(t):
          if not hasattr(n,'lineno') or ((isinstance(t,_ast.FunctionDef) or isinstance(t,_ast.ClassDef)) and n == t.body[0] and isinstance(n,_ast.Expr)):
            continue
          lines.add(n.lineno)
          if isinstance(n,_ast.ClassDef) or isinstance(n,_ast.FunctionDef):
            continue
          else:
            res.append(n)
        del res[0]
      self.result.append((2,self.fileName,node.lineno,len(lines))) 
      self.generic_visit(node) 

    def visit_ClassDef(self,node):
      #large class
      lines = set()
      res = [node]
      while len(res) >= 1:
        t = res[0]
        for n in ast.iter_child_nodes(t):
          if not hasattr(n,'lineno') or ((isinstance(t,_ast.FunctionDef) or isinstance(t,_ast.ClassDef)) and n == t.body[0] and isinstance(n,_ast.Expr)):
            continue
          lines.add(n.lineno)
          if isinstance(n,_ast.ClassDef) or isinstance(n,_ast.FunctionDef):
            continue
          else:
            res.append(n)
        del res[0]
      self.result.append((3,self.fileName,node.lineno,len(lines)))
      self.generic_visit(node)





