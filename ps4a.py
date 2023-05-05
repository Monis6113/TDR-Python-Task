# Problem Set 4A


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #def get_permutations(sequence):
    # Base case: if the sequence is a single character, there is only one permutation
    if len(sequence) == 1:
        return [sequence]

        # Recursive case: hold out the first character and find all permutations of the remaining characters
    permutations = []
    for i in range(len(sequence)):
            # Get the list of permutations for the remaining characters
        remaining_permutations = get_permutations(sequence[:i] + sequence[i+1:])
            # Insert the first character into each of the permutations of the remaining characters
        for permutation in remaining_permutations:
            permutations.append(sequence[i] + permutation)

    return permutations


    #pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
if __name__ == '__main__':
    print(get_permutations(''))
   # pass #delete this line and replace with your code here

