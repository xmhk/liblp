
import numpy as np



def pyfindpeaks( environment, valuelist , thresh):
    """Determine peak positions in a list or array of real values.

    Arguments:
      - environment: (INT) a maxima has to be the local maximum in this environment of points
      - valuelist: list or array of points to find the maxima in
      - thresh: a maximum has to be larger than this value

    Returns:
      - listindices: positions of the peaks found

    """
    def limitss(diff,length,pos):
    #this prevents hitting the borders of the array
        mi = np.max( [0, pos-diff])
        ma = np.min( [length, pos+diff])
        return mi,ma
    #range left/right
    half = int( np.floor( environment/2))
    valuelistlength = len(valuelist)
    #pre-filter the peaks above threshold
    abovethresh = np.nonzero( valuelist>thresh )[0]
    i = 0
    peakpos =np.array([],int)
    # circle through the candidates
    while (i < len(abovethresh)):
        mi,ma = limitss(half, valuelistlength, abovethresh[i])
        partialvaluelist = valuelist[mi:ma]
    # is the valuelist value of the actual position the maximum of the environment?
        if valuelist[abovethresh[i]] == max(partialvaluelist):
            peakpos=np.append(peakpos,abovethresh[i])
        i = i+1
    return peakpos