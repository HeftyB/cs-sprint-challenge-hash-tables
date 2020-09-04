def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    wldict = {}
    
    for index, weight in enumerate(weights):
        wldict[limit - weight] = index
    
    for index, i in enumerate(weights):
        if i in wldict:
            if index > wldict[i]:
                ret = (index, wldict[i])
                return ret
            else:
                ret = (wldict[i], index)
                return ret

    return None
