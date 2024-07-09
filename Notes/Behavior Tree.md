# Behavior Tree
#1-projects/FURP 

- Control Nodes: Govern the flow of execution within the tree.These are non-leaf nodes of the tree.
	- Sequence Node (Logical AND)
	- Fallback Node  (Logical OR) 
	- Decorator Node (Conditional)
- Execution node: Represent atomic behaviors or actions that the system can perform.These are the leaf nodes of the tree
	- Action
	- Condition