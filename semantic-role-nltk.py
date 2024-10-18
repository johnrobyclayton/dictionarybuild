import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags

# Ensure the necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define a simple rule-based function for SRL
def simple_srl(sentence):
    # Tokenize and POS tag the sentence
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)
    print(pos_tags)
    # Initialize empty roles
    agent = None
    action = None
    destination = None
    time = None

    # Identify roles based on POS tags and simple heuristics
    for i, (word, pos) in enumerate(pos_tags):
        # Identify the action (verb)
        if pos.startswith('VB'):
            action = word
        
        # Identify the agent (noun before verb)
        if pos.startswith('NN') and not agent and i < len(pos_tags) - 1 and pos_tags[i+1][1].startswith('VB'):
            agent = word
        
        # Identify the destination (preposition followed by noun)
        if (pos.startswith('IN') or pos.startswith('TO')) and i < len(pos_tags) - 1 and pos_tags[i+1][1].startswith('NN'):
            destination = " ".join([word] + [tokens[i+1]])
        
        # Identify time/frequency (adverb or noun phrase indicating time)
        if pos in ('RB', 'NN') and word.lower() in ['every', 'day', 'week', 'month', 'year']:
            time = word

    return agent, action, destination, time

# Input sentence
sentence = "The boy goes to school every day."

# Perform simple SRL
agent, action, destination, time = simple_srl(sentence)

# Output the results
print(f"Agent: {agent}")
print(f"Action: {action}")
print(f"Destination: {destination}")
print(f"Time: {time}")