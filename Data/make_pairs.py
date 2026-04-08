##################################################
# Georgia Doing (doingg@union.edu)
# 4/8/26
# In-class example of making
##################################################

# load random library
import random

# lists of students and their expertise
csc = ['Seo', 'Tyler', 'Laurus', 'Kai', 'Ryan','Lizzy', 'Jared', 'Nick', 'MaryGrace']
bio = ['Addie', 'Emma', 'Jackson','Finn', 'Alexander', 'Maryann', 'Jasmine','Cody']
both = ['Eva', 'Sofia', 'Willoughby', 'Annabelle']


# even out lists for pairing
def make_lists(l_bio, l_cs, l_both):
    ''' pads lists l_bio and l_cs with names from
    l_both, randomly, to make two evenly sized lists.
    note: if there is an off number of students, bio list
    gets one more'''
    
    class_size = len(l_bio) + len(l_cs) + len(l_both)
    n_pairs = class_size // 2

    # shuffle both list
    l_shuff = l_both.copy()
    random.shuffle(l_shuff)

    # assemble lists
    b = l_bio + l_shuff[n_pairs-len(l_cs):]
    c = l_cs + l_shuff[0:n_pairs-len(l_cs)]
    
    return b, c

# assign students to groups
def make_pairs(b, c, num_pairs=2):
    ''' randomly pairs names from lists b and c,
    default pair size is 2'''
    
    # group nums based off of cs list, shorter
    num_groups = len(c)
    groups = [[]]*num_groups

    # shuffle each group
    b_shuff = b.copy()
    c_shuff = c.copy()
    random.shuffle(b_shuff)
    random.shuffle(c_shuff)

    # start counting pairs
    i = 0

    # repeat selection for as many groups as needed
    for g in range(num_groups):
        # make sure index is in range
        if i < len(c):
            # add one student to the pair, randomly, from each group
            groups[g] = groups[g] + [c_shuff[i]]
            groups[g] = groups[g] + [b_shuff[i]]
            i += 1
    # in case there is an odd num of students, randomly make tripple
    if len(b) > len(c):
        g = random.randint(0,num_groups)
        groups[g] = groups[g] + [b_shuff[-1]]

    return groups

def main():
    b, c = make_lists(bio,csc,both)
    groups = make_pairs(b,c,3)

    for g in groups:
        print(g)

main()
