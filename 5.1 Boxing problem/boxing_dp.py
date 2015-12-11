#coding:utf-8

"""
one box is represented by tuple (h, w, l)
box list is represented by [( , , ), ( , , ), ( , , ), ...]
"""

"""
def box_cmp(b1, b2):
    assert (isinstance(b1, tuple) and isinstance(b2, tuple))
    for itme1, item2 in zip(b1, b2):
        if item1 < item2:
"""

def is_compatible(b1, b2):
    """can b1 be contained in b2 ?"""
    assert isinstance(b1, tuple) and isinstance(b2, tuple)
    for item1, item2 in zip(b1, b2):
        if item1 >= item2:
            return False
    return True

def max_box_num(box_lst):
    
    #sort by height, width, or length
    box_lst.sort()
    #print box_lst

    #initialize memo table
    n = len(box_lst)
    memo = [1] * n
    
    #iterate over all boxes, starting at the first
    for i in range(0,len(box_lst)):
        
        max  = 1; # max number of boxes that can fit in box i considering range 0...i-1
        
        #iterate over all prior boxes to see if box i can fit in box j
        for j in range(0, i):
            
            #if box i can fit in box j, increase the max counter for box i
            if(is_compatible(box_lst[j], box_lst[i])):
            
                val = memo[j] + 1
                
                if(val>max):
                    max = val

        memo[i] = max

    total_max = 0;
    for max in memo:
        if max> total_max:
            total_max = max

    return total_max #max number of boxes that can fit inside eachother considering boxes 0...(n-1)

def max_box_num2(box_lst):
    """(-> (listof boxes) max_number_boxes_to_bring)"""
    assert isinstance(box_lst, list)
    box_lst = sorted(box_lst)

    # init next[] array
    #next[i] is the cloest compatible boxes starting from next[i]
    next_box = list()
    box_lst_len = len(box_lst)
    for idx in xrange(box_lst_len):
        next_box.append(box_lst_len)
        for next_idx in xrange(idx+1, box_lst_len):
            if is_compatible(box_lst[idx] ,box_lst[next_idx]):
                next_box[idx] = next_idx
                break

    # compute memo <-
    # base case and init memo
    # base case memo[box_lst_len+1] = 0
    memo = [0 for i in xrange(box_lst_len+1)]
    for idx in xrange(box_lst_len-1, -1, -1):
        memo[idx] = max(1+memo[next_box[idx]], memo[idx+1])

    return memo[0]

def results_output(box_lst, expected_result):

    output = max_box_num(box_lst)
    display = "(expected,actual) = (" + str(expected_result) + ", " + str(max_box_num(box_lst)) + ") -> " + "boxes: " + str(box_lst)

    print display

if __name__ == "__main__":
    
    #test suite:

    boxes = [(3,3,2)] 
    results_output(boxes, 1);

    boxes.append((1,2,1))
    results_output(boxes, 2);

    boxes.append((2,2,2))
    results_output(boxes, 2);

    boxes.append((2,3,2))
    results_output(boxes, 2); 

    boxes.append((3,3,2))
    results_output(boxes, 2);

    boxes.append((1,1,1))
    results_output(boxes, 2);

    boxes = [(1,2,3),(2,3,4),(3,4,5),(4,5,6)]
    results_output(boxes, 4);

    boxes = [(1,2,3),(3,4,5), (2,3,4), (4,5,6)]
    results_output(boxes, 4);

    boxes = [(1,2,10),(3,4,5), (2,3,4), (4,5,6)]
    results_output(boxes, 3);

    boxes = [(1,2,10),(3,4,5), (2,7,4), (4,5,6)]
    results_output(boxes, 2);

    boxes = [(3,3,2),(1,1,1)]
    results_output(boxes, 2);

    boxes = [(3,3,2),(2,1,1)]
    results_output(boxes, 2);

    boxes = [(3,3,2),(2,1,2)]
    results_output(boxes, 1);

    boxes = [(3,3,2),(2,2,1)]
    results_output(boxes, 2);

    boxes = [(3,3,2),(1,2,1)]
    results_output(boxes, 2);    