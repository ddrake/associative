# Objects of this class are used recursively to build up a tree structure
# whose leaf nodes include all the possible parenthesizations of a list of 
# letters.  
# For example, one parenthesization for the string (list of letters) 'abcde' 
# is '(a(bc))(de)'
# This version generates some redundant branches so is unlikely to be
# efficient for large lists.
class AssocTree:
	def __init__(self, elems, parent):
		self.elems = elems
		self.parent = parent
		self.branches = []
		self.leaves = set()

	@staticmethod
	def from_string(s):
		elems = [c for c in s]
		return AssocTree(elems, None)

	# build the tree and return the list of unique parenthesizations 
	def build_tree(self):
		self.branches = []
		if len(self.elems) == 1:
			self.leaves = set()
			self.leaves.add(self.elems[0])
		else:
			for i in range(len(self.elems)-1):
				newelem = "(" + self.elems[i] + self.elems[i+1] + ")";
				newelems = self.elems[:i] + [newelem] + self.elems[i+2:]
				newtree = AssocTree(newelems, self)
				self.leaves = self.leaves.union(newtree.build_tree())
				self.branches.append(newtree)
		return self.leaves

# example usage

# In [3]: t = AssocTree.from_string('abcde')

# In [4]: t.build_tree()
# Out[4]:
# {'((((ab)c)d)e)',
#  '(((a(bc))d)e)',
#  '(((ab)(cd))e)',
#  '(((ab)c)(de))',
#  '((a((bc)d))e)',
#  '((a(b(cd)))e)',
#  '((a(bc))(de))',
#  '((ab)((cd)e))',
#  '((ab)(c(de)))',
#  '(a(((bc)d)e))',
#  '(a((b(cd))e))',
#  '(a((bc)(de)))',
#  '(a(b((cd)e)))',
#  '(a(b(c(de))))'}

# In [5]: len(_)
# Out[5]: 14