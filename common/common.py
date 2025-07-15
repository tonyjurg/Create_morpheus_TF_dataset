# File: common.py
# Project: github.com/tonyjurg/Create_morpheus_TF_dataset
# Version: 1.1 (4 July 2025)

"""
Utility functions for Text-Fabric syntactic labeling.

These helper functions are used across multiple repositories and Jupyter notebooks.
The primary purpose of this module is to refactor common code for consistency and to
avoid duplication, ensuring that all mappings remain strictly synchronized.

Usage in a Jupyter Notebook:
    import sys
    sys.path.insert(0, "../common")    # Adjust path to common.py as needed
    import common
"""

def find_parent(wordNode, F, L):
    """
    Find the nearest parent phrase or subphrase for the given word node.

    Parameters:
    
        wordNode (int) : The TF node ID for a word.
        F (obj)        : The Text-Fabric’s global namespace for node features.
        L (obj)        : The Text-Fabric’s global namespace for locality.

    Returns:
    
       tuple:
            - parent_node (int) : The Text-Fabric node ID of the parent phrase or subphrase.
            - subflag (str)     : An empty string for phrase, or 'sub' for subphrase.
       Note: tuple (None, None) is returned if no parent found.
            
    """
    for rel, flag in (("phrase", ""), ("subphrase", "sub")):
        parents = L.u(wordNode, rel)
        if parents:
            return parents[0], flag
    return None, None


def find_role(wordNode, F, L):
    """
    Determine the syntactic role of a word node.

    First tries the role directly on the word. If not found, it traverses upward
    through wg (word group) nodes to find an assigned role.

    Parameters:
    
        wordNode (int) : The TF node ID for a word.
        F (obj)        : The Text-Fabric’s global namespace for node features.
        L (obj)        : The Text-Fabric’s global namespace for locality.

    Returns:
    
        str or None: The role (e.g., 's', 'o', 'p'), or None if no role is found.
        
    """
    role = F.role.v(wordNode)
    if role is not None:
        return role

    for wg_node in L.u(wordNode, "wg"):
        role = F.role.v(wg_node)
        if role is not None:
            return role

    return None


def determine_pf(parent_node, morph, pos, lemma, role, F, L):
    """
    Determine the phrase function (pf) label for a word, based on parent phrase,
    morphology, POS, lemma, and syntactic role.

    The function:
    
        - Uses the function value of the parent node by default.
        - Overrides with known cases based on morphology (e.g. 'CONJ' → 'Conj').
        - Applies POS/lemma-specific overrides (e.g. interjection and ἰδοὺ).
        - Falls back on role-based mappings from MACULA conventions.
        - Returns 'Unkn' if no clear classification is found.

    Parameters:
    
        parent_node (int)  : Text-Fabric Node ID of the parent phrase/subphrase.
        morph (str)        : Morphological string, e.g., 'N-NSM'.
        pos (str)          : Part-of-speech tag, e.g., 'verb', 'noun', 'intj'.
        lemma (str)        : Lemma string of the word.
        role (str)         : Syntactic role from the TF data.
        F (obj)            : The Text-Fabric’s global namespace for node features.
        L (obj)            : The Text-Fabric’s global namespace for locality.

    Returns:
    
        str: One of the predefined phrase-function labels like 'Subj', 'Objc', etc.
    
    """
    pf = F.function.v(parent_node)

    # Special override: conjunctions are always 'Conj'
    if morph == "CONJ":
        return "Conj"

    # Special override: interjections and ἰδοὺ get classified as 'Intj'
    if pos == "intj" or lemma == "ὁράω":
        return "Intj"

    # If parent node has a phrase function, use it
    if pf is not None:
        return pf

    # Otherwise, derive from role mapping (based on MACULA conventions)
    match role:
        case "aux":
            return "Aux"
        case "o2" | "o":
            return "Objc"
        case "p":
            return "Pred"
        case "s":
            return "Subj"
        case "io":
            return "Cmpl"
        case "v" | "vc":
            return "Pred"
        case "apposition":
            return "Appo"
        case _:
            return "Unkn"
