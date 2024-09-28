cidadex = 70000
cidadey = 180000
anos = 0

while (cidadex < cidadey):
    cidadex = cidadex + ((3.5 / 100) * cidadex)
    cidadey = cidadey + ((1.5 / 100) * cidadey)
    anos += 1

print('Sabendo que a cidade x cresce 3,5% ao ano \n e que a cidade y cresce 1,5% ao ano \n ao passar de {} anos a ciade x ultrapassará ou ira igualar a população com a cidade y' .format(anos))
