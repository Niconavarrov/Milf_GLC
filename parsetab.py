
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'colon comma curlyb curlybF key_average key_course key_grades key_id key_name number_value sbracket sbracketF string_valueS : sbracket A sbracketFA : curlyb B curlybF comma AA : curlyb B curlybFB : key_id colon number_value comma CC : key_name colon string_value comma DD : key_course colon string_value comma EE : key_grades colon sbracket G sbracketF comma FG : number_value\n         | number_value comma GF : key_average colon number_value'
    
_lr_action_items = {'sbracket':([0,26,],[2,27,]),'$end':([1,5,],[0,-1,]),'curlyb':([2,10,],[4,4,]),'sbracketF':([3,8,12,28,29,33,],[5,-3,-2,30,-8,-9,]),'key_id':([4,],[7,]),'curlybF':([6,14,19,24,34,37,],[8,-4,-5,-6,-7,-10,]),'colon':([7,15,20,25,35,],[9,16,21,26,36,]),'comma':([8,11,17,22,29,30,],[10,13,18,23,31,32,]),'number_value':([9,27,31,36,],[11,29,29,37,]),'key_name':([13,],[15,]),'string_value':([16,21,],[17,22,]),'key_course':([18,],[20,]),'key_grades':([23,],[25,]),'key_average':([32,],[35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'A':([2,10,],[3,12,]),'B':([4,],[6,]),'C':([13,],[14,]),'D':([18,],[19,]),'E':([23,],[24,]),'G':([27,31,],[28,33,]),'F':([32,],[34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> sbracket A sbracketF','S',3,'p_start','yacc.py',6),
  ('A -> curlyb B curlybF comma A','A',5,'p_multiple_records','yacc.py',10),
  ('A -> curlyb B curlybF','A',3,'p_single_record','yacc.py',14),
  ('B -> key_id colon number_value comma C','B',5,'p_record_structure','yacc.py',18),
  ('C -> key_name colon string_value comma D','C',5,'p_name','yacc.py',24),
  ('D -> key_course colon string_value comma E','D',5,'p_course','yacc.py',30),
  ('E -> key_grades colon sbracket G sbracketF comma F','E',7,'p_grades','yacc.py',36),
  ('G -> number_value','G',1,'p_grade_list','yacc.py',42),
  ('G -> number_value comma G','G',3,'p_grade_list','yacc.py',43),
  ('F -> key_average colon number_value','F',3,'p_average','yacc.py',50),
]
