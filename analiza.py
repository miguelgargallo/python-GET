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
    # pprint.pprint(noms)
    return res


res = {}
claus_per_partida = []
N = 71
for i in range(N-20, N+1):
    r = get_resultats(i)
    for (x, y) in r.items():
        if x not in res:
            res[x] = [y]
        else:
            res[x].append(y)
    claus_per_partida.append(set(r.keys()))

res_analitzats = {}

for (x, y) in res.items():
    # if len(y)<15: continue
    if x not in claus_per_partida[-1]:
        continue
    punts = [k for z in y for k in z['punts']]
    partides = [z['partides'] for z in y]
    res_analitzats[x] = {}
    res_analitzats[x]['punts'] = {'min': min(
        punts), 'max': max(punts), 'avg': sum(punts)/len(punts)}
    res_analitzats[x]['torns'] = {'min': min(partides), 'max': max(
        partides), 'avg': sum(partides)/len(partides)}
    res_analitzats[x]['num_partides'] = len(partides)

for (i, (x, y)) in enumerate(sorted(res_analitzats.items(), key=lambda z: z[1]['torns']['avg']), 1):
    print(f'Pos {i}:', x)
    pprint.pprint(res_analitzats[x])
    print('')
