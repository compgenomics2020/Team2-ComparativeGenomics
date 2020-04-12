#!/usr/bin/env python3
'''
  *******************************************************************
  **************-Create phylogeny from kSNP results-*****************
  *******************************************************************

  The usage for this script is: python3 make_phylogeny.py <path/to/input_file.tre> </path/to/output/location>

  By: Courtney Astore
  Last updated: 04/09/2020

'''
import sys
from ete3 import Tree, TreeStyle

tree_file = sys.argv[1]
output_path = sys.argv[2]
file_name = "my_tree.png"
out_file = output_path + "/" + file_name

with open(tree_file, 'r') as f:
    tree_data = f.read().replace('\n', '')

t = Tree(tree_data)
circular_style = TreeStyle()
circular_style.mode = "c"
circular_style.scale = 20
t.render("mytree.png", w=183, units="mm", tree_style=circular_style)
#ts = TreeStyle()
#ts.show_leaf_name = True
#ts.show_branch_length = True
#ts.show_branch_support = True
#ts.render(out_file, dpi=300, w=500, tree_style = ts)

'''
def Generate_makeTree(tree_file, output_path):
# Define output file name and its path
        file_name = "my_tree.png"
        out_file = output_path + "/" + file_name

# Read in .tre file as string
        with open(tree_file, 'r') as f:
                tree_data = f.read().replace('\n', '')

# Build tree & incorporate desired parameters for visualization
        build_tree = Tree(tree_data)
        ts = TreeStyle()
        ts.show_leaf_name = True
        ts.show_branch_length = True
        ts.show_branch_support = True

# Produce/draw output figure: phylogeny
        tree.render(out_file, dpi=300, w=500, tree_style = ts)

def main():
        tree_file = sys.argv[1]
        output_path = sys.argv[2]
        makeTree = Generate_makeTree(tree_file, output_path)
if __name__ == "__main__":
    main()
'''
