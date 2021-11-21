    #!/usr/bin/env python
    # coding: utf-8
    
    # In[1]:
def topsis(inputlst):
    
    #cleaning inputlst

    for i in range(len(inputlst)):
        for j in range(len(inputlst[0])):
            if inputlst[i][j]=='':
                inputlst[i][j]=0


    w=0.25
    
    
    # In[2]:
    
        
    
    # ### Normalization
    
    # In[6]:
    
    
    newinputlst=[[0 for i in range(len(inputlst[0]))] for j in range(len(inputlst))]
    print(newinputlst)  
    
    
    # In[12]:
    
    
    for i in range(len(inputlst[0])):
        maxi=max(inputlst[j][i] for j in range(len(inputlst)))
        for j in range(len(inputlst)):
            newinputlst[j][i]=(inputlst[j][i])/maxi
    print(newinputlst)
    
    
    # In[13]:
    
    
    for i in range(len(newinputlst)):
        newinputlst[i][3]=1-newinputlst[i][3]
    print(newinputlst)
    
    
    # ### Weighted normalized matrix
    
    # In[14]:
    
    
    newinputlst=[[w*i for i in j] for j in newinputlst]
    print(newinputlst)
    
    
    # ## Positive Ideal solution and Negative Ideal solution
    
    # In[19]:
    
    
    p_ideal=[max([i[j] for i in newinputlst]) for j in range(len(newinputlst[0]))]
    n_ideal=[min([i[j] for i in newinputlst]) for j in range(len(newinputlst[0]))]
    print(p_ideal)
    print(n_ideal)
    
    
    # ## Seperation from ideal solution
    
    # In[22]:
    
    
    p_sep=[sum([(p_ideal[i]-newinputlst[j][i]) for i in range(4)]) for j in range(len(newinputlst))]
    print(p_sep)
    
    
    # In[23]:
    
    
    n_sep=[sum([(newinputlst[j][i]-n_ideal[i]) for i in range(4)]) for j in range(len(newinputlst))]
    print(n_sep)
    
    
    # ## Calculating ranks
    
    # In[24]:
    
    
    r=[(n_sep[i]/(n_sep[i]+p_sep[i])) for i in range(len(p_sep))]
    print(r)
    
    
    # In[25]:
    
    
    r1=sorted(r)
    print(r1)
    
    
    # In[28]:
    
    
    ranks=[r1.index(i)+1 for i in r]
    dis=[]
    for i in range(len(ranks)):
        if ranks[i] in dis:
            ranks[i]+=1
        else:
            dis.append(ranks[i])

    
    return ranks

