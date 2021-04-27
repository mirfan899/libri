from g2p_en import G2p

texts = ["MORREL", "VILLEFORT", "NOIRTIER", "D'AVRIGNY",
         "MAKEST", "FLAMELETS", "DELECTASTI", "GIVETH", "AFRICANUS", "VENI", "SPONSA", "LIBANO", "NEED'ST"]
g2p = G2p()
for text in texts:
    out = g2p(text)
    print(text, out)
