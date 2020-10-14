# -*- coding: utf-8 -*-
#!/usr/bin/python3

# =============================================================================
# dict defining complimentary nucleotides
# =============================================================================

nt_dict = {
    "A" : "T",
    "T" : "A",
    "G" : "C",
    "C" : "G"
}

# =============================================================================
# defining Seq class 
# =============================================================================

class Seq:
    
    def __init__(self, seq = str()):

        self.seq = seq 
        self.l = len(seq)
        self.rev_comp = self.__revComp()
        print("=========")
        self.reportSeq()
        self.reportLen()
        self.reportRevComp()
    
    # methods for report seq characteristics
    def reportSeq(self):
        
        print("The seq is {}.".format(self.seq))
        
    def reportLen(self):
        
        print("The length of the seq is {}.".format(self.l))
        
    def reportRevComp(self):
        
        print("The reverse compliment of the seq is {}.".format(self.rev_comp))
        
    # methods for altering seq   
    def changeSeq(self, new = str()):
        
        self.__init__(new)
        
        
    def extendSeq(self, add = str()):
        
        self.__init__(self.seq+add)
        
    # get reverse compliment 
    def __revComp(self):
        
        return "".join([nt_dict[n] for n in self.seq])[::-1]
    
    # find the index positions using 1-indexing of motif in sequence
    def findMotif(self, motif):
        
        """
        Find the 5' nt position of all instances of a motif in sequence
        """
        
        motif_locations = []
        
        for idx in range(len(self.seq)):
                
            if self.seq[idx:idx+len(motif)] == motif:
                
                motif_locations.append(idx+1)
                
        return motif_locations


s = Seq("ATG")
    


s.changeSeq("AAAAGCCGTAATTG")
        
