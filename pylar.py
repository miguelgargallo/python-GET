from bs4 import BeautifulSoup
import pprint


def get_resultats(i):
    res = {}
    with open(str(i)) as f:
        s = BeautifulSoup(f)
        noms = set()
        nom = None
        num = None
        for x in s.recursiveChildGenerator():
            if x.name == 'td':
                aux = x.next
                if '\n' in aux:
                    aux = aux.split('\n')[0]
                    if aux == '':
                        continue
                if nom is None:
                    if x.title != '':
                        nom = aux
                        noms.add(nom)
                else:
                    try:
                        num = int(aux)
                    except ValueError:
                        nom = None
                        continue
                    if nom not in res:
                        res[nom] = {'punts': [], 'partides': 0}
                    res[nom]['partides'] += 1
                    res[nom]['punts'].append(num)
                    nom = None
    return res


# Use the get_resultats function to parse the results for each match
res = {}
claus_per_partida = []
N = 71
for i in range(N-20, N+1):
    r = get_resultats(i)
    claus_per_partida.append(set(r.keys()))
    for k in r:
        if k not in res:
            res[k] = {'punts': [], 'partides': 0}
        res[k]['partides'] += 1
        res[k]['punts'].append(r[k]['punts'])

# Get the players that have played in all the matches
claus = claus_per_partida[0]
for c in claus_per_partida[1:]:
    claus = claus.intersection(c)

# Print the results
pprint.pprint(res)

# Save all to an output file called super.md
with open('super.md', 'w') as f:
    f.write('| Nom | Puntuació |\n')
    f.write('| --- | --------- |\n')
    for k in sorted(res, key=lambda x: res[x]['punts'], reverse=True):
        f.write('| {} | {} |\n'.format(k, res[k]['punts']))
