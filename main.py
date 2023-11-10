import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        MED[(S, T)] = len(T)
    elif T == "":
        MED[(S, T)] = len(S)
    else:
        if S[0] == T[0]:
            MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
        else:
            MED[(S, T)] = 1 + min(
                fast_MED(S[1:], T, MED),  # Deletion
                fast_MED(S, T[1:], MED),  # Insertion
                fast_MED(S[1:], T[1:], MED)  # Substitution
            )
    return MED[(S, T)]


def fast_align_MED(S, T, MED={}, alignments = {}):
    # TODO - keep track of alignment
     if (S, T) in alignments:
      return alignments[(S, T)]
  if S == "":
      MED[(S, T)] = len(T)
      alignments[(S, T)] = ("-" * len(T), T)
  elif T == "":
      MED[(S, T)] = len(S)
      alignments[(S, T)] = (S, "-" * len(S))
  else:
      if S[0] == T[0]:
          MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
          align_S, align_T = fast_align_MED(S[1:], T[1:], MED, alignments)
          alignments[(S, T)] = (S[0] + align_S, T[0] + align_T)
      else:
          del_cost = 1 + fast_MED(S[1:], T, MED)
          ins_cost = 1 + fast_MED(S, T[1:], MED)
          sub_cost = 1 + fast_MED(S[1:], T[1:], MED)
          if del_cost <= ins_cost and del_cost <= sub_cost:
              align_S, align_T = fast_align_MED(S[1:], T, MED, alignments)
              alignments[(S, T)] = (S[0] + align_S, "-" + align_T)
          elif ins_cost <= del_cost and ins_cost <= sub_cost:
              align_S, align_T = fast_align_MED(S, T[1:], MED, alignments)
              alignments[(S, T)] = ("-" + align_S, T[0] + align_T)
          else:
              align_S, align_T = fast_align_MED(S[1:], T[1:], MED, alignments)
              alignments[(S, T)] = (S[0] + align_S, T[0] + align_T)
  return alignments[(S, T)]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
