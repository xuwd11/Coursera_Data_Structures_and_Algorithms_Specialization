class ActivePoint:
    def __init__(self, active_node, active_edge, active_length, text):
        self.node = active_node
        self.edge_pos = active_edge
        self.length = active_length
        self.text = text

    @property
    def edge(self):
        if self.edge_pos is None:
            return None
        return self.node.get_edge(self.text[self.edge_pos])

    @property
    def edge_char(self):
        if self.edge_pos is None:
            return None
        return self.text[self.edge_pos]

    def __repr__(self):
        return 'ActivePoint(%s, %s, %s)' % (self.node.id, self.edge_char,
                                            self.length)


class Edge:
    def __init__(self, start, text, node, end=-1):
        self.start = start
        self.end = end
        self.text = text
        self.node = node

    def split(self, split_length, current_pos, text):
        new_end = self.start + split_length
        new_node = Node()
        new_node.edges = self.node.edges
        new_node.suffix_link = self.node.suffix_link
        self.node.clear_edges()
        self.node.add_edge(Edge(new_end, self.text, new_node,
                                end=self.end))
        self.node.add_edge(Edge(current_pos, text, Node()))
        self.end = new_end
        self.node.suffix_link = None
        return self.node

    def length(self):
        return self.end - self.start if self.end != -1 else 999999999

    @property
    def start_char(self):
        return self.text[self.start]

    def str(self):
        return self.text[self.start:self.end]

    def __repr__(self):
        return self.str()


class Node:

    total = 0

    def __init__(self):
        Node.total += 1
        self.id = self.total
        self.suffix_link = None
        self.edges = {}

    def add_edge(self, e):
        self.edges[e.start_char] = e

    def get_edge(self, start_char):
        return self.edges.get(start_char)

    def clear_edges(self):
        self.edges = {}


class SuffixTree:

    def __init__(self, text, canonicize='~'):
        self.root = Node()
        self.text = text
        self.canonicize = canonicize
        if canonicize in text:
            raise ValueError("text can not contain canonicize!")
        self.build()

    def build(self):
        text = self.text# + self.canonicize
        self.active_point = ActivePoint(self.root, None, 0, text)
        self.reminder = 0

        for i, c in enumerate(text):
            self.extend(text, i, c)

    def add_suffix_link(self, node):
        if self.pre_node:
            self.pre_node.suffix_link = node
        self.pre_node = node

    def walk_down(self, edge):
        active_point = self.active_point
        if active_point.length >= edge.length():
            active_point.edge_pos += edge.length()
            active_point.length -= edge.length()
            active_point.node = edge.node
            return True
        return False

    def extend(self, text, current, c):
        self.reminder += 1
        self.pre_node = None
        active_point = self.active_point

        while self.reminder:
            if active_point.length == 0:
                active_point.edge_pos = current

            active_edge = active_point.edge

            if active_edge is None:
                active_point.node.add_edge(Edge(current, text, Node()))
                self.add_suffix_link(active_point.node) # Rule 2
            else:
                if self.walk_down(active_edge): # Observation 2
                    continue
                if active_edge.text[active_edge.start + active_point.length] == c:
                    # Observation 1
                    active_point.length += 1
                    self.add_suffix_link(active_point.node)  # Observation 3
                    break

                split_node = active_edge.split(active_point.length, current, text)
                self.add_suffix_link(split_node)  # Rule 2

            self.reminder -= 1

            if active_point.node is self.root and active_point.length > 0:
                # Rule 1
                active_point.length -= 1
                active_point.edge_pos = current - self.reminder + 1
            else:
                # Rule 3
                if active_point.node.suffix_link is not None:
                    active_point.node = active_point.node.suffix_link
                else:
                    active_point.node = self.root


class GeneralizedSuffixTree(SuffixTree):

    def __init__(self, texts):
        self.start_pos = [0]
        concat_str = ''
        for i, text in enumerate(texts):
            terminal_char = chr(i + 1)
            if terminal_char in text:
                raise ValueError("text can not contain canonicize!")
            concat_str += text + terminal_char
            self.start_pos.append(len(text))

        self.concat_str = concat_str
        SuffixTree.__init__(self, self.concat_str)


def export_graph(root, write):
    def export_edges(node):
        for e in node.edges.values():
            write(e)
            export_edges(e.node)
    export_edges(root)

def print_func(s):
    print(s)


if __name__ == "__main__":
    #tree = SuffixTree('abcabxabcd')
    #export_graph(tree.root, print_func)
    s = input()
    tree = SuffixTree(s)
    export_graph(tree.root, print_func)