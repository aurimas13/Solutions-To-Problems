# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # -----------------------------------
        def dfs(node):

            if not node:
                # base case:
                # empty node or leaf node
                dfs.path.append('X')

            else:
                # general case:
                # generate path preorder traversal
                dfs.path.append( str(node.val) )

                dfs( node.left )
                dfs( node.right )
        # -----------------------------------

        dfs.path = []
        dfs(node=root)
        return ' '.join(dfs.path)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_values = iter( data.split() )

        # --------------------------------
        def rebuild( node_values ):

            next_val = next( node_values )

            if next_val == 'X':
                # base case:
                # empty node or leaf node
                return None
            
            else:
                # general case:
                # rebuild with preorder path
                root = TreeNode(next_val)

                root.left = rebuild( node_values )
                root.right = rebuild( node_values )

                return root
        # --------------------------------
        return rebuild(node_values)
        