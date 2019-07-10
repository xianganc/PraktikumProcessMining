class PetriNet():
    def __init__(self):
        self.places = []
        self.transitions = []
        self.input = []
        self.output = []

    def __str__(self):
        pn = []
        pn.append("Places: {}".format(self.places))
        pn.append("Transitions: {}".format(self.transitions))
        pn.append("Input: {}".format(self.input))
        pn.append("Output: {}".format(self.output))
        return '\n'.join(pn)

    def generate_with_alpha(self, alpha_model, dotfile='pn.dot'):
        self.transitions = alpha_model.tl
        self.input = alpha_model.ti
        self.output = alpha_model.to
        iso = self.__isolated_transitions(alpha_model)
        digraph = self.__pn_description(alpha_model.yl, alpha_model.ti, alpha_model.to, iso)
        with open(dotfile, 'w') as f:
            f.write(digraph)

    def __pn_description(self, yl, ti, to, iso):
        pn = []
        pn.append("digraph pn {")
        pn.append("rankdir=LR;")
        n = ""
        for c in iso:
            pn.append('"{}" [shape=box];'.format(c))
        for pair in yl:
            n+= " "
            for i in pair[0]:
                pn.append('"{}" -> "{}";'.format(i,n))
                pn.append('"{}" [shape=box];'.format(i))
                pn.append('"{}" [shape=circle];'.format(n))
            for i in pair[1]:
                pn.append('"{}" -> "{}";'.format(n, i))
                pn.append('"{}" [shape=box];'.format(i))
        for i in ti:
            print("-----------------")
            print(i)
            print("-----------------")
            pn.append('In -> "{}" '.format(str(i)))
        for o in to:
            pn.append('"{}" -> Out'.format(o))
        pn.append("}")
        return '\n'.join(pn)

    def __isolated_transitions(self, alpha_model):
        tl = alpha_model.tl
        yl = alpha_model.yl
        ti = alpha_model.ti
        to = alpha_model.to

        yl_transitions = set()
        for pair in yl:
            for p in pair:
                yl_transitions.add(p[0])

        appeared = ti | to | yl_transitions
        iso = tl - appeared
        return iso