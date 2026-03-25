def DNA_strand(dna):
    comp_dna = []
    for symbol in dna:
        if symbol == "A":
            comp_dna.append("T")
        elif symbol == "T":
            comp_dna.append("A")
        elif symbol == "C":
            comp_dna.append("G")
        elif symbol == "G":
            comp_dna.append("C")
        else:
            pass
    
    dna = "".join(comp_dna)
    return dna
