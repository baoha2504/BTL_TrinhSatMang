from vncorenlp import VnCoreNLP
from collections import Counter
import re

def simple_usage(sentences):
    vncorenlp_file = r'VnCoreNLP/VnCoreNLP-1.2.jar'

    # Use only word segmentation
    with VnCoreNLP(vncorenlp_file, annotators="wseg") as vncorenlp:
        string = vncorenlp.tokenize(sentences)
        # print('Tokenizing:', vncorenlp.tokenize(sentences))
        
        # Flatten the list of lists into a single list
        flat_list = [word for sublist in string for word in sublist]

        # Combine words into phrases of 2 words or more
        phrases = [' '.join(flat_list[i:i+2]) for i in range(len(flat_list) - 1)]

        # Remove phrases that contain only punctuation or numbers
        phrases = [phrase for phrase in phrases if re.match(r'[^\W\d]+(?:\s+[^\W\d]+)+', phrase)]

        # Count the occurrences of each phrase
        phrase_counts = Counter(phrases)

        # Get the top 6 most common phrases
        top_6_phrases = phrase_counts.most_common(6)

        parases = []
        # Display the top 6 phrases
        print("Top 6 most common phrases:")
        for phrase, count in top_6_phrases:
            text = f"{phrase}: {count} lần"
            parases.append(text)
        return parases



def detect_content(sentences):
    return simple_usage(sentences)
    