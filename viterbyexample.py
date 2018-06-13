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