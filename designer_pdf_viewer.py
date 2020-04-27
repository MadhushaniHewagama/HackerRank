def designerPdfViewer(h, word):
    m_h=0
    for i in word:
        val=ord(i)-97
        c_h=h[val]
        if(m_h<c_h):
            m_h=c_h
    return m_h*len(word)
        #print(val)

h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)
print(result)
