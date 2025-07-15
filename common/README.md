# Common

The following mapping is carried out by a script `common.py` allowing to:

   - retrieves the canonical phrase function from the base annotation when available, 
   - assigns a pseudo-functional category to words outside any functionally labelled phrase, based on their part-of-speech and position within the clause, and 
   - applies this process consistently across both probabilistic modelling and entropy computations to maintain alignment.