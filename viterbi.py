import numpy as np
import copy


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
        aux=[1]
        i=aux+i
        i.append(1)
        mapa_aux.append(i)

    
    a=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    mapa_aux=a+mapa_aux+a

    return mapa_aux

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
def states_prob(mapa):
    states=[]

    for i,m in enumerate(mapa):
        states.append([])
        for j in m:
            if(j==1):
                states[i].append(0)
            else:
                states[i].append(1/44)
    return states


def emision(mapa,sequence):
    m_emision = []

   
    for s,i in enumerate(sequence):
        m_emision.append([])
        for j in range(1,5):
            for k in range(1,17):

                                   #sur               #norte                 #este               #oeste
                if(i=="NS"  and mapa[j+1][k]==1 and mapa[j-1][k]==1 and mapa[j][k-1]==0 and mapa[j][k+1]==0):
                    m_emision[s].append(700/64)
                elif(i=="NWE" and mapa[j+1][k]==0 and mapa[j-1][k]==1 and mapa[j][k-1]==1 and mapa[j][k+1]==1):
                    m_emision[s].append(200/64)
                elif(i=="NSE" and mapa[j+1][k]==1 and mapa[j-1][k]==1 and mapa[j][k-1]==1 and mapa[j][k+1]==0):
                    m_emision[s].append(200/64)
                elif(i=="WE"  and mapa[j+1][k]==0 and mapa[j-1][k]==0 and mapa[j][k-1]==1 and mapa[j][k+1]==1):
                    m_emision[s].append(400/64)
                elif(i=="NSW"  and mapa[j+1][k]==1 and mapa[j-1][k]==1 and mapa[j][k-1]==0 and mapa[j][k+1]==1):
                    m_emision[s].append(200/64) 
                elif(i=="E"  and mapa[j+1][k]==0 and mapa[j-1][k]==0 and mapa[j][k-1]==1 and mapa[j][k+1]==0):
                    m_emision[s].append(200/64)
                else:
                    m_emision[s].append(0)

    return m_emision  

def init_states(mapa):
    states=[]

    for i,r in enumerate(mapa):                
        for j,c in enumerate(r):            
            if(mapa[i][j]==0):
                states.append([i,j])
    return states





def viterbi(obs_seq):
        # returns the most likely state sequence given observed sequence x
        # using the Viterbi algorithm
        T = len(obs_seq)
        N = A.shape[0]
        delta = np.zeros((T, N))
        psi = np.zeros((T, N))
        delta[0] = pi*B[:,obs_seq[0]]
        for t in range(1, T):
            for j in range(N):
                delta[t,j] = np.max(delta[t-1]*A[:,j]) * B[j, obs_seq[t]]
                psi[t,j] = np.argmax(delta[t-1]*A[:,j])

        # backtrack
        states = np.zeros(T, dtype=np.int32)
        states[T-1] = np.argmax(delta[T-1])
        for t in range(T-2, -1, -1):
            states[t] = psi[t+1, states[t+1]]
        return states

def trans_matrix(mapa,states):
    matrices=[] 



    for n,i in enumerate(states):
        matrix=[]
        count=0
        for r in range(6):
            matrix.append([])
            for j in range (18):
                matrix[r].append(0)

        if(mapa[i[0]+1][i[1]]==1):
                count+=1                
        else:
            matrix[i[0]+1][i[1]]=0.25
        if(mapa[i[0]-1][i[1]]==1):
                count+=1
        else:
            matrix[i[0]-1][i[1]]=0.25
        if(mapa[i[0]][i[1]+1]==1):
                count+=1
        else:
            matrix[i[0]][i[1]+1]=0.25
        if(mapa[i[0]][i[1]-1]==1):
                count+=1
        else:
            matrix[i[0]][i[1]-1]=0.25

        matrix[i[0]][i[1]]=count/4

        print(matrix)
        print("----")
        matrices.append(matrix)
    return matrices

        
if __name__ == "__main__":

    mapa=create_map()
    emision_test=init_secuence(1)
    prob_emision=emision(mapa,emision_test)
    states_prob=states_prob(mapa)
    states=init_states(mapa)
    trans=trans_matrix(mapa,states)
    #print(trans[0])

    
    

    




   


        