import numpy as np


def create_map():
    #Representacion mapa: 0:Vacio,1:Pared,2:Oro,3:Wumpus
    mapa=[]
    for i in range(4):
        mapa.append([])
        for j in range (16):
            mapa[i].append(0)

    mapa[0][4]=1
    mapa[0][9]=3
    mapa[0][10]=1
    mapa[0][14]=1
    mapa[1][0]=1
    mapa[1][1]=1
    mapa[1][4]=1
    mapa[1][6]=1
    mapa[1][7]=1
    mapa[1][9]=1
    mapa[1][11]=1
    mapa[1][13]=1
    mapa[1][14]=1
    mapa[1][15]=1
    mapa[2][0]=1
    mapa[2][4]=1
    mapa[2][6]=1
    mapa[2][7]=1
    mapa[2][13]=1
    mapa[2][14]=1
    mapa[2][15]=2
    mapa[3][2]=1
    mapa[3][6]=1
    mapa[3][2]=1
    mapa[3][11]=1
    mapa_aux=[]
    for i in mapa:
        print(i)
        aux=[1]
        i=aux+i
        i.append(1)
        mapa_aux.append(i)
    print("---")
    
    a=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    mapa_aux=a+mapa_aux+a
    for i in mapa_aux:
        print(i)
    print("---")

    return mapa

def init_secuence(i):
    #Secuencia observable
    sequence=[]
    E1= ["NS", "NS" , "NS", "NWE"]
    E2= ["NS", "NS", "NSE"]
    E3= ["WE", "WE", "NS", "NS"]
    E4= ["E", "E", "E", "NSW"]
    sequence.append(E1)
    sequence.append(E2)
    sequence.append(E3)
    sequence.append(E4)

    return sequence[i-1]

def emision(sequence,mapa):
    m_emision = []

    for i in sequence:
        m_emision.append([])
        for j in mapa:
            for k in j:             #sur               #norte                 #este               #oeste
                if(i=="NS"  and mapa[j+1][k]==1 and mapa[j-1][k]==1 and mapa[j][k-1]==0 and mapa[j][k+1]==0):
                    m_emision.append(700/64)
                if(i=="NWE" and mapa[j+1][k]==0 and mapa[j-1][k]==1 and mapa[j][k-1]==1 and mapa[j][k+1]==1):
                    m_emission.append(200/64)
                if(i=="NSE" and mapa[j+1][k]==1 and mapa[j-1][k]==1 and mapa[j][k-1]==1 and mapa[j][k+1]==0):
                    m_emission.append(200/64)
                if(i=="WE"  and mapa[j+1][k]==0 and mapa[j-1][k]==0 and mapa[j][k-1]==1 and mapa[j][k+1]==1):
                    m_emission.append(400/64)
                if(i=="NSW"  and mapa[j+1][k]==1 and mapa[j-1][k]==1 and mapa[j][k-1]==0 and mapa[j][k+1]==1):
                    m_emission.append(200/64) 
                if(i=="E"  and mapa[j+1][k]==0 and mapa[j-1][k]==0 and mapa[j][k-1]==1 and mapa[j][k+1]==0):
                    m_emission.append(200/64)    





def viterbi(hmm, initial_dist, emissions):
    probs = hmm.emission_dist(emissions[0]) * initial_dist
    stack = []

    for emission in emissions[1:]:
        trans_probs = hmm.transition_probs * np.row_stack(probs)
        max_col_ixs = np.argmax(trans_probs, axis=0)
        probs = hmm.emission_dist(emission) * trans_probs[max_col_ixs, np.arange(hmm.num_states)]

        stack.append(max_col_ixs)

    state_seq = [np.argmax(probs)]

    while stack:
        max_col_ixs = stack.pop()
        state_seq.append(max_col_ixs[state_seq[-1]])

    state_seq.reverse()

    return state_seq



if __name__ == "__main__":

    mapa=create_map()
    sequence=init_secuence(1)
    print(mapa)
    
    

    




   


        