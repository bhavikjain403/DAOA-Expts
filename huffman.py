class NodeTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

def huffmanCode(node, binString = ""):
    if type(node) is str:
        return {node : binString}
    (l,r)= node.children()
    d = dict()
    d.update(huffmanCode(l, binString+"0"))
    d.update(huffmanCode(r, binString+"1"))
    return d

s = input("Enter string to be compressed : ")
freq = {}
for c in s:
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1

freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
nodes = freq
while len(nodes)>1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1+c2))
    nodes = sorted(nodes, key= lambda x: x[1], reverse=True)

huffman = huffmanCode(nodes[0][0])
print("The Huffman codes are as follows :")
for (c,f) in freq:
    print(c,"--->",huffman[c])