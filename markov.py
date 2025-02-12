"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    read_file = open(file_path)
    contents = read_file.read()
    read_file.close()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    

    # Creating the keys for dict
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        key = (word1, word2)
        # Value = words[i + 2]
        # values = words[i + 2]

        values = []
        if i != len(words) - 2:

            values.append(words[i + 2])

        elif i == len(words) -2:
            values.append(None)
        
        # For loop getting values
        for i in range(len(words) - 2):
            if words[i] == word1:
                if words[i + 1] == word2: 
                    values.append(words[i + 2])
            
        chains[key] = chains.get(key, values)
        
        """
        words.find('word1 + " " + word2')
        words.count('word1 + " " + word2')
        """
        

    

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
