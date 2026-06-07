def learn_theta(data, colors):
    '''
    Finds theta that is larger than all blue and less than all red.
    '''
    max_blue = max(data[i] for i in range(len(data)) if colors[i] == 'blue')
    return max_blue


def compute_ell(data, colors, theta):
    '''
    Computes the loss function L(theta) for a given theta.
    '''
    loss = 0
    
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1
            
    return float(loss)


def minimize_ell(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) using quadratic time complexity.
    '''
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)
    
    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta
            
    return float(best_theta)


def minimize_ell_sorted(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) in linear time.
    '''
    n = len(data)
    red_le_theta = 0
    blue_gt_theta = sum(1 for c in colors if c == 'blue')
    
    best_theta = data[0]
    best_loss = red_le_theta + blue_gt_theta
    
    for alpha in range(n):
        if colors[alpha] == 'red':
            red_le_theta += 1
        else:
            blue_gt_theta -= 1
        
        loss = red_le_theta + blue_gt_theta
        
        if loss < best_loss:
            best_loss = loss
            best_theta = data[alpha]
    
    return float(best_theta)

